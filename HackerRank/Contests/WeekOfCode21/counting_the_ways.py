#!/usr/bin/env python

import sys
from fractions import gcd

# References :
# [1] http://mathoverflow.net/questions/61329/counting-and-summing-over-solutions-of-a-diophantine-equation
# [2] https://en.wikipedia.org/wiki/Ehrhart_polynomial
# [3] http://math.stackexchange.com/questions/30638/count-the-number-of-positive-solutions-for-a-linear-diophantine-equation

# Il s'agit du probleme classique du rendu de monnaie
# dont on veut compter les solutions.
# L'approche classique de prog dyn n'est evidemment pas
# assez efficace pour de grandes instances.
# Il faut ici est en savoir plus sur la forme des solutions.
# Tout d'abord, a N fixe, il s'agit de compter le nombre de solutions
# de l'equation diophantienne lineaire a1*x1 + ... + an*xn = N

# D'apres [1], ce nombre de solutions est le denumerant de Sylvester
# d(N;a1,...,an)...

# Par ailleurs, ce nombre de solutions peut etre vu comme le nombre
# de points entiers sur la frontiere d'un polytope convexe de dimension n.
# Cela peut etre calcule a l'aide d'un polynome de Ehrhart [2] de degre n.
# Le theoreme de Pick est le plus simple exemple de tel calcul en
# (dimension 2 dans le cas d'un triangle, i.e. 3 sommets).

# Suivons l'analyse de [3]...


# Tout (DP, interpolation, etc) sera fait modulo M premier
M = 10**9+7

def lcm(a,b):
    return a*b/gcd(a,b)

def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a/b)*v)

def inv_mod(a,n):
    _,u,_ = bezout(a,n)
    return u

# Interpolation de Lagrange pour les points
# (0,P[0]), (1,P[1]), ...
def lagrange(P,x0):
    if x0<len(P):
        return P[x0]
    y0 = 0
    for xi in xrange(len(P)):
        pi = P[xi]
        for xj in xrange(len(P)):
            if xj!=xi:
                pi = (pi*(x0-xj)*inv_mod(xi-xj,M))%M
        y0 += pi
    return y0

# Somme des termes <=n par somme des sommes des termes egaux modulo B
# calcules par interpolation
def F(n):
    res = 0
    for r in xrange(min(n+1,B)):
        res = (res + lagrange(C[r],(n-r)/B))%M
    return res

def main():
    global N,A,B,C
    N = int(sys.stdin.readline())
    A = map(int,sys.stdin.readline().split())
    L,R = map(int,sys.stdin.readline().split())
    B = reduce(lcm,A)
    # Prog. dyn. pour "petites valeurs"
    P = [int(n==0) for n in xrange((N+2)*B)]
    P[0] = 1
    for k in xrange(N):
        for n in xrange((N+2)*B):
            if n>=A[k]:
                P[n] = (P[n] + P[n-A[k]])%M
    # Premiers points des B polynomes pour interpolation
    C = [[0 for _ in xrange(N+2)] for _ in xrange(B)]
    for r in xrange(B):
        C[r][0] = P[r]
        for i in xrange(1,N+2):
            C[r][i] = (C[r][i-1] + P[i*B+r])%M
    # Resultat
    print (F(R)-F(L-1))%M

main()
