#!/usr/bin/env python3

from math import sqrt

# 0<=A<=B, B-A = D, A*B = P
# A^2 + DA - P = 0
# Delta = D^2+4P

def solve(D,P):
    if D<0:
        return 0
    if P==0 and D==0:  # (0,0)
        return 1
    if P==0:  # {0, +/-D}
        return 4
    if D==0:
        if P>0:
            p = round(sqrt(P))
            if p*p==P:  # (p,p) & (-p,-p)
                return 2
        return 0
    Delta = D*D+4*P
    if Delta>=0:
        delta = round(sqrt(Delta))
        if delta*delta==Delta and (-D+delta)%2==0:
            a = (-D+delta)//2
            if a!=0 and P%a==0:
                b = P//a
                return len({(a,b),(b,a),(-a,-b),(-b,-a)})
    return 0

def main():
    T = int(input())
    for _ in range(T):
        D,P = map(int,input().split())
        print(solve(D,P))

main()
