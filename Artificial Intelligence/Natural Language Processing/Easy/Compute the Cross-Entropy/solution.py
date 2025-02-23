import math

def computeCrossEntropy(perplexity):
    return math.log(perplexity, 2)


## Main Program
pp = 170

crossEntropy = computeCrossEntropy(pp)
print(round(crossEntropy,2))