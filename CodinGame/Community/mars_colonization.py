#!/usr/bin/env python3

from math import sqrt

def find(T,u):
    if T[u] is None:
        return u
    T[u] = find(T,T[u])
    return T[u]

def main():
    M,S = map(int,input().split())
    P = [tuple(map(int,input().split())) for _ in range(M)]
    dist2 = lambda x1,y1: lambda x2,y2: (x1-x2)**2 + (y1-y2)**2
    E = []
    for i in range(M):
        di = dist2(*P[i])
        for j in range(i+1,M):
            E.append((di(*P[j]),i,j))
    E.sort()
    T = [None]*M
    C = M
    for d,u,v in E:
        u0 = find(T,u)
        v0 = find(T,v)
        if u0!=v0:
            T[v0] = u0  # union
            C -= 1
            if C==S:
                break
    print('%.2f' % round(sqrt(d),2))

main()
