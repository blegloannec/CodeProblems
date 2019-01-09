#!/usr/bin/env python3

import sys
sys.setrecursionlimit(5000)

def depth(T,Depth,u=1,d=1):
    if u>0:
        Depth[u] = d
        depth(T,Depth,T[u][0],d+1)
        depth(T,Depth,T[u][1],d+1)

def traversal(T,Trace,u=1):
    if u>0:
        traversal(T,Trace,T[u][0])
        Trace.append(u)
        traversal(T,Trace,T[u][1])

def main():
    n = int(input())
    T = [(0,0)]+[tuple(map(int,input().split())) for _ in range(n)]
    q = int(input())
    Depth = [0]*(n+1)
    depth(T,Depth)
    for _ in range(q):
        k = int(input())
        T = [(b,a) if Depth[i]>0 and Depth[i]%k==0 else (a,b) for i,(a,b) in enumerate(T)]
        Trace = []
        traversal(T,Trace)
        print(*Trace)

main()
