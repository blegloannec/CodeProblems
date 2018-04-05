#!/usr/bin/env python3

# the numbers on balls are distinct

P = 10**9+7

def inv(n):
    return pow(n,P-2,P)

# fact mod
F = [1,1]
def precomp_fact(N):
    for n in range(2,N+1):
        F.append((n*F[-1])%P)

def binom(n,p):
    if not 0<=p<=n:
        return 0
    return (F[n]*inv(F[p])*inv(F[n-p]))%P

def main():
    N,K = map(int,input().split())
    B = sorted(map(int,input().split()))
    precomp_fact(N)
    S = 0
    for i in range(N):
        S = (S + B[i] * (binom(i,K-1) - binom(N-i-1,K-1))) % P
    print(S)

main()
