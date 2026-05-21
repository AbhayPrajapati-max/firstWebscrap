import requests
from selenium import webdriver
from bs4 import BeautifulSoup
url='https://www.bbc.com'

response=requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')

title=soup.title.text
print(f"this is {title}")
name=soup.find_all("h2")
for h in name:
 print(h)
 text=h.get_text(strip=True)
 print(f'this first text \n{text}')
 if text:
  print(f'this if Text \n{text}')
  with open('bbcnew.txt','a',encoding='utf-8') as f:
   f.write(text+'\n')