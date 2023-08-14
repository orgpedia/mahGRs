# Government Resolutions, Government of Maharashtra

This repository contains government resolutions issued by the Government of Maharashtra for the last five years, there are two files for each resolution 1) original marathi (txt file) and 2) english translation of that resolution (txt file). The original government resolutions can be found at https://gr.maharashtra.gov.in/1145/Government-Resolutions.


The English translation is obtained by processing each the pdf file of each Government Resolution through a pipeline where the following operations are performed 1) Download the file using crawler 2) OCR to handle non-standard fonts 3) paragraph detection 4) table  detection 5) translation to English. This pipeline is run in sepearate repositories check out orgpedia/mah* for each department.


## Data Details

| Num | Department Name | Start Date | Starting Order | Last Date | Last Order | Last Crawl Date | # Marathi Orders | # Translated Orders |
| --- | --------------- | ---------- | -------------- | --------- | ---------- | --------------- | ---------------- | ------------------- |
| 1 | [Agriculture, Dairy Development, Animal Husbandry and Fisheries Department](GRs/Agriculture,_Dairy_Development,_Animal_Husbandry_and_Fisheries_Department) | 16 March 2018 | [201803161624182101.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803161624182101.pdf) | 11 August 2023 | [202308111816131401.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308111816131401.pdf) | 12-Aug-2023 | 3419 | 3360 |
| 2 | [Co-operation, Textiles and Marketing Department](GRs/Co-operation,_Textiles_and_Marketing_Department) | 19 March 2018 | [201803191257576702.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803191257576702.pdf) | 08 August 2023 | [202308081634026602.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308081634026602.pdf) | 12-Aug-2023 | 2139 | 2101 |
| 3 | [Environment Department](GRs/Environment_Department) | 02 December 2017 | [201712041147216904.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201712041147216904.pdf) | 09 August 2023 | [202308091733165604.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308091733165604.pdf) | 12-Aug-2023 | 301 | 294 |
| 4 | [Finance Department](GRs/Finance_Department) | 14 January 2021 | [202101141237329905.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202101141237329905.pdf) | 09 August 2023 | [202308091443085805.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308091443085805.pdf) | 12-Aug-2023 | 538 | 533 |
| 5 | [Food, Civil Supplies and Consumer Protection Department](GRs/Food,_Civil_Supplies_and_Consumer_Protection_Department) | 05 February 2018 | [201802121244545806.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201802121244545806.pdf) | 10 August 2023 | [202308101808242706.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308101808242706.pdf) | 12-Aug-2023 | 860 | 852 |
| 6 | [General Administration Department](GRs/General_Administration_Department) | 16 March 2018 | [201803161224022707.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803161224022707.pdf) | 11 August 2023 | [202308111815194807.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308111815194807.pdf) | 12-Aug-2023 | 3778 | 3759 |
| 7 | [Higher and Technical Education Department](GRs/Higher_and_Technical_Education_Department) | 12 October 2017 | [201710121514029708.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201710121514029708.pdf) | 11 August 2023 | [202308111159333508.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308111159333508.pdf) | 12-Aug-2023 | 2188 | 2166 |
| 8 | [Home Department](GRs/Home_Department) | 22 October 2008 | [20081022.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/20081022.pdf) | 11 August 2023 | [202308111843286229.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308111843286229.pdf) | 12-Aug-2023 | 7829 | 3285 |
| 9 | [Housing Department](GRs/Housing_Department) | 16 November 2017 | [201711161447076609.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201711161447076609.pdf) | 02 August 2023 | [202308021928282409.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308021928282409.pdf) | 05-Aug-2023 | 305 | 301 |
| 10 | [Industries, Energy and Labour Department](GRs/Industries,_Energy_and_Labour_Department) | 15 March 2018 | [201803151204055010.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803151204055010.pdf) | 07 August 2023 | [202308071453439810.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308071453439810.pdf) | 12-Aug-2023 | 1602 | 1597 |
| 11 | [Information Technology Department](GRs/Information_Technology_Department) | 20 January 2018 | [201801201843024511.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201801201843024511.pdf) | 24 April 2023 | [202304241816282211.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202304241816282211.pdf) | 28-May-2023 | 107 | 107 |
| 12 | [Law and Judiciary Department](GRs/Law_and_Judiciary_Department) | 17 March 2018 | [201803171129290212.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803171129290212.pdf) | 11 August 2023 | [202308111455358812.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308111455358812.pdf) | 13-Aug-2023 | 1531 | 1516 |
| 13 | [Marathi Language Department](GRs/Marathi_Language_Department) | 22 February 2018 | [201802031549154233.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201802031549154233.pdf) | 21 July 2023 | [202307211300189433.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202307211300189433.pdf) | 21-Jul-2023 | 290 | 288 |
| 14 | [Medical Education and Drugs Department](GRs/Medical_Education_and_Drugs_Department) | 12 March 2018 | [201803121137094813.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803121137094813.pdf) | 10 August 2023 | [202308101745491413.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308101745491413.pdf) | 13-Aug-2023 | 885 | 841 |
| 15 | [Minorities Development Department](GRs/Minorities_Development_Department) | 09 March 2018 | [201803091218355314.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803091218355314.pdf) | 04 August 2023 | [202308041421111614.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308041421111614.pdf) | 05-Aug-2023 | 805 | 801 |
| 16 | [Other Backward Bahujan Welfare Department](GRs/Other_Backward_Bahujan_Welfare_Department) | 07 March 2022 | [202203081752439334.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202203081752439334.pdf) | 11 August 2023 | [202308111416490934.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308111416490934.pdf) | 13-Aug-2023 | 290 | 289 |
| 17 | [Parliamentary Affairs Department](GRs/Parliamentary_Affairs_Department) | 12 October 2017 | [201710031642378615.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201710031642378615.pdf) | 07 July 2023 | [202307071223304115.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202307071223304115.pdf) | 09-Jul-2023 | 101 | 101 |
| 18 | [Persons with Disabilities Welfare Department](GRs/Persons_with_Disabilities_Welfare_Department) | 04 January 2023 | [202301041906309635.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202301041906309635.pdf) | 31 July 2023 | [202307311337570435.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202307311337570435.pdf) | 05-Aug-2023 | 21 | 21 |
| 19 | [Planning Department](GRs/Planning_Department) | 09 March 2018 | [201803091441032716.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803091441032716.pdf) | 09 August 2023 | [202308111719326516.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308111719326516.pdf) | 13-Aug-2023 | 1291 | 1272 |
| 20 | [Public Health Department](GRs/Public_Health_Department) | 08 February 2018 | [201801311722275417.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201801311722275417.pdf) | 10 August 2023 | [202308091658356917.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308091658356917.pdf) | 13-Aug-2023 | 4864 | 4827 |
| 21 | [Public Works Department](GRs/Public_Works_Department) | 05 March 2018 | [201803051515468118.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803051515468118.pdf) | 11 August 2023 | [202308111437341818.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308111437341818.pdf) | 13-Aug-2023 | 2743 | 2734 |
| 22 | [Revenue and Forest Department](GRs/Revenue_and_Forest_Department) | 23 March 2021 | [202103231328393119.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202103231328393119.pdf) | 11 August 2023 | [202308111548553219.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308111548553219.pdf) | 13-Aug-2023 | 2302 | 2277 |
| 23 | [Rural Development Department](GRs/Rural_Development_Department) | 31 March 2021 | [202103301021181120.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202103301021181120.pdf) | 11 August 2023 | [202308111214039420.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308111214039420.pdf) | 13-Aug-2023 | 1137 | 1021 |
| 24 | [School Education and Sports Department](GRs/School_Education_and_Sports_Department) | 15 May 2018 | [201805161114241221.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201805161114241221.pdf) | 11 August 2023 | [202308111846084621.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308111846084621.pdf) | 13-Aug-2023 | 3056 | 3038 |
| 25 | [Skill Development and Entrepreneurship Department](GRs/Skill_Development_and_Entrepreneurship_Department) | 17 March 2018 | [201803171322099003.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803171322099003.pdf) | 01 August 2023 | [202308011616406403.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308011616406403.pdf) | 05-Aug-2023 | 802 | 800 |
| 26 | [Social Justice and Special Assistance Department](GRs/Social_Justice_and_Special_Assistance_Department) | 03 December 2019 | [201912051107011622.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201912051107011622.pdf) | 10 August 2023 | [202308111110536422.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308111110536422.pdf) | 13-Aug-2023 | 1072 | 1069 |
| 27 | [Soil and Water Conservation Department](GRs/Soil_and_Water_Conservation_Department) | 16 March 2018 | [201803161247582426.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803161247582426.pdf) | 10 August 2023 | [202308101800551926.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308101800551926.pdf) | 13-Aug-2023 | 1684 | 1609 |
| 28 | [Tourism and Cultural Affairs Department](GRs/Tourism_and_Cultural_Affairs_Department) | 14 March 2018 | [201803131542054523.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803131542054523.pdf) | 10 August 2023 | [202308101705364423.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308101705364423.pdf) | 13-Aug-2023 | 718 | 711 |
| 29 | [Tribal Development Department](GRs/Tribal_Development_Department) | 14 March 2018 | [201803091105184924.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803091105184924.pdf) | 04 August 2023 | [202308041848562824.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308041848562824.pdf) | 13-Aug-2023 | 1609 | 1589 |
| 30 | [Urban Development Department](GRs/Urban_Development_Department) | 07 March 2018 | [201803071203178325.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803071203178325.pdf) | 11 August 2023 | [202308111039445525.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308111039445525.pdf) | 13-Aug-2023 | 1977 | 1973 |
| 31 | [Water Resources Department](GRs/Water_Resources_Department) | 09 March 2018 | [201803091034435527.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803091034435527.pdf) | 11 August 2023 | [202308111456216527.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308111456216527.pdf) | 13-Aug-2023 | 2222 | 2214 |
| 32 | [Water Supply and Sanitation Department](GRs/Water_Supply_and_Sanitation_Department) | 13 March 2018 | [201803121414108428.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803121414108428.pdf) | 10 August 2023 | [202308101212041828.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308101212041828.pdf) | 13-Aug-2023 | 3101 | 3069 |
| 33 | [Women and Child Development Department](GRs/Women_and_Child_Development_Department) | 17 March 2018 | [201803171539444330.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803171539444330.pdf) | 09 August 2023 | [202308091415057730.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202308091415057730.pdf) | 13-Aug-2023 | 1082 | 1062 |
----------------------------------------------------------------------------------------------------

**Total Orders**: 56,649 and **Total Translated Orders**: 51,477
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











