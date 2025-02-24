from itertools import product
from math import prod, gcd

## Main Program
urns = [[4,3],[5,4],[4,4]]

allComb = list(product('RB',repeat = 3))
filterComb = [comb for comb in allComb if list(comb).count('R') == 2]

prob_num = 0
for comb in filterComb:
    p_num = 1
    for i in range(len(comb)):
        if comb[i] == 'R':
            p_num *= urns[i][0]
        else:
            p_num *= urns[i][1]
    prob_num = prob_num + p_num

prob_denom = prod([sum(x) for x in urns])
print("{}/{}".format(prob_num//gcd(prob_num,prob_denom),prob_denom//gcd(prob_num,prob_denom)))