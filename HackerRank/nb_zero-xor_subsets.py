#!/usr/bin/env python3

P = 10**9+7
Phi = P-1

T = int(input())
for _ in range(T):
    N = int(input())
    print(pow(2,(pow(2,N,Phi)-N)%Phi,P))
