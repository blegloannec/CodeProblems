#!/usr/bin/env python3

P = 10**9+7
XMAX = 10**5

# precomp fact
F = [1]
for n in range(1,2*XMAX+2):
    F.append((n*F[-1])%P)

def invmod(n):
    return pow(n,P-2,P)

def binom(n,p):
    assert(0<=p<=n)
    return (F[n]*invmod(F[p])*invmod(F[n-p])) % P

# *distinguishable* catalan(n) = n! * C_n
# gives the nb of balanced words on exactly
# n distinguishable pairs of parentheses
def dis_catalan(n):
    return (F[n] * binom(2*n,n) * invmod(n+1)) % P

# dp(Y,K) = nb of K-tuples of balanced words
#           on a total of Y distinguishable parentheses
# O(Y^3)
memo = {}
def dp(Y,K):
    assert(0<K<=Y)
    if K==1:
        return dis_catalan(Y)
    if (Y,K) in memo:
        return memo[Y,K]
    res = 0
    for y in range(1,Y-K+2):  # y<Y and Y-y>=K-1 (with K>=2)
        # words of size y  *  chosen parentheses  *  the rest
        res = (res + dis_catalan(y) * binom(Y,y) * dp(Y-y,K-1)) % P
    memo[Y,K] = res
    return res

# O(Y) formula
def formula(X,Y):
    res = 0
    for K in range(1,min(Y,2*X+1)+1):
        # pick K insertion positions for the Y distinguishable ()
        # and insert a K-tuple
        res = (res + binom(2*X+1,K) * dp(Y,K)) % P
    # balanced words on X distinguishable []
    res = (res * dis_catalan(X)) % P
    return res

def main():
    T = int(input())
    for _ in range(T):
        X,Y = map(int,input().split())
        print(formula(X,Y))

main()
