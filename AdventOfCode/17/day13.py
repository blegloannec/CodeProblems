#!/usr/bin/env python3

import sys
from fractions import gcd

I = [tuple(map(int,L.split(':'))) for L in sys.stdin.readlines()]

# Part 1
print(sum(d*r for (d,r) in I if d%(2*(r-1))==0))

# Part 2
def brute2():  # naive approach, ~3s with python3
    t = 0
    while any((t+d)%(2*(r-1))==0 for (d,r) in I):
        t += 1
    print(t)

#brute2()
    
def lcm(a,b):
    return (a*b)//gcd(a,b)

def filter2():  # fast approach to compute all the solutions
    S = [0]  # all possible delays between 0 and lcm(considered periods)
    l = 1
    for (d,r) in I:
        p = 2*(r-1)
        l0 = l
        l = lcm(l,p)
        T = []
        for x in S:
            for y in range(x,l,l0):
                if ((y+d)%p!=0):
                    T.append(y)
        S = T
    print(min(S))

filter2()
