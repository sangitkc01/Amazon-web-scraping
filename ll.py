from bs4 import BeautifulSoup
import requests

HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})
n=int(input('enter pages = '))
l=[]
for i in range(n):  
    url=BeautifulSoup(f"https://www.amazon.com/s?k=guitar&page={i}&crid=2IQADK0QSXLPZ&qid=1655994706&sprefix=guitar%2Caps%2C447&ref=sr_pg_{i}","html.parser")
    res=requests.get(url,headers=HEADERS)
    soup=BeautifulSoup(res.content,'lxml')
    product=soup.find_all("div",class_="a-section a-spacing-none a-spacing-top-small s-title-instructions-style") 
    
    for j in product:
        Guitar_name=j.find("span",class_="a-size-base-plus a-color-base a-text-normal").text.strip()
       
        data={
            "Guitar Name " : Guitar_name
            }
        l.append(data)
       

import pandas as pd
df=pd.DataFrame(l)
dff=df.to_csv("amazon_guitar_data.csv")

