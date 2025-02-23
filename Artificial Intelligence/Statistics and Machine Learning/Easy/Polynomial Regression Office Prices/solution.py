import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

F,N = map(int,input().split())

x = []
y = []
for i in range(N):
    inputRow = list(map(float,input().split()))
    
    x.append(inputRow[:F])
    y.append(inputRow[F])
    
T = int(input())
testX = []
for i in range(T):
    testX.append(list(map(float,input().split())))

# Fit polynomial features
poly = PolynomialFeatures(degree=3)
X_poly = poly.fit_transform(x)

# Fit the model
model = LinearRegression()
model.fit(X_poly, y)

#Transform test data
testX_poly = poly.fit_transform(testX)

predicted_price = model.predict(testX_poly)

for p in predicted_price:
    print(round(p,2))