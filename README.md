# Government Resolutions, Government of Maharashtra

This repository contains government resolutions issued by the Government of Maharashtra for the last five years, there are two files for each resolution 1) original marathi (txt file) and 2) english translation of that resolution (txt file). The original government resolutions can be found at https://gr.maharashtra.gov.in/1145/Government-Resolutions.


The English translation is obtained by processing each the pdf file of each Government Resolution through a pipeline where the following operations are performed 1) Download the file using crawler 2) OCR to handle non-standard fonts 3) paragraph detection 4) table  detection 5) translation to English. This pipeline is run in sepearate repositories check out orgpedia/mah* for each department.


## Data Details

| Num | Department Name | Start Date | Last Date | Last Crawl Date | # Marathi Orders | # Translated Orders | Starting Order | Last Order |
| --- | --------------- | ---------- | --------- | --------------- | ---------------- | ------------------- | -------------- | ---------- |
| 1 | [Agriculture, Dairy Development, Animal Husbandry and Fisheries Department](GRs/Agriculture,_Dairy_Development,_Animal_Husbandry_and_Fisheries_Department) | 16 March 2018 | 03 November 2023 | 04-Nov-2023 | 3571 | 3511 | [201803161624182101.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803161624182101.pdf) | [202311031804341001.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311031804341001.pdf) |
| 2 | [Co-operation, Textiles and Marketing Department](GRs/Co-operation,_Textiles_and_Marketing_Department) | 19 March 2018 | 03 November 2023 | 04-Nov-2023 | 2229 | 2188 | [201803191257576702.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803191257576702.pdf) | [202311031703581602.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311031703581602.pdf) |
| 3 | [Environment Department](GRs/Environment_Department) | 02 December 2017 | 26 October 2023 | 28-Oct-2023 | 326 | 317 | [201712041147216904.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201712041147216904.pdf) | [202310261551557404.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202310261551557404.pdf) |
| 4 | [Finance Department](GRs/Finance_Department) | 14 January 2021 | 03 November 2023 | 04-Nov-2023 | 590 | 583 | [202101141237329905.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202101141237329905.pdf) | [202311031741562305.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311031741562305.pdf) |
| 5 | [Food, Civil Supplies and Consumer Protection Department](GRs/Food,_Civil_Supplies_and_Consumer_Protection_Department) | 05 February 2018 | 02 November 2023 | 04-Nov-2023 | 885 | 877 | [201802121244545806.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201802121244545806.pdf) | [202311021752334606.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311021752334606.pdf) |
| 6 | [General Administration Department](GRs/General_Administration_Department) | 16 March 2018 | 03 November 2023 | 04-Nov-2023 | 3938 | 3916 | [201803161224022707.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803161224022707.pdf) | [202311032231049607.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311032231049607.pdf) |
| 7 | [Higher and Technical Education Department](GRs/Higher_and_Technical_Education_Department) | 12 October 2017 | 03 November 2023 | 04-Nov-2023 | 2296 | 2271 | [201710121514029708.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201710121514029708.pdf) | [202311031829087308.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311031829087308.pdf) |
| 8 | [Home Department](GRs/Home_Department) | 22 October 2008 | 03 November 2023 | 04-Nov-2023 | 8010 | 3465 | [20081022.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/20081022.pdf) | [202311031932265529.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311031932265529.pdf) |
| 9 | [Housing Department](GRs/Housing_Department) | 16 November 2017 | 01 November 2023 | 04-Nov-2023 | 319 | 315 | [201711161447076609.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201711161447076609.pdf) | [202311011210372409.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311011210372409.pdf) |
| 10 | [Industries, Energy and Labour Department](GRs/Industries,_Energy_and_Labour_Department) | 15 March 2018 | 03 November 2023 | 04-Nov-2023 | 1673 | 1668 | [201803151204055010.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803151204055010.pdf) | [202311031643513310.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311031643513310.pdf) |
| 11 | [Information Technology Department](GRs/Information_Technology_Department) | 20 January 2018 | 27 October 2023 | 28-Oct-2023 | 109 | 109 | [201801201843024511.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201801201843024511.pdf) | [202310271649358711.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202310271649358711.pdf) |
| 12 | [Law and Judiciary Department](GRs/Law_and_Judiciary_Department) | 17 March 2018 | 02 November 2023 | 04-Nov-2023 | 1638 | 1619 | [201803171129290212.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803171129290212.pdf) | [202311021622099712.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311021622099712.pdf) |
| 13 | [Marathi Language Department](GRs/Marathi_Language_Department) | 22 February 2018 | 13 September 2023 | 16-Sep-2023 | 295 | 293 | [201802031549154233.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201802031549154233.pdf) | [202309131600252133.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202309131600252133.pdf) |
| 14 | [Medical Education and Drugs Department](GRs/Medical_Education_and_Drugs_Department) | 12 March 2018 | 01 November 2023 | 04-Nov-2023 | 925 | 878 | [201803121137094813.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803121137094813.pdf) | [202311011757240313.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311011757240313.pdf) |
| 15 | [Minorities Development Department](GRs/Minorities_Development_Department) | 09 March 2018 | 03 November 2023 | 04-Nov-2023 | 829 | 823 | [201803091218355314.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803091218355314.pdf) | [202311031124276614.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311031124276614.pdf) |
| 16 | [Other Backward Bahujan Welfare Department](GRs/Other_Backward_Bahujan_Welfare_Department) | 07 March 2022 | 31 October 2023 | 04-Nov-2023 | 380 | 377 | [202203081752439334.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202203081752439334.pdf) | [202310311541553234.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202310311541553234.pdf) |
| 17 | [Parliamentary Affairs Department](GRs/Parliamentary_Affairs_Department) | 12 October 2017 | 12 September 2023 | 16-Sep-2023 | 104 | 104 | [201710031642378615.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201710031642378615.pdf) | [202309121658524215.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202309121658524215.pdf) |
| 18 | [Persons with Disabilities Welfare Department](GRs/Persons_with_Disabilities_Welfare_Department) | 04 January 2023 | 31 October 2023 | 04-Nov-2023 | 37 | 37 | [202301041906309635.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202301041906309635.pdf) | [202310311148111635.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202310311148111635.pdf) |
| 19 | [Planning Department](GRs/Planning_Department) | 09 March 2018 | 01 November 2023 | 04-Nov-2023 | 1341 | 1321 | [201803091441032716.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803091441032716.pdf) | [202311011659420316.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311011659420316.pdf) |
| 20 | [Public Health Department](GRs/Public_Health_Department) | 08 February 2018 | 02 November 2023 | 04-Nov-2023 | 5091 | 5053 | [201801311722275417.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201801311722275417.pdf) | [202311021615412117.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311021615412117.pdf) |
| 21 | [Public Works Department](GRs/Public_Works_Department) | 05 March 2018 | 03 November 2023 | 04-Nov-2023 | 2813 | 2804 | [201803051515468118.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803051515468118.pdf) | [202311031630589618.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311031630589618.pdf) |
| 22 | [Revenue and Forest Department](GRs/Revenue_and_Forest_Department) | 23 March 2021 | 03 November 2023 | 04-Nov-2023 | 2651 | 2614 | [202103231328393119.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202103231328393119.pdf) | [202311031833322019.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311031833322019.pdf) |
| 23 | [Rural Development Department](GRs/Rural_Development_Department) | 31 March 2021 | 01 November 2023 | 04-Nov-2023 | 1256 | 1132 | [202103301021181120.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202103301021181120.pdf) | [202311011400145920.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311011400145920.pdf) |
| 24 | [School Education and Sports Department](GRs/School_Education_and_Sports_Department) | 15 May 2018 | 03 November 2023 | 04-Nov-2023 | 3228 | 3206 | [201805161114241221.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201805161114241221.pdf) | [202311031656298221.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311031656298221.pdf) |
| 25 | [Skill Development and Entrepreneurship Department](GRs/Skill_Development_and_Entrepreneurship_Department) | 17 March 2018 | 03 November 2023 | 04-Nov-2023 | 848 | 846 | [201803171322099003.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803171322099003.pdf) | [202311031528569703.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311031528569703.pdf) |
| 26 | [Social Justice and Special Assistance Department](GRs/Social_Justice_and_Special_Assistance_Department) | 03 December 2019 | 30 October 2023 | 04-Nov-2023 | 1130 | 1126 | [201912051107011622.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201912051107011622.pdf) | [202310311417146522.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202310311417146522.pdf) |
| 27 | [Soil and Water Conservation Department](GRs/Soil_and_Water_Conservation_Department) | 16 March 2018 | 03 November 2023 | 04-Nov-2023 | 1818 | 1710 | [201803161247582426.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803161247582426.pdf) | [202311031627566826.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311031627566826.pdf) |
| 28 | [Tourism and Cultural Affairs Department](GRs/Tourism_and_Cultural_Affairs_Department) | 14 March 2018 | 03 November 2023 | 04-Nov-2023 | 808 | 798 | [201803131542054523.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803131542054523.pdf) | [202311031756357923.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311031756357923.pdf) |
| 29 | [Tribal Development Department](GRs/Tribal_Development_Department) | 14 March 2018 | 03 November 2023 | 04-Nov-2023 | 1685 | 1663 | [201803091105184924.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803091105184924.pdf) | [202311031514087924.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311031514087924.pdf) |
| 30 | [Urban Development Department](GRs/Urban_Development_Department) | 07 March 2018 | 03 November 2023 | 04-Nov-2023 | 2090 | 2085 | [201803071203178325.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803071203178325.pdf) | [202311031242106625.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311031242106625.pdf) |
| 31 | [Water Resources Department](GRs/Water_Resources_Department) | 09 March 2018 | 02 November 2023 | 04-Nov-2023 | 2374 | 2363 | [201803091034435527.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803091034435527.pdf) | [202311021527285827.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311021527285827.pdf) |
| 32 | [Water Supply and Sanitation Department](GRs/Water_Supply_and_Sanitation_Department) | 13 March 2018 | 03 November 2023 | 04-Nov-2023 | 3177 | 3132 | [201803121414108428.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803121414108428.pdf) | [202311031046220728.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311031046220728.pdf) |
| 33 | [Women and Child Development Department](GRs/Women_and_Child_Development_Department) | 17 March 2018 | 02 November 2023 | 04-Nov-2023 | 1145 | 1122 | [201803171539444330.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803171539444330.pdf) | [202311021508441430.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311021508441430.pdf) |
----------------------------------------------------------------------------------------------------

**Total Orders**: 59,609 and **Total Translated Orders**: 54,326
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











