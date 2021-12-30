#!/usr/bin/env python3

def find(T,x):
    if T[x]<0:
        return x
    T[x] = find(T,T[x])
    return T[x]

def union(T,x,y):
    x0,y0 = find(T,x),find(T,y)
    if x0!=y0:
        T[y0] = x0

def kruskal(N,E):
    T = [-1]*(N+1)
    E.sort(key=(lambda x: x[2]))
    MST = []
    C = N
    i = W = 0
    while C>1:
        u,v,w = E[i]
        if find(T,u)!=find(T,v):
            union(T,u,v)
            C -= 1
            W += w
            MST.append(E[i])
        i += 1
    MST.sort()
    return W,MST

def main():
    N,M = map(int,input().split())
    E = [tuple(map(int,input().split())) for _ in range(M)]
    W,MST = kruskal(N,E)
    print(len(MST),W)
    for e in MST:
        print(*e)

main()
