from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

date_list = []
ex_rate_list = []
path = "C:/Users/dbdrl/Desktop/융기/chromedriver.exe"
driver = webdriver.Chrome(path)
for i in range(0, 370):
    driver.get("https://finance.naver.com/marketindex/exchangeDailyQuote.nhn?marketindexCd=FX_USDKRW&page=%s" % str(i+1))
    rcv_data = driver.page_source
    soupData = BeautifulSoup(rcv_data, 'html.parser')
    date = soupData.findAll('td', attrs={'class': 'date'})
    price = soupData.findAll('td', attrs={'class' : 'num'})
    for i in range(0, 20, 2):
        ex_rate_list.append(price[i].get_text())
    for title in date:
        date_list.append(title.get_text())

ex_rate_list.reverse()
date_list.reverse()

df = pd.DataFrame(columns=['date', 'exchange'])
df["date"] = date_list
df["exchange"] = ex_rate_list
df.to_csv("C:./now_exchange.csv", mode='w', header=True, index=False)


