#!/usr/bin/env python3

import sys

def find(T,x):
    if T[x]<0:
        return x
    T[x] = find(T,T[x])
    return T[x]

def union(T,x,y):
    x0 = find(T,x)
    y0 = find(T,y)
    if x0!=y0:
        T[y0] = x0
    return x0!=y0

def main():
    N = int(sys.stdin.readline())
    DescRepr = {}
    T = [-1]*N
    E = []
    for u in range(N):
        C = list(map(int,sys.stdin.readline().split()))
        for i in range(1,C[0]+1):
            if C[i] in DescRepr:
                u0 = DescRepr[C[i]]
                if union(T,u0,u):
                    E.append((u0+1, u+1, C[i]))
            else:
                DescRepr[C[i]] = u
    if len(E)<N-1:
        sys.stdout.write('impossible\n')
    else:
        for e in E:
            sys.stdout.write('%d %d %d\n' % e)

main()
