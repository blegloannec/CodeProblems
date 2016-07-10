#!/usr/bin/env python

from math import sqrt

# solution obtenue en ligne droite en depliant le cuboid
# x0 = xy/(y+z) sinon
# (bien symetrique en y/z car xz/(y+z) conduirait au meme d)
# d^2 = x^2 + (y+z)^2
# cette route est la bonne (parmi les 3 candidats)
# ssi x est la plus grande des 3 dimensions
# par symetrie, on ne considerera que ce cas dans l'enumeration

def sqr(n):
    s = int(sqrt(n))
    return s*s==n

def main():
    M = 10**6
    cpt = 0
    x = 1
    while cpt<=M:
        for yz in xrange(2,2*x+1):
            # compter les decompositions yz = y+z
            # avec y<=x et z<=x
            if sqr(x*x+yz*yz):
                cpt += yz/2 if yz<=x else x-(yz+1)/2+1
        x += 1
    print x-1

main()
