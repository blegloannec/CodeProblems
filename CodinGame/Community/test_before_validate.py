#!/usr/bin/env python3

from heapq import *

# topological sort with priority queue for "stability"
# "If multiple actions can be done at the same time,
# choose the one that appears first in the initial order."
# G is assumed to be a DAG
def topo_sort(G):
    N = len(G)
    Pred = [0]*N
    for u in range(N):
        for v in G[u]:
            Pred[v] += 1
    H = [u for u in range(N) if Pred[u]==0]
    #heapify(H)  # already a heap
    O = []
    while H:
        u = heappop(H)
        O.append(u)
        for v in G[u]:
            Pred[v] -= 1
            if Pred[v]==0:
                heappush(H,v)
    return O

def main():
    N = int(input())
    A = [input() for _ in range(N)]
    Num = {A[i]:i for i in range(N)}
    M = int(input())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a,p,b = input().split()
        if p=='after':
            a,b = b,a
        G[Num[a]].append(Num[b])
    for o in topo_sort(G):
        print(A[o])

main()
