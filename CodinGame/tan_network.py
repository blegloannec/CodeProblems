#!/usr/bin/env python3

from math import pi,sqrt,cos
from collections import defaultdict
from heapq import *

S = {}
G = defaultdict(list)

def dist(s1,s2):
    la1,lo1 = S[s1][1]
    la2,lo2 = S[s2][1]
    x = (lo2-lo1)*cos((la1+la2)/2.)
    y = la2-la1
    return 6371.*sqrt(x*x+y*y)

def srad(x):
    return pi*float(x)/180.

def dijkstra(s,e):
    D = {s:0.}
    Pred = {s:None}
    H = [(0.,s)]
    while H:
        d,u = heappop(H)
        if u==e:
            break
        if d>D[u]:
            continue
        for (v,w) in G[u]:
            if v not in D or d+w<D[v]:
                D[v] = d+w
                Pred[v] = u
                heappush(H,(D[v],v))
    if e not in D:
        return None
    Path = []
    while e!=s:
        Path.append(e)
        e = Pred[e]
    Path.append(s)
    return Path[::-1]

def main():
    start = input()
    end = input()
    n = int(input())
    for _ in range(n):
        sid,name,_,la,lo,_,_,_,_ = input().split(',')
        S[sid] = (name[1:-1],(srad(la),srad(lo)))
    m = int(input())
    for _ in range(m):
        sidu,sidv = input().split()
        G[sidu].append((sidv,dist(sidu,sidv)))
    Path = dijkstra(start,end)
    if Path==None:
        print('IMPOSSIBLE')
    else:
        print('\n'.join(S[u][0] for u in Path))

main()
