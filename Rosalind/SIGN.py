#!/usr/bin/env python3

from itertools import *

def fact(n):
    return 1 if n<=1 else n*fact(n-1)

n = int(input())
print(fact(n)*2**n)
for P in permutations(range(1,n+1)):
    for M in product([-1,1],repeat=n):
        S = [m*a for (m,a) in zip(M,P)]
        print(' '.join(map(str,S)))
