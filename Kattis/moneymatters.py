#!/usr/bin/env python3

def find(x):
    if T[x]<0:
        return x
    T[x] = find(T[x])
    return T[x]

def union(x, y):
    x0 = find(x)
    y0 = find(y)
    if x0!=y0:
        T[y0] = x0
        S[x0] += S[y0]
        S[y0] = 0

def main():
    global S,T
    N,M = map(int,input().split())
    S = [int(input()) for _ in range(N)]
    T = [-1]*N
    for _ in range(M):
        x,y = map(int,input().split())
        union(x,y)
    possible = all(s==0 for s in S)
    print('POSSIBLE' if possible else 'IMPOSSIBLE')

main()
