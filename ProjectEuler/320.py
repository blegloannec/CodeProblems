#!/usr/bin/env python

from collections import defaultdict

# si p premier, la multiplicite de p dans n! est
# a = sum( n/p^i, i>1 ) en division entiere
# c'est donc en particulier borne par n*sum( 1/p^i, i>1 ) = n/(p-1)
# donc n/p <= a <= n/(p-1) (permiere inegalite triviale, n/p est le
# nb de multiples de p qui sont <= n)
# donc a(p-1) <= n <= ap, soit un intervalle d'ordre a
# dans le pire cas, i.e. pour p=2, a <= n <= 10^6 sur les entrees
# donc on aura sur les solutions de ce pb des a verifiant
# 1234567890 ~ 10^9 <= a <= 1234567890*10^6 ~ 10^15
# il est raisonnable de faire une recherche dichotomique dedans

# On deduira facilement les decompositions des n! jusqu'a n = 10^6
# a partir des decompositions des nb <= 10^6 obtenues en criblant

# runs in 39s with pypy

def sieve_decomp(N):
    P = [True for _ in xrange(N)]
    Decomp = [[] for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,N):
        if P[i]:
            Decomp[i].append((i,1))
            for k in xrange(2*i,N,i):
                P[k] = False
                m = 1
                l = k/i
                while l%i==0:
                    l /= i
                    m += 1
                Decomp[k].append((i,m))
    return P,Decomp

# multiplicite de p dans la decomposition de n!
def fact_mult(n,p):
    res = 0
    q = p
    while n>=q:
        res += n/q
        q *= p
    return res

# recherche dichotomique du plus petit n tel que la
# multiplicite de p dans n! soit >= a
def dicho(p,a):
    n,N = a*(p-1),a*p
    while N>n:
        m = (n+N)/2
        if fact_mult(m,p)<a:
            n = m+1
        else:
            N = m
    return n

# MAIN
N = 10**6
M = 10**18
A = 1234567890
# D la decomposition de i! pour le i courant
D = defaultdict(int)
# Ta[p] = valeur du n minimal pour lequel la multiplicite
# de p dans la decompositon de i! (i courant) est >= D[p]*A
Ta = {}
# valeur maximale de Ta, vaut N(i) pour le i courant
maxTa = -1

def fusion_decomp(decomp):
    global maxTa
    for (p,m) in decomp:
        D[p] += m
        # on met a jour Ta[p] et maxTa
        Ta[p] = dicho(p,A*D[p])
        if Ta[p]>maxTa:
            maxTa = Ta[p]

def main():
    _,Decomp = sieve_decomp(N+1)
    for i in xrange(2,10):
        fusion_decomp(Decomp[i])
    S = 0
    for i in xrange(10,N+1):
        fusion_decomp(Decomp[i])
        S = (S+maxTa)%M
    print S

main()
