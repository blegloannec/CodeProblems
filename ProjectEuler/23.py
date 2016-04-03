#!/usr/bin/env python

NMAX = 28123

def divisors(n):
    return filter((lambda d: n%d==0), range(1,n))

def abundant(n):
    return sum(divisors(n))>n

A = filter(abundant,range(1,NMAX))

res = 0
for n in range(1,NMAX):
    for a in A:
        if a>=n:
            res += n
            break
        if n-a in A:
            break
print res
