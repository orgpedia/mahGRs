import cmd
import datetime
import json
import logging
import os
import subprocess
import sys
from pathlib import Path


Qdrant_URL = "http://localhost:6333"
Openai_URL = "https://api.openai.com"
LogFileName = ".chat.log"
MaxTokens = 8191


class ChatBot:
    def __init__(self, index_name, doc_paths):
        self.index_name = index_name
        self.doc_paths = list(doc_paths)

        self.dept_dir = doc_paths[0].parent
        self.emb_dir = self.dept_dir / ".embs"
        self.emb_dir.mkdir(exist_ok=True)

        self.openai_api_key = os.environ.get("OPENAI_API_KEY", "")
        if not self.openai_api_key:
            print("Unable to find OpenAI API Key, quitting")
            sys.exit(4)

        self.emb_model = "text-embedding-ada-002"
        self.chat_model = "gpt-4"

        # This stores the id used by Qdrant to actual document name
        self.id_doc_file = self.emb_dir / "id_doc.json"
        if self.id_doc_file.exists():
            self.id_doc_dict = json.loads(self.id_doc_file.read_text())
        else:
            self.id_doc_dict = {}

        docs_dict = json.loads((self.dept_dir / "GRs.json").read_text())
        self.doc_url_dict = dict((f'{v["code"]}.pdf.en.txt', v["url"]) for v in docs_dict.values())

        self.query_texts = {}
        query_text_files = self.emb_dir.glob("query-*.en.txt")
        self.query_texts = dict((f.read_text().strip(), f) for f in query_text_files)

        self.lgr = logging.getLogger(__name__)
        self.lgr.setLevel(logging.DEBUG)

        self.file_handler = logging.FileHandler(LogFileName, mode="a")  # Change to a
        self.file_handler.setLevel(logging.DEBUG)
        self.lgr.addHandler(self.file_handler)
        self.lgr.debug(f"<< Started {len(self.doc_paths)} docs {datetime.datetime.today()}")

    def get_url(self, doc_path):
        return self.doc_url_dict[Path(doc_path).name]

    def gen_doc_embeddings(self, doc_paths):
        emb_files = []
        for doc_path in doc_paths:
            assert ".en.txt" in doc_path.name

            emb_path = self.emb_dir / doc_path.name.replace(".en.txt", ".en.emb.json")
            if emb_path.exists():
                emb_files.append(emb_path)
                continue

            lines = doc_path.read_text()
            lines = [ln for ln in lines if ln[:6] != "# Page"]

            success = self.gen_embeddings(" ".join(lines), emb_path)
            if success:
                emb_files.append(emb_path)
        return emb_files

    def gen_embeddings(self, text, save_path):
        self.lgr.debug(f"Generating embedding: {text[:20]}")
        text = text.replace("\n", " ")

        if len(text) > MaxTokens * 2:  # approximation, please use tiktoken
            # print(f'Error generating embedding, #tokens > {MaxTokens}')
            self.lgr.debug(f"Error generating embedding, #tokens > {MaxTokens}")
            return False

        cmd = ["curl", "-s", f"{Openai_URL}/v1/embeddings"]
        cmd += ["-H", "Content-Type: application/json"]
        cmd += ["-H", f"Authorization: Bearer {self.openai_api_key}"]
        cmd += ["-d", json.dumps({"input": text, "model": self.emb_model})]

        try:
            output = subprocess.check_output(cmd)
            emb_json = json.loads(output)
        except subprocess.CalledProcessError as e:
            print(f"\t** Unable to get embeddings returncode: {e.returncode}")
            emb_json = output = "error"

        if "error" in emb_json:
            print(f"Error generating embedding {output}")
            self.lgr.debug(f"Error generating embedding {output}")
            return False
        else:
            save_path.write_bytes(output)
            self.lgr.debug(f"generated embedding {save_path}")
            return True

    def build_index(self):
        self.lgr.debug("Build Index")

        def create_collection(name, dist_measure, vec_size):
            cmd = ["curl", "-s", "-X", "PUT", f"{Qdrant_URL}/collections/{name}"]
            cmd += [
                "-H",
                "Content-Type: application/json",
            ]
            cmd += ["-d", json.dumps({"vectors": {"size": vec_size, "distance": dist_measure}})]
            output = subprocess.check_output(cmd)  # noqa

        def add_points(name, all_points):
            for points in all_points:
                cmd = [
                    "curl",
                    "-s",
                    "-L",
                    "-X",
                ]
                cmd += ["PUT", f"{Qdrant_URL}/collections/{self.index_name}/points?wait=true"]
                cmd += ["-H", "Content-Type: application/json"]
                cmd += ["--data-raw", json.dumps({"points": [points]})]
                output = subprocess.check_output(cmd)  # noqa

        indexed_docs = set(self.id_doc_dict.values())
        missing_docs = [d for d in self.doc_paths if d.name not in indexed_docs]
        if not missing_docs:
            self.lgr.debug("Index exists")
            return

        print("Building index will take some time...")

        embedding_files = self.gen_doc_embeddings(missing_docs)
        if not embedding_files:
            return

        # load embeddings
        vec_size, points = 0, []
        for emb_file in embedding_files:
            emb_id = len(self.id_doc_dict) + 1
            emb_vec = json.loads(emb_file.read_text())["data"][0]["embedding"]

            doc_name = emb_file.name.replace(".emb.json", ".txt")

            points.append({"id": emb_id, "vector": emb_vec, "payload": {"doc_name": doc_name}})
            self.id_doc_dict[str(emb_id)] = doc_name
            vec_size = max(len(emb_vec), vec_size)

        create_collection(self.index_name, "Cosine", vec_size)
        add_points(self.index_name, points)
        self.id_doc_file.write_text(json.dumps(self.id_doc_dict))
        self.lgr.debug(f"Done building index, added points: {len(points)}")

    def query(self, query_text):
        self.lgr.debug(f"Query: {query_text}")

        def search(query_vec):
            cmd = [
                "curl",
                "-s",
                "-L",
                "-X",
            ]
            cmd += ["POST", f"{Qdrant_URL}/collections/{self.index_name}/points/search"]
            cmd += [
                "-H",
                "Content-Type: application/json",
            ]
            cmd += ["--data-raw", json.dumps({"vector": query_vec, "limit": 3})]

            output = subprocess.check_output(cmd)
            result_dict = json.loads(output)
            if "result" not in result_dict:
                return []

            result_ids = [r["id"] for r in result_dict["result"]]
            return result_ids

        if query_text in self.query_texts:
            self.lgr.debug("\tQuery: Found embeddings")
            txt_file = self.query_texts[query_text]
            emb_file = txt_file.parent / txt_file.name.replace(".en.txt", ".en.emb.json")
            query_vec = json.loads(emb_file.read_text())["data"][0]["embedding"]
        else:
            self.lgr.debug("\tQuery: Generating embeddings")
            idx = len(self.query_texts) + 1
            txt_file = self.emb_dir / f"query-{idx}.en.txt"  # store query also in the emb dir
            emb_file = self.emb_dir / f"query-{idx}.en.emb.json"

            success = self.gen_embeddings(query_text, emb_file)
            if success:
                txt_file.write_text(query_text)
                self.query_texts[query_text] = emb_file
                query_vec = json.loads(emb_file.read_text())["data"][0]["embedding"]
            else:
                query_vec = []

        if not query_vec:
            self.lgr.debug("Embedding not found")
            return []

        result_ids = search(query_vec)
        result_docs = [self.id_doc_dict[str(i)] for i in result_ids]
        result_doc_paths = [self.dept_dir / d for d in result_docs]

        self.lgr.debug(f"Done querying: {len(result_docs)}")
        return result_doc_paths

    def completion(self, query_text, doc):
        self.lgr.debug(f"completion_api: {query_text}")

        def call_completion(messages):
            cmd = ["curl", "-s", f"{Openai_URL}/v1/chat/completions"]
            cmd += [
                "-H",
                "Content-Type: application/json",
            ]
            cmd += ["-H", f"Authorization: Bearer {self.openai_api_key}"]
            cmd += ["-d", json.dumps({"model": self.chat_model, "messages": messages})]

            try:
                output = subprocess.check_output(cmd)
            except subprocess.CalledProcessError as e:
                print(f"\t** Unable to get completions: {e.returncode}")
                return {"error": {"message": f"called process erroror: {e.returncode}"}}

            return json.loads(output)

        sys_msg = "You are an expert in government resolutions, answer very precisely and succintly"
        prompt = f"In the following government resolution - {query_text}\n---\n{doc}"
        messages = [{"role": "system", "content": sys_msg}, {"role": "system", "content": prompt}]

        result = call_completion(messages)
        self.lgr.debug("completion_api")

        if "choices" not in result:
            return f'Error: {result["error"]["message"]}'

        return result["choices"][0]["message"]["content"]

    def chat(self, query_text):
        doc_paths = self.query(query_text)
        self.file_handler.flush()

        if not doc_paths:
            return "Unable to find matching documents", []

        result = self.completion(query_text, doc_paths[0].read_text())
        return result, doc_paths


