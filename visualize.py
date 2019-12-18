import matplotlib.pyplot as plt
import pandas as pd
import time

now = []
prophet = []
ari = []
#실제 주식 데이터
a = pd.read_csv('now_exchange.csv', thousands = ',', header=0)

#prophet 예측 데이터
b = pd.read_csv('exchange_predict_now.csv', thousands = ',', header=0)

#arima 예측 데이터
c = pd.read_csv('arima_predict.csv', thousands = ',', header=0)

aa = []
bb = []
#12월2일부터 12월 17일까지 예측 가격 리스트에 저장
for i in range(3703, 3715):
    aa.append(a['y'][i])
    bb.append(b['exchange'][i])


df = pd.DataFrame(columns=['date', 'prophet', 'arima', 'real'])
df["date"] = c['ds']
df["prophet"] = bb
df['arima'] = c['y']
df['real'] = aa
df.to_csv("C:./result_predict_now.csv", mode='w', header=True, index=False)


result = pd.read_csv('result_predict_now.csv', thousands = ',', header=0, index_col=0)
plt.plot(result['prophet'], color="red",label='prophet')
plt.plot(result['arima'], color="blue",label= 'arima')
plt.plot(result['real'], color="black", label = 'real')
plt.legend()
plt.show()

