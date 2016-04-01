#!/usr/bin/env python

from math import sqrt

def nb_diviseurs(n):
    s = 2
    r = int(sqrt(n))
    if n%r==0:
        s += 1
    for i in range(2,r):
        if n%i==0:
            s += 2
    return s

def problem12():
    n = 1
    nb = 1
    while nb_diviseurs(nb) < 500:
        n += 1
        nb = n*(n+1)/2
    print nb

problem12()
