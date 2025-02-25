import random

def simulateSnakesAndLadders(boardSize, diceProb, ladStartCoords, ladEndCoords, snakStartCoords, snakEndCoords):
    rollAttempts = 0
    curSquare = 1

    while (curSquare != boardSize) and (rollAttempts < 1000):
        roll = random.choices([1, 2, 3, 4, 5, 6], weights=diceProb)[0]
        rollAttempts += 1

        if (curSquare + roll) <= boardSize:
            curSquare += roll
            
            # Ladder Check
            if curSquare in ladStartCoords:
                ladInd = ladStartCoords.index(curSquare)
                curSquare = ladEndCoords[ladInd]
            
            # Snake Check
            if curSquare in snakStartCoords:
                snakInd = snakStartCoords.index(curSquare)
                curSquare = snakEndCoords[snakInd]
    
    if ((rollAttempts == 1000) and (curSquare != boardSize)):
        rollAttempts = 0    # Ignore if game hasn't terminated after 1000 rolls

    return rollAttempts

def getAverage(arr):
    return (sum(arr) / len(arr))


## Main Program
noGames = 5000
boardSize = 100

T = int(input())
for tests in range(T):
    diceProb = list(map(float,input().split(',')))
    noLadders, noSnakes = map(int,input().split(','))
    rawInput = input().split()
    ladStartCoords = []
    ladEndCoords = []
    for lad in range (noLadders):
        coords = list(map(int,rawInput[lad].split(',')))
        ladStartCoords.append(coords[0])
        ladEndCoords.append(coords[1])
    rawInput = input().split()
    snakStartCoords = []
    snakEndCoords = []
    for snak in range (noSnakes):
        coords = list(map(int,rawInput[snak].split(',')))
        snakStartCoords.append(coords[0])
        snakEndCoords.append(coords[1])
    
    rollCounts = []
    for game in range(noGames):
        rolls = simulateSnakesAndLadders(boardSize, diceProb, ladStartCoords, ladEndCoords, snakStartCoords, snakEndCoords)
        if rolls > 0:
            rollCounts.append(rolls)

    print(int(getAverage(rollCounts)))