#!/usr/bin/env python3

import sys
from fractions import Fraction

def randgen(N):
    s = 290797
    T = []
    for _ in range(4*N):
        s = (s*s)%50515093
        T.append(s%500)
    return T

def true_intersection(A,B):
    x1,y1,x2,y2 = A
    x3,y3,x4,y4 = B
    a,b,e = x2-x1,-(x4-x3),x3-x1
    c,d,f = y2-y1,-(y4-y3),y3-y1
    det = a*d-b*c
    if det==0:
        return None
    # Cramer
    t,tp = e*d-b*f,a*f-e*c
    if det<0:
        det = -det
        t = -t
        tp = -tp
    if 0<t<det and 0<tp<det:
        t,tp = Fraction(t,det),Fraction(tp,det)
        return (x1+t*a,y1+t*c)
    return None

def main():
    N = int(sys.stdin.readline())
    T = randgen(N)
    P = set()
    for a in range(N):
        A = T[4*a:4*a+4]
        for b in range(a+1,N):
            B = T[4*b:4*b+4]
            I = true_intersection(A,B)
            if I!=None:
                P.add(I)
    print(len(P))

main()
