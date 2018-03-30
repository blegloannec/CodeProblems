#!/usr/bin/env python3

from collections import Counter

# basic combinatorics
# difficulty "Hard", really?!

P = 10**9+7

# factorials mod
N = 10**5+1
F = [1]*N
for n in range(2,N):
    F[n] = (n*F[n-1]) % P

def inv(n):
    return pow(n,P-2,P)

def anacount(S):
    C = Counter(S)
    if sum(C[c]%2 for c in C)>1:
        return 0
    res = F[len(S)//2]
    for c in C:
        res = (res*inv(F[C[c]//2])) % P
    return res

S = input().strip()
print(anacount(S))
