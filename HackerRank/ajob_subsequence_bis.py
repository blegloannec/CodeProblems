#!/usr/bin/env python3

# cf ajob_subsequence.py
# Method 2: using Lucas's theorem

def digits(n):
    D = []
    while n:
        n,d = divmod(n,P)
        D.append(d)
    return D

def inv(n):
    return pow(n,P-2,P)

def binom(n,p):
    if 0<=p<=n:
        return (Fact[n] * inv((Fact[p]*Fact[n-p])%P)) % P
    return 0

def binom_lucas(n,k):
    assert 0<=k<=n
    Dn = digits(n)
    Dk = digits(k)
    while len(Dk)<len(Dn):
        Dk.append(0)
    res = 1
    for ni,ki in zip(Dn,Dk):
        res = (res * binom(ni,ki)) % P
    return res

if __name__=='__main__':
    T = int(input())
    for _ in range(T):
        N,K,P = map(int,input().split())
        Fact = [1]*P
        for i in range(2,P):
            Fact[i] = (Fact[i-1]*i) % P
        print(binom_lucas(N+1,K+1))
