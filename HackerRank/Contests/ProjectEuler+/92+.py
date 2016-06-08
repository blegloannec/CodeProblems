#!/usr/bin/env python

import sys

# si n < 10^K
# alors succ(n) <= K*9^2 <= 16200 pour K <= 200

def succ(n):
    s = 0
    while n>0:
        c = n%10
        s += c*c
        n /= 10
    return s

def chain(x):
    if X[x]>0:
        return X[x]
    x0 = chain(succ(x))
    X[x] = x0
    return x0

NMAX = 201
XMAX = 16201
M = 1000000007

# P(n,x) le nb de nb a n chiffres dont le successeur
# vaut x
# P(n,x) = sum( P(n-1,x-a^2), a=0..9 )
# pourrait etre ameliore en "triant" les chiffres et
# en multipliant par les bons coeff binomiaux, mais
# cette progdyn est suffisante
def progdyn():
    P = [[0 for _ in xrange(XMAX)] for _ in xrange(NMAX)]
    P[0][0] = 1
    for n in xrange(1,NMAX):
        for x in xrange(XMAX):
            for a in xrange(10):
                if x<a*a:
                    break
                P[n][x] = (P[n][x]+P[n-1][x-a*a])%M
    return P
            
def main():
    global NMAX,XMAX,X
    K = int(sys.stdin.readline())
    NMAX = K+1
    XMAX = max(300,81*K+1)
    X = [0 for _ in xrange(XMAX)]
    X[1] = 1
    X[89] = 89
    for i in xrange(1,XMAX):
        chain(i)
    P = progdyn()
    cpt = 0
    for i in xrange(XMAX):
        if X[i]==89:
            cpt = (cpt+P[K][i])%M
    print cpt

main()
