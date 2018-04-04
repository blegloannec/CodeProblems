#!/usr/bin/env python3

M = 10000
P = 10**9+7

N = [1]
N0,N1 = 1,0  # nb of anti-11 strings ending with 0/1
for i in range(1,M+1):
    N0,N1 = (N0+N1)%P,N0
    N.append((N0+N1)%P)
# (it's fibonacci btw)

# MAIN
T = int(input())
for _ in range(T):
    print(N[int(input())])
