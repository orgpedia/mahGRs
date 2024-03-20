# Government Resolutions, Government of Maharashtra

This repository contains government resolutions issued by the Government of Maharashtra for the last five years, there are two files for each resolution 1) original marathi (txt file) and 2) english translation of that resolution (txt file). The original government resolutions can be found at https://gr.maharashtra.gov.in/1145/Government-Resolutions.

The English translation is obtained by processing each the pdf file of each Government Resolution through a pipeline where the following operations are performed 1) Download the file using crawler 2) OCR to handle non-standard fonts 3) paragraph detection 4) table  detection 5) translation to English. This pipeline is run in sepearate repositories check out orgpedia/mah* for each department.


## Data Details

| Num | Department Name | Start Date | Last Date | # Marathi Orders | # Translated Orders | Starting Order | Last Order |
| --- | --------------- | ---------- | --------- | ---------------- | ------------------- | -------------- | ---------- |
| 1 | Agriculture, Dairy Development, Animal Husbandry and Fisheries Department | 16 Mar 2018 | 12 Feb 2024 | 7743 | 7743 | [201803161624182101.pdf](url) [mr](GRs/Agriculture,_Dairy_Development,_Animal_Husbandry_and_Fisheries_Department/201803161624182101.pdf.mr.txt) [en](GRs/Agriculture,_Dairy_Development,_Animal_Husbandry_and_Fisheries_Department/201803161624182101.pdf.en.txt) | [202402121502319001.pdf](url) [mr](GRs/Agriculture,_Dairy_Development,_Animal_Husbandry_and_Fisheries_Department/202402121502319001.pdf.mr.txt) [en](GRs/Agriculture,_Dairy_Development,_Animal_Husbandry_and_Fisheries_Department/202402121502319001.pdf.en.txt) |
| 2 | Co-operation, Textiles and Marketing Department | 19 Mar 2018 | 28 Feb 2024 | 4783 | 4783 | [201803191257576702.pdf](url) [mr](GRs/Co-operation,_Textiles_and_Marketing_Department/201803191257576702.pdf.mr.txt) [en](GRs/Co-operation,_Textiles_and_Marketing_Department/201803191257576702.pdf.en.txt) | [202402281753053702.pdf](url) [mr](GRs/Co-operation,_Textiles_and_Marketing_Department/202402281753053702.pdf.mr.txt) [en](GRs/Co-operation,_Textiles_and_Marketing_Department/202402281753053702.pdf.en.txt) |
----------------------------------------------------------------------------------------------------

**Total Orders**: 12,526 and **Total Translated Orders**: 12,526
## Accessing Data

The easist way to access the data is to clone the repository or download the data as a zip file (Click the green button '< > Code' at the top. All the files are arranged as per department and are in the [GRs](GRs) directory.

Please note that the repository even though it contains only txt file is about 1GB in size.

## Running Chatbot

You can run a simple Q & A chatbot on this data using [chat.py](chat.py), a simple chat applications that has no external depedencies and requires you to run [Qdrant](https://qdrant.tech/) vector database, have need to have `curl` on your machine and have an [OpenAI API Key](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key).

Start qdrant on your local machine
```shell
docker pull qdrant/qdrant
docker run -p 6333:6333 qdrant/qdrant
```

Provide Open AI API Key, this chat app uses two APIs embeddings and completions.
```shell
export OPENAI_API_KEY='XXX'
```

This will start the chat app on all the orders (GRs) that have 'library' keyword in their subject.

```shell
python chat.py GRs/Higher_and_Technical_Education_Department library
```

![screenshot of running chat.py](screenshot.png)

* You get clickable links in references if you run in iTerm2 *.

## Thanks

Orgpedia would like to thank [AI4Bharat](https://ai4bharat.iitm.ac.in/) for releasing [IndicTrans2](https://github.com/AI4Bharat/IndicTrans2).

Thanks to its accuracy and performance Orgpedia was able to translate over 50,000 documents relatively quickly and at a fraction of the price of the online servicess.











