#!/usr/bin/env python

# si l'on prend k pierres, il faut n-k > 2k pour que l'adversaire
# ne puisse pas tout prendre, donc k<n/3

# DP pour determiner si n pierres est une position gagnante
# lorsque l'on peut prendre 1<=k<=p pierres
memo = {}
def win(n,p):
    if n==0:
        return False
    if n<=p:
        return True
    if (n,p) in memo:
        return memo[n,p]
    res = False
    for k in xrange(1,p+1):
        if not win(n-k,2*k):
            res = True
            break
    memo[n,p] = res
    return res

def M_naive(n):
    for p in xrange(n-1,0,-1):
        if not win(n-p,2*p):
            return p
    return 0

# on remarque que M(i) = 0 ssi est un nombre de Fibonacci
def fibo(n):
    F = [1,1]
    for _ in xrange(n):
        F.append(F[-1]+F[-2])
    return F

F = fibo(100)

# et le pattern suivant lie a la suite de Fibonacci
def M_pattern(n):
    i = len(F)-1
    while n<F[i]:
        i -= 1
    f = F[i]
    while f<=2*(n-f):
        n -= f
        i -= 2
        f = F[i]
    return n-f

# genere la liste des intervalles significatifs
# pour les valeurs de F[i] a F[i+1]-1
def gen_ruptures(i):
    R = [(F[i],0)]
    d = F[i]
    for k in xrange(i,4,-2):
        n = (3*F[k]+1)/2-F[k]
        R.append((d+n,n-F[k-2]))
        d += F[k-2]
        n -= F[i]
    return R

def S(n):
    s = 0
    for i in xrange(2,len(F)-1):
        R = gen_ruptures(i)
        R.append((F[i+1],0))
        for k in xrange(len(R)-1):
            a,b,v = R[k][0],R[k+1][0]-1,R[k][1]
            if b>n:
                b = n
            s += (b-a+1)*(v+v+b-a)/2
            if b==n:
                return s

print S(10**18)%(10**8)
