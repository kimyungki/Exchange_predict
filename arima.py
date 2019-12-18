import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

#Arima
data_ARIMA = pd.read_csv('C:/Users/dbdrl/Desktop/융기/now_exchange.csv', thousands = ',', header=0, index_col=0)



#차분하기
diff1=data_ARIMA.diff(periods=1).iloc[1:]

#ARIMA모수 구한 후 입력하기
model = ARIMA(data_ARIMA, order=(1,1,1))

#상수제거
model_fit = model.fit(trend='nc')

#예측할 개수
fore = model_fit.forecast(steps=1)
print(fore)