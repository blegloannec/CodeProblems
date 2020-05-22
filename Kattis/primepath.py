#!/usr/bin/env python3

from collections import deque

S = 4

def sieve(N=10**S):
    P = [True]*N
    for i in range(2,N):
        if P[i]:
            for k in range(i*i,N,i):
                P[k] = False
    return P

def bfs(p, q):
    D = [-1]*10**S
    Q = deque([p])
    D[p] = 0
    while Q:
        u = Q.popleft()
        if u==q:
            break
        for v in G[u]:
            if D[v]<0:
                D[v] = D[u]+1
                Q.append(v)
    return D[q]

def main():
    global G
    P = sieve()
    G = [[] for _ in range(10**S)]
    for p in range(10**(S-1),10**S):
        if P[p]:
            p10 = 1
            for k in range(S):
                c = (p//p10)%10
                for d in range((1 if p10==0 else 0), 10):
                    if d!=c:
                        q = p + (d-c)*p10
                        if P[q]:
                            G[p].append(q)
                p10 *= 10
    T = int(input())
    for _ in range(T):
        p,q = map(int,input().split())
        d = bfs(p,q)
        print(d if d>=0 else 'Impossible')

main()
