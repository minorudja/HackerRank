def getMean(arr):
    mean = sum(x)/len(x)
    return mean
    
def getMedian(arr):
    arr.sort()
    N = len(arr)
    if (N%2) == 0:
        median = (arr[(N//2)-1] + arr[N//2])/2
    else:
        median = arr[N//2]
    return median
        
def getMode(arr):
    set_arr = set(arr)
    
    maxCount = 0
    for n in set_arr:
        freq = arr.count(n)
        if freq > maxCount:
            maxCount = freq
            mode = n
        if freq == maxCount:
            if n < mode:
                mode = n
    return mode
    
def getSD(arr):
    m = getMean(arr)
    meanSqSum = 0
    for n in arr:
        meanSqSum += pow(n-m,2)
    
    sd = pow((meanSqSum/len(arr)),0.5)
    return sd
    
def getLUB(arr):
    mean = getMean(arr)
    sd = getSD(arr)
    sd_m = sd / pow(len(arr),0.5)
    
    lub = [mean - (1.96 * sd_m), mean + (1.96 * sd_m)]
    return lub
    

N = int(input())
x = list(map(int,input().split()))

print(round(getMean(x),1))
print(round(getMedian(x),1))
print(getMode(x))
print(round(getSD(x),1))
lub = getLUB(x)
print(round(lub[0],1),round(lub[1],1))