#!/usr/bin/env python

import sys

nbS = 0
A = []

def decomp(n):
    if n==0:
        return []
    if n==1:
        return [(1,1,1)]
    r = int(n**(1./3.))
    r0 = r
    while r0*r*r<=n:
        r0 += 1
    r0 -= 1
    res = decomp(n-r0*r*r)
    res.append((r0,r,r))
    return res
    
def cyclepoilu(Q,L):
    global nbS
    u0 = nbS+1
    s = 3*(Q-2)
    for i in xrange(s):
        nbS += 1
        A.append((u0+i,u0+(i+1)%s))
    d = 0
    while d<Q-2 and L!=[]:
        B1,B2,B3 = L.pop()
        for i in xrange(B1):
            nbS += 1
            A.append((u0+d,nbS))
        for i in xrange(B2):
            nbS += 1
            A.append((u0+d+Q-2,nbS))
        for i in xrange(B3):
            nbS += 1
            A.append((u0+d+2*(Q-2),nbS))
        d += 1

def b3(n):
    return n*(n-1)*(n-2)/6
        
def etoile(B):
    global nbS
    nbS += 1
    u0 = nbS
    for i in xrange(B):
        nbS += 1
        A.append((u0,nbS))
        
def main():
    P,Q = map(int,sys.stdin.readline().split())
    if Q==2:
        while P>0:
            b = 3
            while P>=b3(b):
                b += 1
            b -= 1
            etoile(b)
            P -= b3(b)
    else:
        dP = decomp(P)
        while dP!=[]:
            cyclepoilu(Q,dP)
    print nbS,len(A)
    for x,y in A:
        print x,y

main()
