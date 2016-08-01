#!/usr/bin/env python

from collections import defaultdict
from math import sqrt

# seul 1 est repunit d'ordre 1 (dans toutes les bases)
# n est toujours un repunit d'ordre 2 (s'écrit 11)
# en base n-1 (car il s'ecrit 11)
# si n<N est un strong repunit, alors il est aussi repunit
# d'ordre >=3 dans une base B, donc B^2+B+1<N, a fortiori B<sqrt(N)

# repunits <N dans la base B
def genrep(B,N):
    r = 1
    while r<N:
        yield r
        r = B*r+1

def main():
    N = 10**12
    S = int(sqrt(N))
    D = defaultdict(int)
    for B in xrange(2,S+1):
        for r in genrep(B,N):
            D[r] += 1
    s = 0
    for r in D:
        if r>S+1 or D[r]>1:
            s += r
    print s

main()
