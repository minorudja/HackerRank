def getMean(arr):
    return sum(arr)/len(arr)

def getPearsonCorrCoef(x,y):
    xMean = getMean(x)
    yMean = getMean(y)
    n = len(x)

    sumXY = sum([(x[i]-xMean)*(y[i]-yMean) for i in range(n)])
    sumX2 = sum([pow(x[i]-xMean,2) for i in range(n)])
    sumY2 = sum([pow(y[i]-yMean,2) for i in range(n)])

    r = sumXY / pow(sumX2*sumY2,0.5)

    try:
        r = sumXY / pow(sumX2*sumY2,0.5)
    except ZeroDivisionError:
        r = 0 # Least correlation coef

    return r


## Main Program
x = [15,12,8,8,7,7,7,6,5,3]         # Physics
y = [10,25,17,11,13,17,20,13,9,15]  # History

print(round(getPearsonCorrCoef(x,y),3))