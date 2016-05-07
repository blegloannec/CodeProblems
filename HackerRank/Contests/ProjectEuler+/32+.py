#!/usr/bin/env python

import sys

def pandigitprod(a,b,N):
    D = [False for _ in xrange(10)]
    D[0] = True
    for i in xrange(N+1,10):
        D[i] = True
    C = 0
    n = a
    while n>0:
        c = n%10
        if D[c]:
            return False
        D[c] = True
        C += 1
        n /= 10
    n = b
    while n>0:
        c = n%10
        if D[c]:
            return False
        D[c] = True
        C += 1
        n /= 10
    n = a*b
    while n>0:
        c = n%10
        if D[c]:
            return False
        D[c] = True
        C += 1
        n /= 10
    return C==N

bornes = {4: [((1,10),(1,10))],
          5: [((1,10),(1,100))],
          6: [((1,100),(1,100))],
          7: [((1,100),(1,100))],
          8: [((1,100),(1,1000))],
          9: [((1,10),(1000,10000)),((10,100),(100,1000))]}

def main():
    N = int(sys.stdin.readline())
    S = set()
    s = 0
    for ((i0,i1),(j0,j1)) in bornes[N]:
        for i in xrange(i0,i1):
            for j in xrange(j0,j1):
                if (i*j not in S) and pandigitprod(i,j,N):
                    s += i*j
                    S.add(i*j)
    print s

main()
