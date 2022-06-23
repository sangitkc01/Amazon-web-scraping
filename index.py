from bs4 import BeautifulSoup
import requests


HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})
n=int(input('enter pages = '))
l=[]
for i in range(n):  
    url=BeautifulSoup(f"https://www.amazon.com/s?k=guitar&page={i}&crid=2IQADK0QSXLPZ&qid=1655994706&sprefix=guitar%2Caps%2C447&ref=sr_pg_{i}","html.parser")
    res=requests.get(url,headers=HEADERS)
    soup=BeautifulSoup(res.content,'lxml')
    product=soup.find_all("div",class_="a-section a-spacing-small s-padding-left-small s-padding-right-small") 
    for j in product:
        Guitar_name=j.find("div",class_="a-section a-spacing-none a-spacing-top-small s-title-instructions-style")
        des=Guitar_name.h2.a
        des1=des.text.strip()
        
        des2=des.get('href')

        data={
            "Guitar Name " : des1,
            "href ": des2,
            
        }
        l.append(data)

import pandas as pd
df=pd.DataFrame(l)
print(df)
