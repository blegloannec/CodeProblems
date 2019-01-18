#!/usr/bin/env python3

H = int(input())
N = int(input())
G = [list(map(int,input().split())) for _ in range(N)]

C = max_size = depth = 0
Comp = {}
for ui in range(N):
    for uj in range(N):
        if G[ui][uj]<H and (ui,uj) not in Comp:
            Comp[ui,uj] = C
            C += 1
            CurrCompo = [(ui,uj)]
            Q = [(ui,uj)]
            while Q:
                vi,vj = Q.pop()
                for wi,wj in [(vi-1,vj),(vi+1,vj),(vi,vj-1),(vi,vj+1)]:
                    if 0<=wi<N and 0<=wj<N and G[wi][wj]<=H and (wi,wj) not in Comp:
                        Comp[wi,wj] = Comp[vi,vj]
                        CurrCompo.append((wi,wj))
                        Q.append((wi,wj))
            if len(CurrCompo)>max_size:
                max_size = len(CurrCompo)
                depth = min(G[x][y] for x,y in CurrCompo)
            elif len(CurrCompo)==max_size:
                depth = min(depth,min(G[x][y] for x,y in CurrCompo))
print(depth)