class ChatShell(cmd.Cmd):
    question_num = 1
    prompt = f"> Question [{question_num}]:\n"

    def __init__(self, chat):
        cmd.Cmd.__init__(self)
        self.chat = chat

    def emptyLine(self):
        pass

    def print_link(self, doc):
        term_program = os.environ.get("TERM_PROGRAM", "")
        pdf_name = doc.name.replace(".en.txt", "")

        if "iTerm" in term_program:
            doc_url = self.chat.get_url(doc.name)
            escape_mask = "\033]8;{};{}\033\\{}\033]8;;\033\\"
            print(escape_mask.format("", doc_url, f"[{pdf_name}]"), end=" ")
        else:
            print(f"[{pdf_name}]", end=" ")

    def do_exit(self, arg):
        return self.do_quit(arg)

    def do_bye(self, arg):
        return self.do_quit(arg)

    def do_quit(self, arg):
        print("Quitting...")
        return True

    def default(self, q):
        if not q.strip():
            return

        if q.strip().lower() in ("exit", "quit", "q", "x"):
            self.close()

        result, doc_paths = self.chat.chat(q)

        print(f"\n> Answer [{self.question_num}]:")
        print(result)

        if doc_paths:
            print("\nReferences:")
            [self.print_link(d) for d in doc_paths]
        print("\n")
        self.question_num += 1
        self.prompt = f"> Question [{self.question_num}]:\n"


def chat_shell(chat):
    chat_shell = ChatShell(chat)
    chat_shell.cmdloop()


def get_matching_docs(dept_dir, keywords):
    def has_keywords(text):
        return any(k in text.lower() for k in keywords) if keywords else True

    keywords = [k.lower() for k in keywords]

    docs_dict = json.loads((dept_dir / "GRs.json").read_text())
    matching_doc_names = [k for k, v in docs_dict.items() if has_keywords(v["text"])]

    return [dept_dir / f"{d}.en.txt" for d in matching_doc_names]


def main():
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} <dept_dir> [<keywords>]")
        sys.exit(1)

    dept_dir = Path(sys.argv[1])
    keywords = sys.argv[2:]

    print(f"Department: {dept_dir.name}")
    print(f"Keywords: {keywords}")

    if not (dept_dir / "GRs.json").exists():
        print(f"Unable to locate GRs.json in {dept_dir}, quitting")
        sys.exit(2)

    # Only 1 index per department !!
    matching_docs = get_matching_docs(dept_dir, keywords)

    chat = ChatBot(dept_dir.name, matching_docs)
    chat.build_index()

    print("\n-----------")

    chat_shell(chat)


main()
