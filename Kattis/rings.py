#!/usr/bin/env python3

import sys
input = sys.stdin.readline

def find(Repr, x):
    if Repr[x] is None:
        return x
    Repr[x] = find(Repr, Repr[x])
    return Repr[x]

def union(Repr, Size, x, y):
    x0 = find(Repr, x)
    y0 = find(Repr, y)
    if x0!=y0:
        Repr[y0] = x0
        Size[x0] += Size[y0]

def circ_intersect(C1, C2):
    x1,y1,r1 = C1
    x2,y2,r2 = C2
    d2 = (x1-x2)**2 + (y1-y2)**2
    return (r1-r2)**2 < d2 < (r1+r2)**2

def main():
    while True:
        N = int(input())
        if N<0:
            break
        if N==0:
            res = 0
        else:
            C = [tuple(map(float, input().split())) for _ in range(N)]
            Repr = [None]*N
            Size = [1]*N
            for i in range(N):
                for j in range(i+1,N):
                    if circ_intersect(C[i], C[j]):
                        union(Repr, Size, i, j)
            res = max(Size)
        sys.stdout.write(f'The largest component contains {res} ring{"" if res==1 else "s"}.\n')

main()
