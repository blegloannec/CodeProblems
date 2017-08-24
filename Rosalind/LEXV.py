#!/usr/bin/env python3

from itertools import product

A = input().split()
n = int(input())

## lazy hack over itertools
def main0():
    S0 = '   '
    for P in product(A,repeat=n):
        S = ''.join(P)
        d = 0
        while d<n and S[d]==S0[d]:
            d += 1
        for i in range(d+1,n):
            print(S[:i])
        print(S)
        S0 = S

#main0()

## custom recursion (actually simpler)
def nest(S):
    if len(S)<n:
        for a in A:
            S.append(a)
            yield ''.join(S)
            yield from nest(S)
            S.pop()

def main1():
    for S in nest([]):
        print(S)

main1()
