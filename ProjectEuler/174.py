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
    N = [0 for _ in xrange(11)]
    for n in D:
        if D[n]<=10:
            N[D[n]] += 1
    print sum(N)

main()
