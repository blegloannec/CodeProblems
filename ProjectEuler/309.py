#!/usr/bin/env python

from fractions import gcd
from math import sqrt

# on pose hx et hy les cotes verticaux des triangles rectangles
# de base w et d'hypotenuses x et y
# on a h = hx*hy / (hx+hy) qui doit etre entier

# runs in < 4s with pypy

# generating prime pythagorean triples
# for c < C, choose N = int(sqrt(C))+1 and filter
def pythagorean(N):
    for m in xrange(2,N):
        n0s = 1+m%2
        for n in xrange(n0s,m,n0s):
            if gcd(m,n)==1:
                a,b,c = m*m-n*n,2*m*n,m*m+n*n
                yield (a,b,c)

def main():
    N = 10**6
    T = [[] for _ in xrange(N)]
    # on genere tous les triangles rectangles d'hypothenuse <N
    for (a,b,c) in pythagorean(int(sqrt(N))+1):
        for i in xrange(1,(N-1)/c+1):
            T[i*a].append((i*b,i*c))
            T[i*b].append((i*a,i*c))
    cpt = 0
    for w in xrange(1,N):
        # on teste toutes les paires de triangles ayant w en commun
        for i in xrange(len(T[w])):
            hx,x = T[w][i]
            for j in xrange(i+1,len(T[w])):
                hy,y = T[w][j]
                if y!=x and (hx*hy)%(hx+hy)==0:
                    cpt += 1
    print cpt

main()
