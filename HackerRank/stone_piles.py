#!/usr/bin/env python

import sys

# partitions de l'entier n en k morceaux
# sans doublon interne (ie jamais 2 composantes de meme taille)
def partitions(n,k):
    if k==1:
        yield [n]
    elif k<=n:
        for p in partitions(n-1,k-1):
            if p[-1]!=1:
                p.append(1)
                yield p
        for p in partitions(n-k,k):
            for i in xrange(k):
                p[i] += 1
            yield p

def mex(succ):
    i = 0
    while i in succ:
        i += 1
    return i

G = [-1 for _ in xrange(51)]
def grundy(n):
    if G[n]>=0:
        return G[n]
    succ = set()
    for k in xrange(2,n+1):
        for p in partitions(n,k):
            v = 0
            for x in p:
                v ^= grundy(x)
            succ.add(v)
    g = mex(succ)
    G[n] = g
    return g

def main():
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        N = int(sys.stdin.readline())
        X = map(int,sys.stdin.readline().split())
        if reduce((lambda x,y: x^y),map(grundy,X))==0:
            print 'BOB'
        else:
            print 'ALICE'

main()
