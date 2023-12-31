# Government Resolutions, Government of Maharashtra

This repository contains government resolutions issued by the Government of Maharashtra for the last five years, there are two files for each resolution 1) original marathi (txt file) and 2) english translation of that resolution (txt file). The original government resolutions can be found at https://gr.maharashtra.gov.in/1145/Government-Resolutions.


The English translation is obtained by processing each the pdf file of each Government Resolution through a pipeline where the following operations are performed 1) Download the file using crawler 2) OCR to handle non-standard fonts 3) paragraph detection 4) table  detection 5) translation to English. This pipeline is run in sepearate repositories check out orgpedia/mah* for each department.


## Data Details

| Num | Department Name | Start Date | Last Date | Last Crawl Date | # Marathi Orders | # Translated Orders | Starting Order | Last Order |
| --- | --------------- | ---------- | --------- | --------------- | ---------------- | ------------------- | -------------- | ---------- |
| 1 | [Agriculture, Dairy Development, Animal Husbandry and Fisheries Department](GRs/Agriculture,_Dairy_Development,_Animal_Husbandry_and_Fisheries_Department) | 16 March 2018 | 22 December 2023 | 22-Dec-2023 | 3634 | 3573 | [201803161624182101.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803161624182101.pdf) | [202312221518258301.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312221518258301.pdf) |
| 2 | [Co-operation, Textiles and Marketing Department](GRs/Co-operation,_Textiles_and_Marketing_Department) | 19 March 2018 | 19 December 2023 | 22-Dec-2023 | 2271 | 2230 | [201803191257576702.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803191257576702.pdf) | [202312191735299602.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312191735299602.pdf) |
| 3 | [Environment Department](GRs/Environment_Department) | 02 December 2017 | 09 November 2023 | 26-Nov-2023 | 336 | 327 | [201712041147216904.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201712041147216904.pdf) | [202311091716582504.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311091716582504.pdf) |
| 4 | [Finance Department](GRs/Finance_Department) | 14 January 2021 | 08 December 2023 | 09-Dec-2023 | 615 | 609 | [202101141237329905.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202101141237329905.pdf) | [202312081246357605.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312081246357605.pdf) |
| 5 | [Food, Civil Supplies and Consumer Protection Department](GRs/Food,_Civil_Supplies_and_Consumer_Protection_Department) | 05 February 2018 | 20 December 2023 | 22-Dec-2023 | 895 | 887 | [201802121244545806.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201802121244545806.pdf) | [202312201650378506.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312201650378506.pdf) |
| 6 | [General Administration Department](GRs/General_Administration_Department) | 16 March 2018 | 22 December 2023 | 22-Dec-2023 | 4013 | 3993 | [201803161224022707.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803161224022707.pdf) | [202312221756089407.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312221756089407.pdf) |
| 7 | [Higher and Technical Education Department](GRs/Higher_and_Technical_Education_Department) | 12 October 2017 | 22 December 2023 | 22-Dec-2023 | 2331 | 2326 | [201710121514029708.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201710121514029708.pdf) | [202312221913418008.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312221913418008.pdf) |
| 8 | [Home Department](GRs/Home_Department) | 22 October 2008 | 22 December 2023 | 22-Dec-2023 | 8087 | 3542 | [20081022.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/20081022.pdf) | [202312221921220829.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312221921220829.pdf) |
| 9 | [Housing Department](GRs/Housing_Department) | 16 November 2017 | 22 November 2023 | 26-Nov-2023 | 322 | 318 | [201711161447076609.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201711161447076609.pdf) | [202311221219205209.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311221219205209.pdf) |
| 10 | [Industries, Energy and Labour Department](GRs/Industries,_Energy_and_Labour_Department) | 15 March 2018 | 18 December 2023 | 22-Dec-2023 | 1703 | 1698 | [201803151204055010.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803151204055010.pdf) | [202312181657291710.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312181657291710.pdf) |
| 11 | [Information Technology Department](GRs/Information_Technology_Department) | 20 January 2018 | 15 December 2023 | 16-Dec-2023 | 110 | 110 | [201801201843024511.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201801201843024511.pdf) | [202312151508137711.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312151508137711.pdf) |
| 12 | [Law and Judiciary Department](GRs/Law_and_Judiciary_Department) | 17 March 2018 | 22 December 2023 | 22-Dec-2023 | 1662 | 1646 | [201803171129290212.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803171129290212.pdf) | [202312221712028312.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312221712028312.pdf) |
| 13 | [Marathi Language Department](GRs/Marathi_Language_Department) | 22 February 2018 | 22 December 2023 | 22-Dec-2023 | 304 | 302 | [201802031549154233.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201802031549154233.pdf) | [202312221750521233.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312221750521233.pdf) |
| 14 | [Medical Education and Drugs Department](GRs/Medical_Education_and_Drugs_Department) | 12 March 2018 | 20 December 2023 | 22-Dec-2023 | 962 | 918 | [201803121137094813.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803121137094813.pdf) | [202312201725520313.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312201725520313.pdf) |
| 15 | [Minorities Development Department](GRs/Minorities_Development_Department) | 09 March 2018 | 20 December 2023 | 22-Dec-2023 | 846 | 841 | [201803091218355314.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803091218355314.pdf) | [202312201320164914.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312201320164914.pdf) |
| 16 | [Other Backward Bahujan Welfare Department](GRs/Other_Backward_Bahujan_Welfare_Department) | 07 March 2022 | 22 December 2023 | 22-Dec-2023 | 441 | 439 | [202203081752439334.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202203081752439334.pdf) | [202312221305448534.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312221305448534.pdf) |
| 17 | [Parliamentary Affairs Department](GRs/Parliamentary_Affairs_Department) | 12 October 2017 | 22 November 2023 | 26-Nov-2023 | 105 | 105 | [201710031642378615.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201710031642378615.pdf) | [202311221247565415.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311221247565415.pdf) |
| 18 | [Persons with Disabilities Welfare Department](GRs/Persons_with_Disabilities_Welfare_Department) | 04 January 2023 | 19 December 2023 | 22-Dec-2023 | 43 | 43 | [202301041906309635.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202301041906309635.pdf) | [202312191658375135.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312191658375135.pdf) |
| 19 | [Planning Department](GRs/Planning_Department) | 09 March 2018 | 19 December 2023 | 22-Dec-2023 | 1368 | 1348 | [201803091441032716.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803091441032716.pdf) | [202312191655008716.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312191655008716.pdf) |
| 20 | [Public Health Department](GRs/Public_Health_Department) | 08 February 2018 | 11 December 2023 | 22-Dec-2023 | 5198 | 5161 | [201801311722275417.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201801311722275417.pdf) | [202312111314096017.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312111314096017.pdf) |
| 21 | [Public Works Department](GRs/Public_Works_Department) | 05 March 2018 | 21 December 2023 | 22-Dec-2023 | 2867 | 2858 | [201803051515468118.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803051515468118.pdf) | [202312211715095018.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312211715095018.pdf) |
| 22 | [Revenue and Forest Department](GRs/Revenue_and_Forest_Department) | 23 March 2021 | 22 December 2023 | 22-Dec-2023 | 2771 | 2736 | [202103231328393119.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202103231328393119.pdf) | [202312221659383219.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312221659383219.pdf) |
| 23 | [Rural Development Department](GRs/Rural_Development_Department) | 31 March 2021 | 21 December 2023 | 22-Dec-2023 | 1311 | 1189 | [202103301021181120.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202103301021181120.pdf) | [202312211729410720.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312211729410720.pdf) |
| 24 | [School Education and Sports Department](GRs/School_Education_and_Sports_Department) | 15 May 2018 | 22 December 2023 | 22-Dec-2023 | 3324 | 3306 | [201805161114241221.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201805161114241221.pdf) | [202312221935228121.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312221935228121.pdf) |
| 25 | [Skill Development and Entrepreneurship Department](GRs/Skill_Development_and_Entrepreneurship_Department) | 17 March 2018 | 18 December 2023 | 22-Dec-2023 | 864 | 861 | [201803171322099003.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803171322099003.pdf) | [202312181803070903.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312181803070903.pdf) |
| 26 | [Social Justice and Special Assistance Department](GRs/Social_Justice_and_Special_Assistance_Department) | 03 December 2019 | 18 December 2023 | 22-Dec-2023 | 1160 | 1157 | [201912051107011622.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201912051107011622.pdf) | [202312191645374522.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312191645374522.pdf) |
| 27 | [Soil and Water Conservation Department](GRs/Soil_and_Water_Conservation_Department) | 16 March 2018 | 22 December 2023 | 22-Dec-2023 | 1895 | 1819 | [201803161247582426.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803161247582426.pdf) | [202312221535120326.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312221535120326.pdf) |
| 28 | [Tourism and Cultural Affairs Department](GRs/Tourism_and_Cultural_Affairs_Department) | 14 March 2018 | 22 December 2023 | 22-Dec-2023 | 883 | 874 | [201803131542054523.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803131542054523.pdf) | [202312221449589323.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312221449589323.pdf) |
| 29 | [Tribal Development Department](GRs/Tribal_Development_Department) | 14 March 2018 | 18 December 2023 | 22-Dec-2023 | 1730 | 1708 | [201803091105184924.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803091105184924.pdf) | [202312151218073224.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312151218073224.pdf) |
| 30 | [Urban Development Department](GRs/Urban_Development_Department) | 07 March 2018 | 20 December 2023 | 22-Dec-2023 | 2155 | 2150 | [201803071203178325.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803071203178325.pdf) | [202312201101297425.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312201101297425.pdf) |
| 31 | [Water Resources Department](GRs/Water_Resources_Department) | 09 March 2018 | 11 December 2023 | 22-Dec-2023 | 2403 | 2395 | [201803091034435527.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803091034435527.pdf) | [202312201717300927.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312201717300927.pdf) |
| 32 | [Water Supply and Sanitation Department](GRs/Water_Supply_and_Sanitation_Department) | 13 March 2018 | 20 December 2023 | 22-Dec-2023 | 3249 | 3205 | [201803121414108428.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803121414108428.pdf) | [202312201149051328.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312201149051328.pdf) |
| 33 | [Women and Child Development Department](GRs/Women_and_Child_Development_Department) | 17 March 2018 | 20 December 2023 | 22-Dec-2023 | 1164 | 1143 | [201803171539444330.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803171539444330.pdf) | [202312201603177030.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312201603177030.pdf) |
----------------------------------------------------------------------------------------------------

**Total Orders**: 61,022 and **Total Translated Orders**: 55,817
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











