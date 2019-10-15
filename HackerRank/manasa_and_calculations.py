#!/usr/bin/env python3

MOD = 10**9+7

N = int(input())
P = [map(int,input().split()) for _ in range(N)]
S = 1
a_eq_b = True
for p,a,b in P:
    if a!=b:
        S *= pow(p,a,MOD) + pow(p,b,MOD)
        a_eq_b = False
    else:
        S *= pow(p,a,MOD)
    S %= MOD
if a_eq_b:
    S = (S+S) % MOD
print(S)
