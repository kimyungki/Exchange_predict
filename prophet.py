import pandas as pd
import matplotlib.pyplot as plt
from fbprophet import Prophet

#fbpropher

# housands = ',' 옵션으로 천 단위 자리수 구분 콤마 없애고 불러오기
data_exchange = pd.read_csv('C:/Users/dbdrl/Desktop/융기/now_exchange.csv', thousands = ',')

#Prophet 클래스 객체를 만듬
m = Prophet()

#시계열 데이터 입력으로 fit 메서드를 호출
m.fit(data_exchange)

#예측하고 싶은 날짜 구간을 생성 미래 Dataframe 생성
predict = m.make_future_dataframe(periods=365)

predict2 = m.predict(predict)

#왼쪽부터 날짜,예측값,예측최소값,예측최대값
print(predict2[['ds','yhat','yhat_lower', 'yhat_upper']])


fig1 = m.plot(predict2)
plt.show(fig1)

m.plot_components(predict2)
plt.show()

#csv파일로 저장
df = pd.DataFrame(columns=['date', 'exchange', 'lower', 'upper'])
df["date"] = predict2['ds']
df["exchange"] = predict2['yhat']
df['lower'] = predict2['yhat_lower']
df['upper'] = predict2['yhat_upper']
df.to_csv("C:./exchange_predict_now.csv", mode='w', header=True, index=False)

