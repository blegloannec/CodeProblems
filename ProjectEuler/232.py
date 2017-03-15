#!/usr/bin/env python3

from itertools import product

# P1 has a 1/2 proba to win 1 point
# the associated expected number of points per round is 1/2
# P2 has a 1/2^T proba to win 2^(T-1) points
# the associated expected number of points per round is 1/2^T * 2^(T-1) = 1/2

# DP solution, runs in 2s with python3

S = 100
TMAX = 10 # it's enough

memo = {}
# (min) probability of P1 to win from scores s1 & s2 at P1's turn
def P1(s1=0,s2=0):
    if (s1,s2) in memo:
        return memo[s1,s2]
    if s1>=S or s2>=S:
        # if s1>=100, then s1 wins otherwise s2 would have won at previous round
        return 1. if s1>=S else 0.
    # P1(s1,s2) = 1/2 * (1-1/2^T1) * P1(s1,s2) + 1/2 * (1-1/2^T2) * P1(s1+1,s2)
    #  + 1/2 * 1/2^T1 * P1(s1,s2+2^(T1-1)) + 1/2 * 1/2^T2 * P1(s1+1,s2+2^(T2-1))
    # for T1/T2 chosen by P2 when P1 has won/lost
    memo[s1,s2] = min((0.5*(1.-0.5**T2)*P1(s1+1,s2)+0.5**(T1+1)*P1(s1,s2+(1<<(T1-1)))+0.5**(T2+1)*P1(s1+1,s2+(1<<(T2-1)))) / (1.-0.5*(1.-0.5**T1)) for (T1,T2) in product(range(1,TMAX),range(1,TMAX)))
    return memo[s1,s2]

print(1-P1())
