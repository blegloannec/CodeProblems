#!/usr/bin/env python

# Considering 2,3,5,7 truncatable (but not in the final sum)
# p = a_n...a_0 truncatable iff
# p prime and a_(n-1)...a_0 left-truncatable
# and a_n...a_1 right-truncatable

from math import *

def eratosthene(n):
    l = range(2,n+1)
    s = int(sqrt(n))+1
    for i in range(2,s):
        for k in range(2*i,n+1,i):
            l[k-2] = -1
    return filter((lambda x: x>0),l)

def trunc_pair(n):
   m = 10**int(log10(n))
   return (n-(n/m)*m,n/10)

def problem37():
    P = eratosthene(1000000)
    LT = [2,3,5,7]
    RT = [2,3,5,7]
    T = []
    for p in P[4:]:
        a,b = trunc_pair(p)
        plt,prt = a in LT, b in RT
        if plt:
            LT.append(p)
        if prt:
            RT.append(p)
        if plt and prt:
            T.append(p)
    print sum(T)

problem37()
