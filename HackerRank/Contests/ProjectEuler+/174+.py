#!/usr/bin/env python

from collections import defaultdict

def main():
    M = 10**6
    D = defaultdict(int)
    a = 3
    while a*a-(a-2)*(a-2)<=M:
        for b in xrange(a-2,0,-2):
            n = a*a-b*b
            if n>M:
                break
            D[n] += 1
        a += 1
    Cpt = [0 for _ in xrange(M+1)]
    for n in xrange(1,M+1):
        Cpt[n] += Cpt[n-1]
        if 0<D[n]<=10:
            Cpt[n] += 1
    T = int(input())
    for _ in xrange(T):
        print Cpt[int(input())]

main()
