#!/usr/bin/env python3

from collections import *

def bfs(G,u0,uf):
    Q = deque([u0])
    Pred = {u0:None}
    while Q:
        u = Q.popleft()
        if u==uf:
            break
        for v,p in G[u]:
            if v not in Pred:
                Pred[v] = (u,p)
                Q.append(v)
    if uf not in Pred:
        return None
    Pub = []
    u = uf
    while Pred[u]!=None:
        u,p = Pred[u]
        Pub.append(p)
    return Pub[::-1]

def main():
    scientist = input()
    N = int(input())
    Title = [input() for _ in range(N)]
    G = defaultdict(list)
    for p in range(N):
        A = input().split()
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                G[A[i]].append((A[j],p))
                G[A[j]].append((A[i],p))
    Pub = bfs(G,scientist,'Erdős')
    if Pub is None:
        print('infinite')
    else:
        print(len(Pub))
        for p in Pub:
            print(Title[p])

main()
