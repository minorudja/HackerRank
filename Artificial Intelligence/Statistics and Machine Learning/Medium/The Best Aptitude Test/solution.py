def getMean(arr):
    return sum(arr)/len(arr)

def getPearsonCorrCoef(x,y):
    xMean = getMean(x)
    yMean = getMean(y)
    n = len(x)

    sumXY = sum([(x[i]-xMean)*(y[i]-yMean) for i in range(n)])
    sumX2 = sum([pow(x[i]-xMean,2) for i in range(n)])
    sumY2 = sum([pow(y[i]-yMean,2) for i in range(n)])

    try:
        r = sumXY / pow(sumX2*sumY2,0.5)
    except ZeroDivisionError:
        r = 0 # Least correlation coef

    return r

def getBestAptitudeTest(N,gpa,aptTest_Scores):
    pearsonR2Scores = []
    for testInd in range(5):
        pearsonR2Scores.append(pow(getPearsonCorrCoef(gpa,aptTest_Scores[testInd]),2))
    
    maxCoefInd = pearsonR2Scores.index(max(pearsonR2Scores))
    return (maxCoefInd + 1)


## Main Program
T = int(input())
for tc in range(T):
    aptTest_Scores = []
    N = int(input())
    gpa = list(map(float,input().split()))
    for i in range(5):
        aptTest_Scores.append(list(map(float,input().split())))
    print(getBestAptitudeTest(N,gpa,aptTest_Scores))