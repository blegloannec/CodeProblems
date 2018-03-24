#!/usr/bin/env python3

def precomp_binom(M):
    M += 1
    B = [[0]*M for _ in range(M)]
    B[0][0] = 1
    for n in range(1,M):
        B[n][0] = 1
        for p in range(1,n+1):
            B[n][p] = B[n-1][p-1] + B[n-1][p]
    return B

B = precomp_binom(20)

def kth_path(X,Y,K):
    P = []
    k = 0
    while X>0 or Y>0:
        if X>0 and k+B[X+Y-1][X-1]>K:
            X -= 1
            P.append('H')
        else:
            if X>0:
                k += B[X+Y-1][X-1]
            Y -= 1
            P.append('V')
    return ''.join(P)

def main():
    T = int(input())
    for _ in range(T):
        X,Y,K = map(int,input().split())
        print(kth_path(X,Y,K))

main()
