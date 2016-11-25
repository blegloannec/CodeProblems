#!/usr/bin/env python

from math import sqrt
from fractions import gcd

# cf pb 108, 1/a + 1/b = 1/n <=> x*y = n^2
# pour a = n+x et b = n+y
# quant a l'equation 1/a + 1/b = p/n <=> 1/(p*a) + 1/(p*b) = 1/n
# donc pour chaque solution (a,b) de l'equation pour 1/n
# on peut choisir pour p un diviseur commun de a et b et fabriquer
# l'equation 1/(a/p) + 1/(b/p) = p/n
# par exemple, pour n = 10, on a n^2 = 100 = 2^2*5^2
# on a par exemple la solution (2+10,50+10), 1/12 + 1/60 = 1/10
# gcd(12,60) = 12 = 2^2*3
# on peut prendre p = 2,3,4,6,12 et produire les 5 equations
# 1/6 + 1/30 = 2/10, 1/4 + 1/20 = 3/10, 1/3 + 1/15 = 3/10,
# 1/2 + 1/10 = 6/10, 1/1 + 1/5 = 12/10
# donc le nb de solutions est la somme sur a <= b solution de
# 1/a+1/b = 1/n des nb_diviseurs(gcd(a,b))

def nb_diviseurs(n):
    if n==1:
        return 1
    s = 2
    r = int(sqrt(n))
    if r*r==n: # n is a square
        s += 1
        r -= 1
    for i in xrange(2,r+1):
        if n%i==0:
            s += 2
    return s

# ici le "n" en question est un 10^n = 2^n*5^n
def nb_sol(n):
    N = 10**n
    cpt = 0
    for p2 in xrange(2*n+1):
        for p5 in xrange(2*n+1):
            a = 2**p2 * 5**p5
            if a<=N:
                b = N*N/a
                cpt += nb_diviseurs(gcd(a+N,b+N))
    return cpt

print sum(nb_sol(n) for n in xrange(1,10))
