#!/usr/bin/env python3

import sys
sys.setrecursionlimit(2000)
from functools import lru_cache

# DP to "optimize" the expected score
# To reduce the conf. space, we restrict ourselves to configurations
# with (full stacks excluded):
#  - c1 stacks of size B-1 (hence c1 available top positions)
#  - c2                B-2 (      c2           2nd          )
#  - r (<= N-c1-c2) remaining stacks:
#    * exactly 1 of size h < B-2: the current "garbage" stack
#    * r-1 empty stacks
# This restriction does not lead to the actual optimal, but it is
# good enough to approximate it as the topmost positions have the
# most weight in the score.
# Indeed, for B = 15 and N = 20,
# we compute  E(0, 0, 0, 20) = 19086952424670876
# while the statement provides 19131995794056374.42
def DP(c1, c2, h, r, d):
    emax = 0.
    move = 0
    if c1>0:
        e = d*10.**(B-1) + E(c1-1, c2, h, r)
        if e>=emax:
            emax = e
            move = 1
    if c2>0:
        e = d*10.**(B-2) + E(c1+1, c2-1, h, r)
        if e>=emax:
            emax = e
            move = 2
    if r>0:
        if h==B-3:
            e = d*10.**h + E(c1, c2+1, 0, r-1)
        else:
            e = d*10.**h + E(c1, c2, h+1, r)
        if e>=emax:
            emax = e
            move = 3
    return (emax, move)

@lru_cache(maxsize=None)
def E(c1, c2, h, r):
    return sum(DP(c1, c2, h, r, d)[0] for d in range(10))/10.

def case():
    C1 = []
    C2 = []
    h = 0
    R = list(range(1,N+1))
    for _ in range(N*B):
        D = int(input())
        _, move = DP(len(C1), len(C2), h, len(R), D)
        assert move!=0
        if move==1:
            pick = C1.pop()
        elif move==2:
            pick = C2.pop()
            C1.append(pick)
        else:
            h += 1
            pick = R[-1]
            if h==B-2:
                R.pop()
                C2.append(pick)
                h = 0
        print(pick, flush=True)

def main():
    global N,B
    T,N,B,P = map(int, input().split())
    for _ in range(T):
        case()
    assert input()=='1'

main()
