#!/usr/bin/env python3

import sys

def find(x):
    if T[x]<0:
        return x
    T[x] = find(T[x])
    return T[x]

def union(x,y):
    T[find(y)] = find(x)

def main():
    global T
    W,H = map(int,input().split())
    T = [-1]*(W*H)
    Seen = [False]*(W*H)
    b,e = 0,W*H-1
    Seen[b] = Seen[e] = True
    L = sys.stdin.readlines()
    i = 0
    while find(b)!=find(e):
        x,y = map(int,L[i].split())
        u = H*x+y
        Seen[u] = True
        for (vx,vy) in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            if 0<=vx<W and 0<=vy<H:
                v = H*vx+vy
                if Seen[v] and find(u)!=find(v):
                    union(u,v)
        i += 1
    print(i)

main()
