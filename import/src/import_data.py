import datetime
import json
import shutil
import sys

from pathlib import Path

DeptNameDict = {
    "Agriculture, Dairy Development, Animal Husbandry and Fisheries Department": 'mahagri',
    "Co-operation, Textiles and Marketing Department": 'mahcoop',
    "Environment Department": 'mahenv',
    "Finance Department": 'mahfin',
    "Food, Civil Supplies and Consumer Protection Department": 'mahfood',
    "General Administration Department": 'mahadmin',
    "Higher and Technical Education Department": 'mahtech',
    "Home Department": 'mahhome',
    "Housing Department":  'mahhouse',
    "Industries, Energy and Labour Department":  'mahind',
    "Information Technology Department":  'mahit',
    "Law and Judiciary Department": 'mahlaw',
    "Marathi Language Department": 'mahmar',
    "Medical Education and Drugs Department":  'mahmed',
    "Minorities Development Department": 'mahmin',
    "Other Backward Bahujan Welfare Department":  'mahbah',
    "Parliamentary Affairs Department": 'mahpar',
    "Persons with Disabilities Welfare Department": 'mahdis',
    "Planning Department":  'mahplan',
    "Public Health Department": 'mahhea',
    "Public Works Department": 'mahpwd',
    "Revenue and Forest Department": 'mahrev',
    "Rural Development Department": 'mahrural',
    "School Education and Sports Department": 'mahedu',
    "Skill Development and Entrepreneurship Department": 'mahskill',
    "Social Justice and Special Assistance Department": 'mahsoc',
    "Soil and Water Conservation Department": 'mahsoil',
    "Tourism and Cultural Affairs Department": 'mahtour',
    "Tribal Development Department": 'mahtrib',
    "Urban Development Department": 'mahurb',
    "Water Resources Department": 'mahwater',
    "Water Supply and Sanitation Department": 'mahsanit',
    "Women and Child Development Department": 'mahwom'
}

Year = 2024

def get_tgt_info(src_info):
    tgt_info = {}
    tgt_info['url'] = src_info['Download']
    tgt_info['dept'] = src_info['Department Name']
    tgt_info['text'] = src_info['Title']
    tgt_info['code'] = src_info['Unique Code']
    tgt_info['date'] = src_info['G.R. Date']
    tgt_info['size_kb'] = src_info['File Size (KB)']
    tgt_info['name'] = f'{src_info["Unique Code"]}.pdf'
    tgt_info['order_number'] = src_info.get("order_number", '')
    tgt_info['order_type'] = src_info.get("order_type", '')
    return tgt_info

def export_data(src_dir, tgt_dir):
    def get_code(src_file):
        code, _ = src_file.name.split('.', 1)
        return code.replace('\u200d', '')

    def get_date_str(dt):
        if isinstance(dt, str):
            d, m, y = dt.split('-')
            dt = datetime.date(year=int(y), month=int(m), day=int(d))
        return dt.strftime('%d %b %Y')

    def get_urls(info):
        code, url = info['code'], info['url']
        mr_path, en_path = f'{tgt_dir}/{code}.pdf.mr.txt', f'{tgt_dir}/{code}.pdf.en.txt'
        return f'[{code}.pdf]({url}) [mr]({mr_path}) [en]({en_path})'

    def get_date_code(info):
        dt = info.get('date', None)
        d, m, y = dt.split('-')
        dt = datetime.date(year=int(y), month=int(m), day=int(d))
        return dt, info['code']

    tgt_files = list(tgt_dir.glob('*.txt'))
    src_files = list(src_dir.glob('*.txt'))

    tgt_files_set = set(t.name for t in tgt_files)
    tgt_json_path = tgt_dir / 'GRs.json'
    tgt_dict = json.loads(tgt_json_path.read_text())

    tgt_new_json_path = tgt_dir / 'GRs-new.json'
    tgt_new_infos = json.loads(tgt_new_json_path.read_text()) if tgt_new_json_path.exists() else []

    todo_src_files = [s for s in src_files if s.name not in tgt_files_set]

    src_json_path = src_dir / 'GRs.json'
    src_infos = json.loads(src_json_path.read_text()) if src_json_path.exists() else []
    src_dict = {i["Unique Code"]:i for i in src_infos}

    num_tgt_mr_files = len([f for f in tgt_files if '.mr.txt' in f.name])
    num_tgt_en_files = len([f for f in tgt_files if '.en.txt' in f.name])

    todo_written = 0
    for src_file in todo_src_files:
        todo_code = get_code(src_file)
        shutil.copyfile(src_file, tgt_dir / src_file.name)
        #print(f'copying {src_file} -> {tgt_dir / src_file.name}')
        if '.en.txt' in src_file.name:
            todo_info = get_tgt_info(src_dict[todo_code])
            tgt_dict[f'{todo_code}.pdf'] = todo_info

            src_info = src_dict[todo_code]
            tgt_new_infos.append(src_info)
            todo_written += 1

    tgt_json_path.write_text(json.dumps(tgt_dict))
    tgt_new_json_path.write_text(json.dumps(tgt_new_infos))
    print(f'{tgt_dir}: #{len(todo_src_files)} copied')

    tgt_infos = list(tgt_dict.values())
    tgt_infos = [i for i in tgt_infos if i['date']]
    tgt_infos.sort(key=get_date_code)

    first, last = tgt_infos[0], tgt_infos[-1]

    first_date, last_date = get_date_str(first['date']), get_date_str(last['date'])
    num_mr, num_en = str(num_tgt_mr_files + todo_written), str(num_tgt_en_files + todo_written)
    start_urls, last_urls = get_urls(first), get_urls(last)

    return [first_date, last_date, num_mr, num_en, start_urls, last_urls]

