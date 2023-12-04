# Government Resolutions, Government of Maharashtra

This repository contains government resolutions issued by the Government of Maharashtra for the last five years, there are two files for each resolution 1) original marathi (txt file) and 2) english translation of that resolution (txt file). The original government resolutions can be found at https://gr.maharashtra.gov.in/1145/Government-Resolutions.


The English translation is obtained by processing each the pdf file of each Government Resolution through a pipeline where the following operations are performed 1) Download the file using crawler 2) OCR to handle non-standard fonts 3) paragraph detection 4) table  detection 5) translation to English. This pipeline is run in sepearate repositories check out orgpedia/mah* for each department.


## Data Details

| Num | Department Name | Start Date | Last Date | Last Crawl Date | # Marathi Orders | # Translated Orders | Starting Order | Last Order |
| --- | --------------- | ---------- | --------- | --------------- | ---------------- | ------------------- | -------------- | ---------- |
| 1 | [Agriculture, Dairy Development, Animal Husbandry and Fisheries Department](GRs/Agriculture,_Dairy_Development,_Animal_Husbandry_and_Fisheries_Department) | 16 March 2018 | 01 December 2023 | 03-Dec-2023 | 3604 | 3541 | [201803161624182101.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803161624182101.pdf) | [202312011523471401.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312011523471401.pdf) |
| 2 | [Co-operation, Textiles and Marketing Department](GRs/Co-operation,_Textiles_and_Marketing_Department) | 19 March 2018 | 01 December 2023 | 03-Dec-2023 | 2257 | 2208 | [201803191257576702.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803191257576702.pdf) | [202312011532153802.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312011532153802.pdf) |
| 3 | [Environment Department](GRs/Environment_Department) | 02 December 2017 | 09 November 2023 | 26-Nov-2023 | 336 | 318 | [201712041147216904.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201712041147216904.pdf) | [202311091716582504.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311091716582504.pdf) |
| 4 | [Finance Department](GRs/Finance_Department) | 14 January 2021 | 01 December 2023 | 03-Dec-2023 | 610 | 599 | [202101141237329905.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202101141237329905.pdf) | [202312011538196605.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312011538196605.pdf) |
| 5 | [Food, Civil Supplies and Consumer Protection Department](GRs/Food,_Civil_Supplies_and_Consumer_Protection_Department) | 05 February 2018 | 01 December 2023 | 03-Dec-2023 | 892 | 883 | [201802121244545806.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201802121244545806.pdf) | [202312011812070006.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312011812070006.pdf) |
| 6 | [General Administration Department](GRs/General_Administration_Department) | 16 March 2018 | 01 December 2023 | 03-Dec-2023 | 3982 | 3953 | [201803161224022707.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803161224022707.pdf) | [202312011654164407.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312011654164407.pdf) |
| 7 | [Higher and Technical Education Department](GRs/Higher_and_Technical_Education_Department) | 12 October 2017 | 01 December 2023 | 03-Dec-2023 | 2318 | 2313 | [201710121514029708.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201710121514029708.pdf) | [202312011732255608.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312011732255608.pdf) |
| 8 | [Home Department](GRs/Home_Department) | 22 October 2008 | 01 December 2023 | 03-Dec-2023 | 8057 | 3509 | [20081022.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/20081022.pdf) | [202312011454506629.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312011454506629.pdf) |
| 9 | [Housing Department](GRs/Housing_Department) | 16 November 2017 | 22 November 2023 | 26-Nov-2023 | 322 | 318 | [201711161447076609.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201711161447076609.pdf) | [202311221219205209.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311221219205209.pdf) |
| 10 | [Industries, Energy and Labour Department](GRs/Industries,_Energy_and_Labour_Department) | 15 March 2018 | 30 November 2023 | 03-Dec-2023 | 1695 | 1685 | [201803151204055010.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803151204055010.pdf) | [202311301457248810.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311301457248810.pdf) |
| 11 | [Information Technology Department](GRs/Information_Technology_Department) | 20 January 2018 | 27 October 2023 | 28-Oct-2023 | 109 | 109 | [201801201843024511.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201801201843024511.pdf) | [202310271649358711.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202310271649358711.pdf) |
| 12 | [Law and Judiciary Department](GRs/Law_and_Judiciary_Department) | 17 March 2018 | 01 December 2023 | 03-Dec-2023 | 1652 | 1628 | [201803171129290212.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803171129290212.pdf) | [202312011700089912.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312011700089912.pdf) |
| 13 | [Marathi Language Department](GRs/Marathi_Language_Department) | 22 February 2018 | 28 November 2023 | 03-Dec-2023 | 300 | 297 | [201802031549154233.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201802031549154233.pdf) | [202311281219182333.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311281219182333.pdf) |
| 14 | [Medical Education and Drugs Department](GRs/Medical_Education_and_Drugs_Department) | 12 March 2018 | 30 November 2023 | 03-Dec-2023 | 947 | 898 | [201803121137094813.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803121137094813.pdf) | [202311301518273313.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311301518273313.pdf) |
| 15 | [Minorities Development Department](GRs/Minorities_Development_Department) | 09 March 2018 | 29 November 2023 | 03-Dec-2023 | 842 | 835 | [201803091218355314.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803091218355314.pdf) | [202311291709338614.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311291709338614.pdf) |
| 16 | [Other Backward Bahujan Welfare Department](GRs/Other_Backward_Bahujan_Welfare_Department) | 07 March 2022 | 30 November 2023 | 03-Dec-2023 | 410 | 403 | [202203081752439334.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202203081752439334.pdf) | [202311301740195334.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311301740195334.pdf) |
| 17 | [Parliamentary Affairs Department](GRs/Parliamentary_Affairs_Department) | 12 October 2017 | 22 November 2023 | 26-Nov-2023 | 105 | 104 | [201710031642378615.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201710031642378615.pdf) | [202311221247565415.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311221247565415.pdf) |
| 18 | [Persons with Disabilities Welfare Department](GRs/Persons_with_Disabilities_Welfare_Department) | 04 January 2023 | 28 November 2023 | 03-Dec-2023 | 42 | 40 | [202301041906309635.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202301041906309635.pdf) | [202311281605117035.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311281605117035.pdf) |
| 19 | [Planning Department](GRs/Planning_Department) | 09 March 2018 | 01 December 2023 | 03-Dec-2023 | 1362 | 1334 | [201803091441032716.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803091441032716.pdf) | [202312011706342316.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312011706342316.pdf) |
| 20 | [Public Health Department](GRs/Public_Health_Department) | 08 February 2018 | 01 December 2023 | 03-Dec-2023 | 5170 | 5124 | [201801311722275417.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201801311722275417.pdf) | [202312011646149417.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312011646149417.pdf) |
| 21 | [Public Works Department](GRs/Public_Works_Department) | 05 March 2018 | 01 December 2023 | 03-Dec-2023 | 2845 | 2829 | [201803051515468118.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803051515468118.pdf) | [202312011520091118.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312011520091118.pdf) |
| 22 | [Revenue and Forest Department](GRs/Revenue_and_Forest_Department) | 23 March 2021 | 01 December 2023 | 03-Dec-2023 | 2737 | 2685 | [202103231328393119.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202103231328393119.pdf) | [202312011701344719.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312011701344719.pdf) |
| 23 | [Rural Development Department](GRs/Rural_Development_Department) | 31 March 2021 | 01 December 2023 | 03-Dec-2023 | 1294 | 1163 | [202103301021181120.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202103301021181120.pdf) | [202312011421179720.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312011421179720.pdf) |
| 24 | [School Education and Sports Department](GRs/School_Education_and_Sports_Department) | 15 May 2018 | 01 December 2023 | 03-Dec-2023 | 3294 | 3257 | [201805161114241221.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201805161114241221.pdf) | [202312012038422721.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312012038422721.pdf) |
| 25 | [Skill Development and Entrepreneurship Department](GRs/Skill_Development_and_Entrepreneurship_Department) | 17 March 2018 | 28 November 2023 | 03-Dec-2023 | 861 | 857 | [201803171322099003.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803171322099003.pdf) | [202311281843435903.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311281843435903.pdf) |
| 26 | [Social Justice and Special Assistance Department](GRs/Social_Justice_and_Special_Assistance_Department) | 03 December 2019 | 30 November 2023 | 03-Dec-2023 | 1157 | 1151 | [201912051107011622.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201912051107011622.pdf) | [202311301754072622.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311301754072622.pdf) |
| 27 | [Soil and Water Conservation Department](GRs/Soil_and_Water_Conservation_Department) | 16 March 2018 | 01 December 2023 | 03-Dec-2023 | 1854 | 1720 | [201803161247582426.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803161247582426.pdf) | [202312011519340826.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312011519340826.pdf) |
| 28 | [Tourism and Cultural Affairs Department](GRs/Tourism_and_Cultural_Affairs_Department) | 14 March 2018 | 30 November 2023 | 03-Dec-2023 | 859 | 848 | [201803131542054523.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803131542054523.pdf) | [202312011553208523.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312011553208523.pdf) |
| 29 | [Tribal Development Department](GRs/Tribal_Development_Department) | 14 March 2018 | 01 December 2023 | 03-Dec-2023 | 1719 | 1691 | [201803091105184924.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803091105184924.pdf) | [202311301136431324.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311301136431324.pdf) |
| 30 | [Urban Development Department](GRs/Urban_Development_Department) | 07 March 2018 | 01 December 2023 | 03-Dec-2023 | 2117 | 2102 | [201803071203178325.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803071203178325.pdf) | [202312011449327225.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312011449327225.pdf) |
| 31 | [Water Resources Department](GRs/Water_Resources_Department) | 09 March 2018 | 01 December 2023 | 03-Dec-2023 | 2395 | 2378 | [201803091034435527.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803091034435527.pdf) | [202312011727398927.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312011727398927.pdf) |
| 32 | [Water Supply and Sanitation Department](GRs/Water_Supply_and_Sanitation_Department) | 13 March 2018 | 01 December 2023 | 03-Dec-2023 | 3211 | 3160 | [201803121414108428.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803121414108428.pdf) | [202312011528302528.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202312011528302528.pdf) |
| 33 | [Women and Child Development Department](GRs/Women_and_Child_Development_Department) | 17 March 2018 | 29 November 2023 | 03-Dec-2023 | 1157 | 1131 | [201803171539444330.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/201803171539444330.pdf) | [202311291550489130.pdf](https://gr.maharashtra.gov.in/Site/Upload/Government%20Resolutions/English/202311291550489130.pdf) |
----------------------------------------------------------------------------------------------------

**Total Orders**: 60,512 and **Total Translated Orders**: 55,071
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











