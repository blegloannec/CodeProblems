#!/usr/bin/env python3

from collections import defaultdict

Radius = 3
Delay = 2

def dfs(rounds, bombs):
    u0 = (bombs, tuple(range(len(Targets))), ())
    Dist = {u0: 0}
    Pred = {}
    Q = [u0]
    while Q:
        u = Q.pop()
        b,T,Pending = u
        if not T:
            break
        if b==0 or Dist[u]==rounds:
            continue
        Pend1 = [(p,t-1) for p,t in Pending if t!=1]
        if Pending:
            v = (b, T, tuple(Pend1))
            if v not in Dist:
                Dist[v] = Dist[u]+1
                Pred[v] = (u,'WAIT')
                Q.append(v)
        Pos = defaultdict(list)
        for t in T:
            i,j = Targets[t]
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                x,y,r = i+dx,j+dy,1
                while r<=Radius and 0<=x<H and 0<=y<W and Grid[x][y]!='#':
                    Pos[x,y].append(t)
                    x,y,r = x+dx,y+dy,r+1
        Occupied = [Targets[t] for t in T] + [p for p,_ in Pending]
        Avail = sorted((p for p in Pos if p not in Occupied), key=(lambda p: len(Pos[p])))
        for p in Avail:
            Pendv = tuple(Pend1 + [(p,Delay)] + [(Targets[i],Delay) for i in Pos[p]])
            v = (b-1, tuple(i for i in T if i not in Pos[p]), Pendv)
            if v not in Dist:
                Dist[v] = Dist[u]+1
                x,y = p
                Pred[v] = (u, '%d %d' % (y,x))
                Q.append(v)
    Plan = []
    while u in Pred:
        u,x = Pred[u]
        Plan.append(x)
    Plan.reverse()
    return Plan

def main():
    global W,H,Grid,Targets
    W,H = map(int,input().split())
    Grid = [list(input()) for _ in range(H)]
    Targets = []
    for i in range(H):
        for j in range(W):
            if Grid[i][j]=='@':
                Targets.append((i,j))
                Grid[i][j] = '.'
    # game loop
    t = 0
    Plan = None
    while True:
        # rounds: number of rounds left before the end of the game
        # bombs: number of bombs left
        rounds,bombs = map(int,input().split())
        if Plan is None:
            Plan = dfs(rounds,bombs)
        print(Plan[t] if t<len(Plan) else 'WAIT')
        t += 1

main()
