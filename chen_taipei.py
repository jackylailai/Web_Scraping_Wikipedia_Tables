import requests
from bs4 import BeautifulSoup
import pprint


r = requests.get("https://zh.wikipedia.org/wiki/%E8%87%BA%E5%8C%97%E5%B8%82%E7%9B%B4%E8%BD%84%E5%B8%82%E5%AE%9A%E5%8F%A4%E8%B9%9F%E5%88%97%E8%A1%A8")
soup = BeautifulSoup(r.text, "html.parser")

tables1 = soup.find("table")#要來找table,條件放後面 ;wikitable sortable jquery-tablesorter有十個
# for i in range(11):

    # for table in tables:   
trs = tables1.find_all("tr")#第一個table進來 開始帶入 改成尋找這一個table裡頭的tr(很多個)
        
for tr in trs:#第一個tr進來 開始帶入 改成尋找這一個tr裡頭的td
    tds = tr.find_all("td")#~~~~trs太多他不知道你要哪個  要單獨的東西才可以執行查找功能
        
       
        
            #這個tds 又是一團td
    for div in tds:
        # #inside of this loop you will be accessing each review
        if div == tds[0]:
            print(div.text)
        if div == tds[3]:
            print(div.text)

            # print("") #doing this to print a blank line to "separate" them for you



                



