from statsmodels.tsa.arima.model import ARIMA

## Main Program
N = int(input())
passCount = [0 for i in range(N)]
for i in range(N):
    inputList = input().split('\t')
    passCount[int(inputList[0][9:])-1] = int(inputList[1])

arima_model = ARIMA(passCount, order = (1,1,2))
model_fit = arima_model.fit()

predictions = model_fit.forecast(steps=12)  # Predict next 12 points
for pred in predictions:
    print(int(pred))