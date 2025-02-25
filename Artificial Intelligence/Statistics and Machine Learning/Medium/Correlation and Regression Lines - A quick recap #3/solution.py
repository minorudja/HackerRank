def getMean(arr):
    return sum(arr)/len(arr)

def getRegressionParams(x,y):
    xMean = getMean(x)
    yMean = getMean(y)
    n = len(x)

    sumXY = sum([(x[i]-xMean)*(y[i]-yMean) for i in range(n)])
    sumX2 = sum([pow(x[i]-xMean,2) for i in range(n)])

    m = sumXY / sumX2
    c = yMean - m * xMean

    return (m,c)


## Main Program
x = [15,12,8,8,7,7,7,6,5,3]         # Physics
y = [10,25,17,11,13,17,20,13,9,15]  # History

m, c = getRegressionParams(x,y)

x_1 = 10
y = (m * x_1) + c

print(round(y,1))