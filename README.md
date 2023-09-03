# Government Resolutions, Government of Maharashtra

This repository contains government resolutions issued by the Government of Maharashtra for the last five years, there are two files for each resolution 1) original marathi (txt file) and 2) english translation of that resolution (txt file). The original government resolutions can be found at https://gr.maharashtra.gov.in/1145/Government-Resolutions.


The English translation is obtained by processing each the pdf file of each Government Resolution through a pipeline where the following operations are performed 1) Download the file using crawler 2) OCR to handle non-standard fonts 3) paragraph detection 4) table  detection 5) translation to English. This pipeline is run in sepearate repositories check out orgpedia/mah* for each department.


## Data Details

| Num | Department Name | Start Date | Last Date | Last Crawl Date | # Marathi Orders | # Translated Orders | Starting Order | Last Order |
| --- | --------------- | ---------- | --------- | --------------- | ---------------- | ------------------- | -------------- | ---------- |
| 1 | [Agriculture, Dairy Development, Animal Husbandry and Fisheries Department](GRs/Agriculture,_Dairy_Development,_Animal_Husbandry_and_Fisheries_Department) | 16 March 2018 | 01 September 2023 | 02-Sep-2023 | 3446 | 3386 | [201803161624182101.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803161624182101.pdf) | [202309011601484001.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202309011601484001.pdf) |
| 2 | [Co-operation, Textiles and Marketing Department](GRs/Co-operation,_Textiles_and_Marketing_Department) | 19 March 2018 | 01 September 2023 | 02-Sep-2023 | 2161 | 2122 | [201803191257576702.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803191257576702.pdf) | [202309011526027502.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202309011526027502.pdf) |
| 3 | [Environment Department](GRs/Environment_Department) | 02 December 2017 | 25 August 2023 | 25-Aug-2023 | 303 | 296 | [201712041147216904.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201712041147216904.pdf) | [202308251542131904.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308251542131904.pdf) |
| 4 | [Finance Department](GRs/Finance_Department) | 14 January 2021 | 31 August 2023 | 02-Sep-2023 | 552 | 546 | [202101141237329905.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202101141237329905.pdf) | [202308311538144305.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308311538144305.pdf) |
| 5 | [Food, Civil Supplies and Consumer Protection Department](GRs/Food,_Civil_Supplies_and_Consumer_Protection_Department) | 05 February 2018 | 30 August 2023 | 02-Sep-2023 | 864 | 856 | [201802121244545806.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201802121244545806.pdf) | [202308301449051706.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308301449051706.pdf) |
| 6 | [General Administration Department](GRs/General_Administration_Department) | 16 March 2018 | 01 September 2023 | 02-Sep-2023 | 3817 | 3798 | [201803161224022707.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803161224022707.pdf) | [202309011756530207.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202309011756530207.pdf) |
| 7 | [Higher and Technical Education Department](GRs/Higher_and_Technical_Education_Department) | 12 October 2017 | 01 September 2023 | 02-Sep-2023 | 2222 | 2200 | [201710121514029708.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201710121514029708.pdf) | [202309011619152008.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202309011619152008.pdf) |
| 8 | [Home Department](GRs/Home_Department) | 22 October 2008 | 31 August 2023 | 02-Sep-2023 | 7864 | 3320 | [20081022.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/20081022.pdf) | [202308311215369329.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308311215369329.pdf) |
| 9 | [Housing Department](GRs/Housing_Department) | 16 November 2017 | 29 August 2023 | 02-Sep-2023 | 310 | 306 | [201711161447076609.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201711161447076609.pdf) | [202308291802019809.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308291802019809.pdf) |
| 10 | [Industries, Energy and Labour Department](GRs/Industries,_Energy_and_Labour_Department) | 15 March 2018 | 01 September 2023 | 02-Sep-2023 | 1612 | 1607 | [201803151204055010.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803151204055010.pdf) | [202309011551201010.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202309011551201010.pdf) |
| 11 | [Information Technology Department](GRs/Information_Technology_Department) | 20 January 2018 | 24 April 2023 | 28-May-2023 | 107 | 107 | [201801201843024511.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201801201843024511.pdf) | [202304241816282211.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202304241816282211.pdf) |
| 12 | [Law and Judiciary Department](GRs/Law_and_Judiciary_Department) | 17 March 2018 | 01 September 2023 | 02-Sep-2023 | 1549 | 1534 | [201803171129290212.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803171129290212.pdf) | [202309011654311512.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202309011654311512.pdf) |
| 13 | [Marathi Language Department](GRs/Marathi_Language_Department) | 22 February 2018 | 29 August 2023 | 02-Sep-2023 | 291 | 289 | [201802031549154233.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201802031549154233.pdf) | [202308291250461333.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308291250461333.pdf) |
| 14 | [Medical Education and Drugs Department](GRs/Medical_Education_and_Drugs_Department) | 12 March 2018 | 24 August 2023 | 02-Sep-2023 | 896 | 852 | [201803121137094813.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803121137094813.pdf) | [202308241751012413.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308241751012413.pdf) |
| 15 | [Minorities Development Department](GRs/Minorities_Development_Department) | 09 March 2018 | 29 August 2023 | 02-Sep-2023 | 807 | 803 | [201803091218355314.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803091218355314.pdf) | [202308291249234014.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308291249234014.pdf) |
| 16 | [Other Backward Bahujan Welfare Department](GRs/Other_Backward_Bahujan_Welfare_Department) | 07 March 2022 | 01 September 2023 | 02-Sep-2023 | 339 | 337 | [202203081752439334.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202203081752439334.pdf) | [202309011205218734.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202309011205218734.pdf) |
| 17 | [Parliamentary Affairs Department](GRs/Parliamentary_Affairs_Department) | 12 October 2017 | 22 August 2023 | 26-Aug-2023 | 102 | 102 | [201710031642378615.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201710031642378615.pdf) | [202308221748576515.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308221748576515.pdf) |
| 18 | [Persons with Disabilities Welfare Department](GRs/Persons_with_Disabilities_Welfare_Department) | 04 January 2023 | 01 September 2023 | 02-Sep-2023 | 24 | 24 | [202301041906309635.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202301041906309635.pdf) | [202309011752106535.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202309011752106535.pdf) |
| 19 | [Planning Department](GRs/Planning_Department) | 09 March 2018 | 01 September 2023 | 02-Sep-2023 | 1305 | 1285 | [201803091441032716.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803091441032716.pdf) | [202309011720490216.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202309011720490216.pdf) |
| 20 | [Public Health Department](GRs/Public_Health_Department) | 08 February 2018 | 31 August 2023 | 02-Sep-2023 | 4945 | 4908 | [201801311722275417.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201801311722275417.pdf) | [202308311752047117.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308311752047117.pdf) |
| 21 | [Public Works Department](GRs/Public_Works_Department) | 05 March 2018 | 30 August 2023 | 02-Sep-2023 | 2751 | 2742 | [201803051515468118.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803051515468118.pdf) | [202308311649070418.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308311649070418.pdf) |
| 22 | [Revenue and Forest Department](GRs/Revenue_and_Forest_Department) | 23 March 2021 | 01 September 2023 | 02-Sep-2023 | 2350 | 2325 | [202103231328393119.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202103231328393119.pdf) | [202309011806495219.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202309011806495219.pdf) |
| 23 | [Rural Development Department](GRs/Rural_Development_Department) | 31 March 2021 | 31 August 2023 | 02-Sep-2023 | 1146 | 1028 | [202103301021181120.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202103301021181120.pdf) | [202308311458557020.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308311458557020.pdf) |
| 24 | [School Education and Sports Department](GRs/School_Education_and_Sports_Department) | 15 May 2018 | 01 September 2023 | 02-Sep-2023 | 3092 | 3074 | [201805161114241221.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201805161114241221.pdf) | [202309011807078021.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202309011807078021.pdf) |
| 25 | [Skill Development and Entrepreneurship Department](GRs/Skill_Development_and_Entrepreneurship_Department) | 17 March 2018 | 25 August 2023 | 26-Aug-2023 | 811 | 809 | [201803171322099003.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803171322099003.pdf) | [202308251542010403.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308251542010403.pdf) |
| 26 | [Social Justice and Special Assistance Department](GRs/Social_Justice_and_Special_Assistance_Department) | 03 December 2019 | 30 August 2023 | 02-Sep-2023 | 1082 | 1079 | [201912051107011622.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201912051107011622.pdf) | [202308301828260922.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308301828260922.pdf) |
| 27 | [Soil and Water Conservation Department](GRs/Soil_and_Water_Conservation_Department) | 16 March 2018 | 01 September 2023 | 02-Sep-2023 | 1712 | 1636 | [201803161247582426.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803161247582426.pdf) | [202309011802287526.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202309011802287526.pdf) |
| 28 | [Tourism and Cultural Affairs Department](GRs/Tourism_and_Cultural_Affairs_Department) | 14 March 2018 | 30 August 2023 | 02-Sep-2023 | 741 | 734 | [201803131542054523.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803131542054523.pdf) | [202308301758372223.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308301758372223.pdf) |
| 29 | [Tribal Development Department](GRs/Tribal_Development_Department) | 14 March 2018 | 31 August 2023 | 02-Sep-2023 | 1637 | 1617 | [201803091105184924.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803091105184924.pdf) | [202308311700314824.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308311700314824.pdf) |
| 30 | [Urban Development Department](GRs/Urban_Development_Department) | 07 March 2018 | 01 September 2023 | 02-Sep-2023 | 2007 | 2003 | [201803071203178325.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803071203178325.pdf) | [202309011542126125.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202309011542126125.pdf) |
| 31 | [Water Resources Department](GRs/Water_Resources_Department) | 09 March 2018 | 01 September 2023 | 02-Sep-2023 | 2237 | 2229 | [201803091034435527.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803091034435527.pdf) | [202309011521344027.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202309011521344027.pdf) |
| 32 | [Water Supply and Sanitation Department](GRs/Water_Supply_and_Sanitation_Department) | 13 March 2018 | 31 August 2023 | 02-Sep-2023 | 3130 | 3098 | [201803121414108428.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803121414108428.pdf) | [202308311708319228.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308311708319228.pdf) |
| 33 | [Women and Child Development Department](GRs/Women_and_Child_Development_Department) | 17 March 2018 | 31 August 2023 | 02-Sep-2023 | 1092 | 1072 | [201803171539444330.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803171539444330.pdf) | [202308311804226630.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308311804226630.pdf) |
----------------------------------------------------------------------------------------------------

**Total Orders**: 57,304 and **Total Translated Orders**: 52,124
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











