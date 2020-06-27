#!/usr/bin/env python3

import sys
input = sys.stdin.readline

def ternary_search(A, B):
    (xa,ya), (xb,yb) = A, B
    mid = lambda l: (l*xa+(1.-l)*xb) * (l*ya+(1.-l)*yb)
    l,r = 0.,1.
    while r-l>1e-4:
        m1 = (2.*l+r)/3.
        m2 = (l+2.*r)/3.
        if mid(m1)<mid(m2):
            l = m1
        else:
            r = m2
    return mid(l)

def left_turn(a,b,c):
    return (a[0]-c[0])*(b[1]-c[1]) - (a[1]-c[1])*(b[0]-c[0]) > 0

def upper_hull(S):
    S.sort()
    top = []
    for p in S:
        while len(top)>=2 and not left_turn(p,top[-1],top[-2]):
            top.pop()
        top.append(p)
    return top

def main():
    N,B = map(int, input().split())
    P = []
    for _ in range(N):
        c,h,p = map(float, input().split())
        k = B/c
        P.append((k*h, k*p))
    P = upper_hull(P)
    res = 0.
    for i in range(len(P)-1):
        res = max(res, ternary_search(P[i],P[i+1]))
    print(res)

main()
