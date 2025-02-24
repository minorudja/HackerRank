import itertools
import math

## Main Program
allDiceComb = list(itertools.product(range(1,6+1),repeat = 2))

constraintComb = []
for comb in allDiceComb:
    if ((sum(list(comb)) == 6) and (comb[0] != comb[1])):
        constraintComb.append(1)
    else:
        constraintComb.append(0)

num = sum(constraintComb)
denom = len(constraintComb)

print("{}/{}".format(num//math.gcd(num,denom),denom//math.gcd(num,denom)))