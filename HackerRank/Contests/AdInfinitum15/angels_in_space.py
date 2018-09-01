#!/usr/bin/env python

import sys
from math import *

def scal(V1,V2):
    return sum([V1[i]*V2[i] for i in xrange(3)])

def norm(V):
    return sqrt(scal(V,V))

def BON(V1,V2): # Gram-Schmidt
    U1 = map((lambda x: x/norm(V1)),V1)
    U2 = [V2[i]-scal(V2,U1)*U1[i]/scal(U1,U1) for i in xrange(3)]
    U2 = map((lambda x: x/norm(U2)),U2)
    return (U1,U2)

def angle(P1,P2,P3):
    V1 = [P2[i]-P1[i] for i in xrange(3)]
    V2 = [P3[i]-P1[i] for i in xrange(3)]
    U1,U2 = BON(V1,V2) # orthonormal basis
    W1 = [scal(V1,U1),scal(V1,U2)] # projections
    W2 = [scal(V2,U1),scal(V2,U2)] # to the plane
    n1 = sqrt(W1[0]*W1[0]+W1[1]*W1[1])
    n2 = sqrt(W2[0]*W2[0]+W2[1]*W2[1])
    # get angle from its sinus via cross product
    a = asin((W1[0]*W2[1]-W1[1]*W2[0])/(n1*n2))
    # correct angle if cosinus<0 via dot product
    if W1[0]*W2[0]+W1[1]*W2[1]<0:
        a = pi-a
    return a
    
def main():
    T = int(sys.stdin.readline())
    P = []
    for t in xrange(T):
        P.append(map(int,sys.stdin.readline().split()))
    s = 0
    cpt = 0
    for a in xrange(T):
        for b in xrange(a+1,T):
            for c in xrange(b+1,T):
                s += angle(P[b],P[a],P[c])
                cpt += 1
    print s/cpt # mean of the angles

main()
