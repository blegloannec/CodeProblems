#!/usr/bin/env pypy

# runs in <2s with pypy

# NB: analogue au pb HackerRank / Week of Code 20 / Simple Game

N = 200

# ===== Code pour intuiter la fonction de Grundy =====
# generateur des partitions de n a k composantes
def partitions(n,k):
    if k==1:
        yield [n]
    elif k<=n:
        for p in partitions(n-1,k-1):
            p.append(1)
            yield p
        for p in partitions(n-k,k):
            for i in xrange(k):
                p[i] += 1
            yield p

def mex(succ):
    i = 0
    while i in succ:
        i += 1
    return i

memo = {}
def grundy(n,k):
    if n==1:
        return 0
    if (n,k) in memo:
        return memo[n,k]
    succ = set()
    for l in xrange(2,k+1):
        for P in partitions(n,l):
            x = 0
            for p in P:
                x ^= grundy(p,k)
            succ.add(x)
    g = mex(succ)
    memo[n,k] = g
    return g

# Fonctions de Grundy_k decouvertes
G3 = [grundy(n,3) for n in xrange(1,N+1)]  # (formule explicite pour k=3 ??)
def G(k,n):
    #assert(0<n<=N and k>1)
    if k==2:
        return 1-(n&1)
    if k==3:
        return G3[n-1]
    # identiques pour k>=4
    return n-1
# ==========


P = 10**9+7

# Partitions d'entiers, O(n^2)
# (nb de partitions de n dont les composantes sont <= m)
memPart = {}
def Part(n,m):
    if n==0:
        return 1
    if m==0:
        return 0
    if (n,m) in memPart:
        return memPart[n,m]
    #assert(m<=n)
    res = (Part(n,m-1) + Part(n-m,min(m,n-m))) % P
    memPart[n,m] = res
    return res

# Partitions d'entiers dont la fonction de Grundy_k est x, O(n^3)
def GrundyPart(k,n,m,x,memo):
    if n==0:
        return int(x==0)
    if m==0:
        return 0
    if (n,m,x) in memo:
        return memo[n,m,x]
    #assert(m<=n)
    res = (GrundyPart(k,n,m-1,x,memo) + GrundyPart(k,n-m,min(m,n-m),x^G(k,m),memo)) % P
    memo[n,m,x] = res
    return res

def f(n,k):
    return Part(n,n) - GrundyPart(k,n,n,0,{})

def g(n):
    # assert(n>=3)
    return (f(n,2) + f(n,3) + (n-3)*f(n,4)) % P

print g(N)
