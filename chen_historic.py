import requests
from bs4 import BeautifulSoup
import pprint
import pandas as pd
import openpyxl
r = requests.get("https://zh.wikipedia.org/wiki/%E8%87%BA%E5%8C%97%E5%B8%82%E6%AD%B7%E5%8F%B2%E5%BB%BA%E7%AF%89%E5%88%97%E8%A1%A8")
soup = BeautifulSoup(r.text, "html.parser")#臺北市歷史建築列表

tables1 = soup.find("table")#要來找table,條件放後面 ;wikitable sortable jquery-tablesorter有十個
# for i in range(11):

    # for table in tables:   
trs = tables1.find_all("tr")#第一個table進來 開始帶入 改成尋找這一個table裡頭的tr(很多個)

result1 = []
result2 = []
for tr in trs:#第一個tr進來 開始帶入 改成尋找這一個tr裡頭的td
    tds = tr.find_all("td")#~~~~trs太多他不知道你要哪個  要單獨的東西才可以執行查找功能
        
       
        
            #這個tds 又是一團td
    for div in tds:
        # #inside of this loop you will be accessing each review
        if div == tds[0]:
            # print(div.text)
            result1.append((div.text.replace("\n","")))
            # print(result1)
        if div == tds[3]:
            # print(div.text)
            result2.append((div.text.replace("\n","")))
            # print(result)
            # print("")    #doing this to print a blank line to "separate" them for you
# print(len(result2))
# print(len(result1))
df = pd.DataFrame(list(zip(result1,result2)), columns=["名稱","創建年代"])
# https://stackoverflow.com/questions/60751819/valueerror-2-columns-passed-passed-data-had-1-columns
# 以上是網路上找到的solution
print(df)
df.to_excel("accupass.xlsx", sheet_name="history", index=False)  # 匯出Excel檔案(不寫入資料索引值)
