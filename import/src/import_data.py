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

def export_data(src_dir, target_dir):
    tgt_files = tgt_dir.glob('*.txt')
    src_files = src_dir.glob('*.txt')
    
    tgt_files_set = set(t.name for t in tgt_files)
    todo_src_files = [s for s in src_files if s.name not in tgt_files_set]

    for s_file in todo_src_file:
        shutil.copyfile(src_file, target_dir / src_file.name)

    print(f'{target_dir}: #{len(todo_src_file)} copied')

def main():
    src_parent_dir = Path(sys.argv[1])
    tgt_parent_dir = Path(sys.argv[2])

    for tgt_name, src_name in DeptNameDict.items():
        tgt_name = tgt_name.replace(' ', '_')
        
        tgt_dir = tgt_parent_dir / tgt_name
        src_dir = src_parent_dir / f'{src_name}2024}'
        export_data(src_dir, tgt_dir)

        
        
        


    
    


