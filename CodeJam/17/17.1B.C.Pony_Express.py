#!/usr/bin/env python3

from heapq import *

# This code is slightly simplified compared to the submitted one.
# Got a WA on large testcase during contest due to a STUPID floating
# point error: the maximal distance filtering was initially done in terms
# of time, i.e. AFTER dividing distances by speed, which causes critical
# floating point errors...

def floyd_warshall(weight):
    for k in range(len(weight)):
        for u in range(len(weight)):
            for v in range(len(weight)):
                weight[u][v] = min(weight[u][v],weight[u][k]+weight[k][v])

def main():
    T = int(input())
    for t in range(1,T+1):
        N,Q = map(int,input().split())
        E,S = [],[]
        for _ in range(N):
            Ei,Si = map(int,input().split())
            E.append(Ei)
            S.append(Si)
        G = []
        for u in range(N):
            G.append(list(map(int,input().split())))
            for v in range(N):
                if G[u][v]<0:
                    G[u][v] = float('inf')
        floyd_warshall(G)
        for u in range(N):
            for v in range(N): # filtering
                if G[u][v]>E[u]:
                    G[u][v] = float('inf')
                else:
                    # ONLY NOW we can divide by the speed without
                    # getting critical floating point errors!
                    G[u][v] /= S[u]
        floyd_warshall(G)
        res = []
        for _ in range(Q):
            u,v = map(int,input().split())
            res.append(G[u-1][v-1])
        print('Case #%d: %s' % (t,' '.join(map(str,res))))

main()
