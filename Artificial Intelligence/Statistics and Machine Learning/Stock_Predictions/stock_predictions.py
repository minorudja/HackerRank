def computeEMA(curPrice,dayPeriod,prevEMA):
    k = 2 / (dayPeriod + 1)
    return((curPrice * k) + (prevEMA * (1 - k)))

def printTransactions(m, k, d, name, owned, prices):
    buyDecision = []
    sellDecision = []
    finalDecisions = []

    emaShortList = []
    emaLongList = []

    for stk in range(k):
        emaShort = [prices[stk][0]]
        emaLong = [prices[stk][0]]

        for ind in range(1, len(prices[stk])):
            emaShort.append(round(computeEMA(prices[stk][ind],10,emaShort[-1]),2))
            emaLong.append(round(computeEMA(prices[stk][ind],200,emaLong[-1]),2))
        
        emaShortList.append(emaShort)
        emaLongList.append(emaLong)

        if (emaShort[-2] > emaLong[-2]) and (emaShort[-1] < emaLong[-1]):
            if prices[stk][-1] < m:
                divScore = (emaLong[-1] - emaShort[-1]) / prices[stk][-1]
                buyDecision.append((prices[stk][-1], divScore, name[stk]))
        
        if (emaShort[-2] < emaLong[-2]) and (emaShort[-1] > emaLong[-1]) and (owned[stk] > 0):
            sellDecision.append([name[stk],'SELL',owned[stk]])
    
    finalDecisions = sellDecision
    buyDecision = sorted(buyDecision, key=lambda x: (-x[1], x[0]))

    for buyIdx in range(len(buyDecision)):
        if m > buyDecision[buyIdx][0]:
            amt = int(m // buyDecision[buyIdx][0])
            finalDecisions.append([buyDecision[buyIdx][2],'BUY',amt])
            m = m - (buyDecision[buyIdx][0] * amt)
    
    noTrans = len(finalDecisions)
    print(noTrans)
    for i in range(noTrans):
        print(finalDecisions[i][0], finalDecisions[i][1], finalDecisions[i][2])


inputLine = [i for i in input().split()]
m = float(inputLine[0])
k = int(inputLine[1])
d = int(inputLine[2])

name = []
owned = []
prices = []
for stk in range(k):
    inputLine = [i for i in input().split()]
    name.append(inputLine[0])
    owned.append(int(inputLine[1]))
    prices.append(list(map(float, inputLine[2:])))

printTransactions(m, k, d, name, owned, prices)