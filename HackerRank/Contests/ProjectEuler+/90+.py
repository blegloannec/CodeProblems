#!/usr/bin/env python

import sys

# naive solution (brute-force on all possible dice)

def parmi(n,p):
    if p==0:
        yield []
    else:
        for i in xrange(p-1,n):
            for S in parmi(i,p-1):
                S.append(i)
                yield S

def f69(c):
    return 6 if c==9 else c

def CinD(c,D):
    res = c in D
    if c==6:
        res |= 9 in D
    return res

def test2(S,D1,D2):
    for (a,b) in S:
        if not ((CinD(a,D1) and CinD(b,D2)) or (CinD(b,D1) and CinD(a,D2))):
            return False
    return True

def test3(S,D1,D2,D3):
    for (a,b,c) in S:
        if not ((CinD(a,D1) and CinD(b,D2) and CinD(c,D3)) or (CinD(a,D1) and CinD(c,D2) and CinD(b,D3)) or (CinD(b,D1) and CinD(a,D2) and CinD(c,D3)) or (CinD(b,D1) and CinD(c,D2) and CinD(a,D3)) or (CinD(c,D1) and CinD(a,D2) and CinD(b,D3)) or (CinD(c,D1) and CinD(b,D2) and CinD(a,D3))):
            return False
    return True

def compte2(N):
    S = [(f69((i*i)/10),f69((i*i)%10)) for i in xrange(1,N+1)]
    cpt = 0
    Des = list(parmi(10,6))
    for D1 in Des:
        for D2 in Des:
            if D1<=D2 and test2(S,D1,D2):
                cpt += 1
    return cpt

def compte3(N):
    S = [(f69((i*i)/100),f69(((i*i)/10)%10),f69((i*i)%10)) for i in xrange(1,N+1)]
    cpt = 0
    Des = list(parmi(10,6))
    for D1 in Des:
        for D2 in Des:
            if D2<D1:
                continue
            for D3 in Des:
                if D2<=D3 and test3(S,D1,D2,D3):
                    cpt += 1
    return cpt

def main():
    N,M = map(int,sys.stdin.readline().split())
    if M==1:
        print [126,70,55][N-1]
    elif M==2:
        print compte2(N)
    else:
        print compte3(N)

main()
