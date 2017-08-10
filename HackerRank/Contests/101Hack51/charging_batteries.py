#!/usr/bin/env python3

from math import atan2

def angle(A):
    return atan2(A[1]-n/2,A[0]-n/2)

def dist(A,B):
    return abs(A[0]-B[0])+abs(A[1]-B[1])

def main():
    global n
    n,m,k = map(int,input().split())
    P = sorted((tuple(map(int,input().split())) for _ in range(m)), key=angle)
    d = 0
    dmin = float('inf')
    for i in range(m+k):
        d += dist(P[i%m],P[(i+1)%m])
        if i>k-2:
            d -= dist(P[(i-(k-1))%m],P[(i-(k-2))%m])
        if i>=k-2:
            dmin = min(dmin,d)
    print(dmin)
    
main()
