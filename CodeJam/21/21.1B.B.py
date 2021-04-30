#!/usr/bin/env python3

from math import gcd

def greedy(u0):
    Cnt = [0]*(u0+1)
    Cnt[u0] = 1
    for u in range(u0,-1,-1):
        if u<len(U):
            if Cnt[u]<U[u]:
                return False
            else:
                Cnt[u] -= U[u]
        if u-A>=0:
            Cnt[u-A] += Cnt[u]
        if u-B>=0:
            Cnt[u-B] += Cnt[u]
    return True

def main():
    global A,B,U
    T = int(input())
    for t in range(1, T+1):
        N,A,B = map(int, input().split())
        U = list(map(int, input().split()))
        G = gcd(A,B)
        R = [i%G for i,u in enumerate(U) if u>0]
        if not all(r==R[0] for r in R):
            print(f'Case #{t}: IMPOSSIBLE')
        else:
            m0 = max(i for i,u in enumerate(U) if u>0)
            u0 = R[0]
            while u0<m0 or not greedy(u0):
                u0 += G
            print(f'Case #{t}: {u0+1}')

main()
