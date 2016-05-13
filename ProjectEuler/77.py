#!/usr/bin/env python

import sys
from math import sqrt

# similar to 31 with prime numbers as coin values

def eratosthene(n):
    l = range(2,n+1)
    s = int(sqrt(n))+1
    for i in range(2,s):
        for k in range(2*i,n+1,i):
            l[k-2] = -1
    return filter((lambda x: x>0),l)

V = eratosthene(1000)

memo = {}
def C(s,k):
    if s==0:
        return 1
    if k<0:
        return 0
    if (s,k) in memo:
        return memo[(s,k)]
    res = C(s,k-1)
    if s>=V[k]:
        res += C(s-V[k],k)
    memo[(s,k)] = res
    return res

def main():
    n = 0
    while C(n,len(V)-1)<=5000:
        n += 1
    print n

main()
