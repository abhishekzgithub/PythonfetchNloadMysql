# [Bombay Stock Exchange Shareholding Pattern](https://www.bseindia.com/index.html)

## Introduction

This is a scraping script made in order to scrape the data from bombay stock exchange.


## Ground Rules

* You need to download  python from the below link
 
   >[python v3](https://www.python.org/downloads/)
    
* You need to  **clone or download** the below repository

   > [Bitbucket link](git clone https://abhishekzbitbucket@bitbucket.org/1018mb/bse_python.git)

* You need to download [Visual Studio code](https://code.visualstudio.com/download)
    

## Getting started

* Clone or download the repository or code from the github repository.
 
* Make sure you can open it inside visual studio code.
 
* Goto the **bse_python** folder

 > ```cd bse_python ```
        
* Rename the template_env  to **.env** and provide the credentials.

* Run on the command line

  > ```pip install pipenv```
  
  > ```pipenv shell```
  
  > ```pipenv install -r requirements.txt```
  
  > ```python run.py```
        
* The results will be downloaded in the **scraped_data** folder in an csv format with the name as **final_df.csv**.

* To schedule it on every **monday** , you may run the **scheduler.py** for it.
   > ```python scheduler.py```

 
 
## Place to know from where the data is getting scraped
 
* https://www.bseindia.com/index.html
 
* Goto **Corporates** tab
 
* Goto the **Corporate Fillings** tab
 
* Then goto **Shareholding Patterns**

> ```https://www.bseindia.com/corporates/Sharehold_Searchnew.aspx```


* For Security name **539807** and quarter **June**, this will lead to


> ```https://www.bseindia.com/corporates/shpPromoterNGroup.aspx?scripcd=539807&qtrid=102```


* The code will rotate over the ```security name``` and ```qtrid``` in the URL and will scrape the data

## Thanks
 
- Please give star if you are using or like it.