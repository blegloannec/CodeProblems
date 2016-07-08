#!/usr/bin/env python

import sys

P = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107]

def loop(p=0,amax=10,n=1,nbdiv=1):
    if p<len(P):
        for a in xrange(1,amax+1):
            n *= P[p]
            nb = nbdiv*(2*a+1)
            if nb>=nblim:
                yield n
                break
            else:
                for x in loop(p+1,a,n,nb):
                    yield x

def main():
    global nblim
    X = int(sys.stdin.readline())
    nblim = 2*(X-1)+1
    print min(loop())

main()
