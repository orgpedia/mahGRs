# Government Resolutions, Government of Maharashtra

This repository contains government resolutions issued by the Government of Maharashtra for the last five years, there are two files for each resolution 1) original marathi (txt file) and 2) english translation of that resolution (txt file). The original government resolutions can be found at https://gr.maharashtra.gov.in/1145/Government-Resolutions.


The English translation is obtained by processing each the pdf file of each Government Resolution through a pipeline where the following operations are performed 1) Download the file using crawler 2) OCR to handle non-standard fonts 3) paragraph detection 4) table  detection 5) translation to English. This pipeline is run in sepearate repositories check out orgpedia/mah* for each department.


## Data Details

| Num | Department Name | Start Date | Starting Order | Last Date | Last Order | Last Crawl Date | # Marathi Orders | # Translated Orders |
| --- | --------------- | ---------- | -------------- | --------- | ---------- | --------------- | ---------------- | ------------------- |
| 1 | [Agriculture, Dairy Development, Animal Husbandry and Fisheries Department](GRs/Agriculture,_Dairy_Development,_Animal_Husbandry_and_Fisheries_Department) | 16 March 2018 | [201803161624182101.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803161624182101.pdf) | 07 July 2023 | [202307071845011901.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202307071845011901.pdf) | 09-Jul-2023 | 3336 | 3277 |
| 2 | [Co-operation, Textiles and Marketing Department](GRs/Co-operation,_Textiles_and_Marketing_Department) | 19 March 2018 | [201803191257576702.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803191257576702.pdf) | 07 July 2023 | [202307071854430202.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202307071854430202.pdf) | 09-Jul-2023 | 2109 | 2073 |
| 3 | [Environment Department](GRs/Environment_Department) | 02 December 2017 | [201712041147216904.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201712041147216904.pdf) | 22 June 2023 | [202306231312376804.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202306231312376804.pdf) | 24-Jun-2023 | 298 | 291 |
| 4 | [Finance Department](GRs/Finance_Department) | 14 January 2021 | [202101141237329905.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202101141237329905.pdf) | 06 July 2023 | [202307061531202605.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202307061531202605.pdf) | 09-Jul-2023 | 519 | 514 |
| 5 | [Food, Civil Supplies and Consumer Protection Department](GRs/Food,_Civil_Supplies_and_Consumer_Protection_Department) | 05 February 2018 | [201802121244545806.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201802121244545806.pdf) | 04 July 2023 | [202307041439454006.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202307041439454006.pdf) | 09-Jul-2023 | 852 | 844 |
| 6 | [General Administration Department](GRs/General_Administration_Department) | 16 March 2018 | [201803161224022707.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803161224022707.pdf) | 07 July 2023 | [202307071829020307.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202307071829020307.pdf) | 09-Jul-2023 | 3685 | 3667 |
| 7 | [Higher and Technical Education Department](GRs/Higher_and_Technical_Education_Department) | 12 October 2017 | [201710121514029708.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201710121514029708.pdf) | 07 July 2023 | [202307071837022908.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202307071837022908.pdf) | 09-Jul-2023 | 2127 | 2122 |
| 8 | [Home Department](GRs/Home_Department) | 22 October 2008 | [20081022.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/20081022.pdf) | 07 July 2023 | [202307071826140729.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202307071826140729.pdf) | 09-Jul-2023 | 7766 | 3222 |
| 9 | [Housing Department](GRs/Housing_Department) | 16 November 2017 | [201711161447076609.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201711161447076609.pdf) | 25 May 2023 | [202305251320009509.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202305251320009509.pdf) | 28-May-2023 | 298 | 294 |
| 10 | [Industries, Energy and Labour Department](GRs/Industries,_Energy_and_Labour_Department) | 15 March 2018 | [201803151204055010.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803151204055010.pdf) | 07 July 2023 | [202307071711269810.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202307071711269810.pdf) | 09-Jul-2023 | 1584 | 1580 |
| 11 | [Information Technology Department](GRs/Information_Technology_Department) | 20 January 2018 | [201801201843024511.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201801201843024511.pdf) | 24 April 2023 | [202304241816282211.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202304241816282211.pdf) | 28-May-2023 | 107 | 107 |
| 12 | [Law and Judiciary Department](GRs/Law_and_Judiciary_Department) | 17 March 2018 | [201803171129290212.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803171129290212.pdf) | 23 June 2023 | [202306231515213912.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202306231515213912.pdf) | 24-Jun-2023 | 1485 | 42 |
| 13 | [Marathi Language Department](GRs/Marathi_Language_Department) | 22 February 2018 | [201802031549154233.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201802031549154233.pdf) | 06 July 2023 | [202307061213519033.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202307061213519033.pdf) | 09-Jul-2023 | 286 | 284 |
| 14 | [Medical Education and Drugs Department](GRs/Medical_Education_and_Drugs_Department) | 12 March 2018 | [201803121137094813.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803121137094813.pdf) | 07 July 2023 | [202307071128258313.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202307071128258313.pdf) | 09-Jul-2023 | 859 | 815 |
| 15 | [Minorities Development Department](GRs/Minorities_Development_Department) | 09 March 2018 | [201803091218355314.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803091218355314.pdf) | 04 July 2023 | [202307041543324914.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202307041543324914.pdf) | 09-Jul-2023 | 798 | 794 |
| 16 | [Other Backward Bahujan Welfare Department](GRs/Other_Backward_Bahujan_Welfare_Department) | 07 March 2022 | [202203081752439334.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202203081752439334.pdf) | 05 July 2023 | [202307061616436734.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202307061616436734.pdf) | 09-Jul-2023 | 217 | 216 |
| 17 | [Parliamentary Affairs Department](GRs/Parliamentary_Affairs_Department) | 12 October 2017 | [201710031642378615.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201710031642378615.pdf) | 07 July 2023 | [202307071223304115.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202307071223304115.pdf) | 09-Jul-2023 | 101 | 101 |
| 18 | [Persons with Disabilities Welfare Department](GRs/Persons_with_Disabilities_Welfare_Department) | 04 January 2023 | [202301041906309635.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202301041906309635.pdf) | 16 June 2023 | [202306161702465035.pdf](https://gr.maharashtra.gov.in/ps://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202306161702465035.pdf) | 17-Jun-2023 | 16 | 0 |
| 19 | [Planning Department](GRs/Planning_Department) | 09 March 2018 | [201803091441032716.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803091441032716.pdf) | 05 July 2023 | [202307051210502616.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202307051210502616.pdf) | 09-Jul-2023 | 1266 | 1247 |
| 20 | [Public Health Department](GRs/Public_Health_Department) | 08 February 2018 | [201801311722275417.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201801311722275417.pdf) | 05 July 2023 | [202307051937526817.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202307051937526817.pdf) | 09-Jul-2023 | 4771 | 4735 |
| 21 | [Public Works Department](GRs/Public_Works_Department) | 05 March 2018 | [201803051515468118.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803051515468118.pdf) | 07 July 2023 | [202307071651257518.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202307071651257518.pdf) | 09-Jul-2023 | 2718 | 2709 |
| 22 | [Revenue and Forest Department](GRs/Revenue_and_Forest_Department) | 23 March 2021 | [202103231328393119.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202103231328393119.pdf) | 07 July 2023 | [202307071127559119.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202307071127559119.pdf) | 09-Jul-2023 | 2171 | 2148 |
| 23 | [Rural Development Department](GRs/Rural_Development_Department) | 31 March 2021 | [202103301021181120.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202103301021181120.pdf) | 05 July 2023 | [202307071752344820.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202307071752344820.pdf) | 09-Jul-2023 | 1076 | 962 |
| 24 | [School Education and Sports Department](GRs/School_Education_and_Sports_Department) | 15 May 2018 | [201805161114241221.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201805161114241221.pdf) | 07 July 2023 | [202307071848111621.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202307071848111621.pdf) | 09-Jul-2023 | 2983 | 2965 |
| 25 | [Skill Development and Entrepreneurship Department](GRs/Skill_Development_and_Entrepreneurship_Department) | 17 March 2018 | [201803171322099003.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803171322099003.pdf) | 04 July 2023 | [202307041154237403.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202307041154237403.pdf) | 09-Jul-2023 | 788 | 786 |
| 26 | [Social Justice and Special Assistance Department](GRs/Social_Justice_and_Special_Assistance_Department) | 03 December 2019 | [201912051107011622.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201912051107011622.pdf) | 07 July 2023 | [202307071717166722.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202307071717166722.pdf) | 09-Jul-2023 | 1041 | 1038 |
| 27 | [Soil and Water Conservation Department](GRs/Soil_and_Water_Conservation_Department) | 16 March 2018 | [201803161247582426.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803161247582426.pdf) | 07 July 2023 | [202307071647577526.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202307071647577526.pdf) | 09-Jul-2023 | 1655 | 1580 |
| 28 | [Tourism and Cultural Affairs Department](GRs/Tourism_and_Cultural_Affairs_Department) | 14 March 2018 | [201803131542054523.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803131542054523.pdf) | 05 July 2023 | [202307061257344023.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202307061257344023.pdf) | 09-Jul-2023 | 684 | 677 |
| 29 | [Tribal Development Department](GRs/Tribal_Development_Department) | 14 March 2018 | [201803091105184924.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803091105184924.pdf) | 05 July 2023 | [202307051538177224.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202307051538177224.pdf) | 09-Jul-2023 | 1571 | 1551 |
| 30 | [Urban Development Department](GRs/Urban_Development_Department) | 07 March 2018 | [201803071203178325.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803071203178325.pdf) | 06 July 2023 | [202307061841329825.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202307061841329825.pdf) | 09-Jul-2023 | 1941 | 1937 |
| 31 | [Water Resources Department](GRs/Water_Resources_Department) | 09 March 2018 | [201803091034435527.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803091034435527.pdf) | 05 July 2023 | [202307051923177527.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202307051923177527.pdf) | 09-Jul-2023 | 2190 | 2182 |
| 32 | [Water Supply and Sanitation Department](GRs/Water_Supply_and_Sanitation_Department) | 13 March 2018 | [201803121414108428.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803121414108428.pdf) | 06 July 2023 | [202307061432045628.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202307061432045628.pdf) | 09-Jul-2023 | 3043 | 3015 |
| 33 | [Women and Child Development Department](GRs/Women_and_Child_Development_Department) | 17 March 2018 | [201803171539444330.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803171539444330.pdf) | 07 July 2023 | [202307071819524430.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202307071819524430.pdf) | 09-Jul-2023 | 1065 | 1046 |
----------------------------------------------------------------------------------------------------

**Total Orders**: 55,406 and **Total Translated Orders**: 48,821
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









