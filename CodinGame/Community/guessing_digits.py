#!/usr/bin/env python3

from operator import add, mul
from collections import defaultdict

# precomp. all solutions by eliminating possible deductions turn after turn
def precomp():
    Op = (add, mul)
    SumProd = [defaultdict(set) for _ in range(2)]
    for a in range(1,10):
        for b in range(a,10):
            for o in range(2):
                SumProd[o][Op[o](a,b)].add((a,b))
    Sol = {}
    t = 0
    while True:
        p = t&1
        AB = [ab for ab,s in SumProd[p].items() if len(s)==1]
        if not AB:
            break
        for ab in AB:
            a,b = SumProd[p][ab].pop()
            del SumProd[p][ab]
            Sol[a+b,a*b] = (a,b,t)
            SumProd[p^1][Op[p^1](a,b)].remove((a,b))
        t += 1
    return Sol

if __name__=='__main__':
    Sol = precomp()
    x = int(input())  # a+b
    y = int(input())  # a*b
    if (x,y) in Sol:
        a,b,t = Sol[x,y]
        print('({},{}) {} {}'.format(a, b, ('BURT','SARAH')[t&1], t//2+1))
    else:
        print('IMPOSSIBLE')
