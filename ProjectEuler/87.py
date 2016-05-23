#!/usr/bin/env python

from math import sqrt

def eratosthene(n):
    l = range(2,n+1)
    s = int(sqrt(n))+1
    for i in range(2,s):
        for k in range(2*i,n+1,i):
            l[k-2] = -1
    return filter((lambda x: x>0),l)

def main():
    P = eratosthene(100000)
    M = 50000000
    S = set()
    for a in P:
        A = a*a
        if A>=M:
            break
        for b in P:
            B = b*b*b
            if A+B>=M:
                break
            for c in P:
                X = A+B+c*c*c*c
                if X<M:
                    S.add(X)
                else:
                    break
    print len(S)

main()
