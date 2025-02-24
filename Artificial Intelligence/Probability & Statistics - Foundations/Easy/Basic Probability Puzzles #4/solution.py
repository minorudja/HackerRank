from itertools import product
from math import prod, gcd
from copy import deepcopy

## Main Program
bags = [[4,5],[3,7]]
drawOrder = [1,2,2]

allComb = list(product('RB',repeat = 3))
filterComb = [comb for comb in allComb if list(comb).count('B') == 2]

prob_num = 0
for comb in filterComb:
    p_num = 1
    temp_bags = deepcopy(bags)  #To fix list copy referencing issue
    for i in range(len(comb)):
        if comb[i] == 'R':
            p_num *= temp_bags[drawOrder[i]-1][0]
            temp_bags[drawOrder[i]-1][0] -= 1
        else:
            p_num *= temp_bags[drawOrder[i]-1][1]
            temp_bags[drawOrder[i]-1][1] -= 1
    prob_num = prob_num + p_num

prob_denom = sum(bags[0]) * sum(bags[1]) * (sum(bags[1])-1)
print("{}/{}".format(prob_num//gcd(prob_num,prob_denom),prob_denom//gcd(prob_num,prob_denom)))