def write_readme(lines):
    header = ['Num', 'Department Name', 'Start Date', 'Last Date', \
              '# Marathi Orders', '# Translated Orders', 'Starting Order', 'Last Order']
    total_orders, total_translated = sum(int(ln[4]) for ln in lines), sum(int(ln[5]) for ln in lines)
    insert_lines = ['## Data Details', '']
    insert_lines += [f'| {" | ".join(header)} |']
    insert_lines += [f'| {" | ".join(["-" * len(h) for h in header])} |']
    insert_lines += [f'| {" | ".join(ln)} |' for ln in lines]
    insert_lines += ['-' * 100]
    insert_lines += ['']
    insert_lines += [f'**Total Orders**: {total_orders:,} and **Total Translated Orders**: {total_translated:,}']

    readme_file = Path("README.md")
    readme_lines = readme_file.read_text().split("\n")
    if '## Data Details' in readme_lines:
        s_idx, e_idx = readme_lines.index("## Data Details"), readme_lines.index("## Accessing Data")
        readme_lines = readme_lines[:s_idx] + insert_lines + readme_lines[e_idx:]
    else:
        ins_idx = readme_lines.index("## Accessing Data")
        readme_lines = readme_lines[:ins_idx] + insert_lines + readme_lines[ins_idx:]
    readme_file.write_text("\n".join(readme_lines))

def main():
    src_parent_dir = Path(sys.argv[1])
    tgt_parent_dir = Path(sys.argv[2])

    # need to add last_crawl_date


    table_lines = []
    for (idx, (tgt_name, src_name)) in enumerate(DeptNameDict.items()):
        tgt_name = tgt_name.replace(' ', '_')
        tgt_dir = tgt_parent_dir / tgt_name

        src_stub_dir = Path(f'{src_name}2024') / 'export' / Path(f'orgpedia_{src_name}2024')
        src_dir = src_parent_dir / src_stub_dir

        if src_dir.exists():
            line = export_data(src_dir, tgt_dir)
            line = [str(idx+1), tgt_name.replace('_', ' ')] + line
            print(f'{src_name} {line}')
            table_lines.append(line)
        else:
            print(f'src_dir not found: {str(src_dir)}')

    write_readme(table_lines)
    return 0

main()

"""
{
  "201803161624182101.pdf": {
    "url": "https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803161624182101.pdf",
    "dept": "Agriculture, Dairy Development, Animal Husbandry and Fisheries Department",
    "text": "Regarding the transfer of 21493.30 m.sq. land area to BMC for building for the 18.30 meter service from Shivdham Cemetary to Aarey Chek Post near Jogeshwari Western Express Way.",
    "code": "201803161624182101",
    "date": "16-03-2018",
    "size_kb": "126",
    "name": "mahagri-1.pdf",
    "num_pages": 2,
    "large_image_idxs": [],
    "crawl_dir": "31-Mar-2022"
  },
"""


"""

  {
    "SN": "43",
    "Department Name": "Urban Development Department",
    "Title": "Release of surcharge on stamp duty to Nagpur Metro Rail Project to the implementing agencies of the Vital Urban Transport Project of Mumbai, Nagpur and Pune Metro Railway from the amount deposited against 1 stamp duty surcharge as per the provisions of the Mumbai Municipal Corporation Act-1888 and the Maharashtra Municipal Corporation Act-1949",
    "Unique Code": "202401101814396825",
    "G.R. Date": "10-01-2024",
    "File Size (KB)": "213",
    "Download": "https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202401101814396825.pdf",
    "wayback": {
      "url": "https://web.archive.org/web/20240112190710/https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202401101814396825.pdf",
      "sha1": "3TCVLDAFCQAFCG5N6EM7N6QBFSDENW2X",
      "length": "204942",
      "status": true
    },
    "archive": {
      "url": "http://s3.us.archive.org/in.gov.maharashtra.gr.202401101814396825/202401101814396825.pdf",
      "identifier": "in.gov.maharashtra.gr.202401101814396825",
      "status": true
    },
    "status": "exported",
    "mr_file": "202401101814396825.pdf.mr.txt",
    "en_file": "202401101814396825.pdf.en.txt",
    "order_number": "एमआरडी-३३२३/प्र.क्र.९०(भाग-२)/नवि-७",
    "order_type": "शासन निर्णय क्रमांक"
  },

"""
