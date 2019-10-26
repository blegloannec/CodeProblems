#!/usr/bin/env python3

def cross(A,B,C):
    return (B[0]-A[0])*(C[1]-A[1]) - (B[1]-A[1])*(C[0]-A[0])

def area(P):
    a = 0.
    for i in range(1,len(P)-1):
        a += cross(P[0],P[i],P[i+1])
    return a/2.

def main():
    N = int(input())
    P = [tuple(map(float,input().split())) for _ in range(N)]
    A = float(input())
    a = (A/area(P))**0.5
    P = [(a*x,a*y) for x,y in P]
    xmin = min(x for x,_ in P)
    ymin = min(y for _,y in P)
    P = [(x-xmin,y-ymin) for x,y in P]
    for p in P:
        print(*p)

main()
