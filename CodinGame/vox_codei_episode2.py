#!/usr/bin/env python3

from heapq import *
from collections import defaultdict

Radius = 3
Delay = 2
Dirs = [(-1,0),(1,0),(0,-1),(0,1)]

def targ_at_time(n,t):
    return TCycle[n][t%len(TCycle[n])]

def precomp_positions(r0, rounds):
    global TPos
    R = r0+rounds+1
    TPos = [defaultdict(list) for _ in range(R)]
    for d in range(r0,R):
        for t in range(NbTargets):
            i,j = targ_at_time(t,d+Delay+1)
            TPos[d][i,j].append(t)
            for dx,dy in Dirs:
                x,y,r = i+dx,j+dy,1
                while r<=Radius and 0<=x<H and 0<=y<W and Grid[x][y]!='#':
                    TPos[d][x,y].append(t)
                    x,y,r = x+dx,y+dy,r+1
                    
def dfs(t0, bombs, rounds):
    u0 = (t0, bombs, tuple(range(NbTargets)), (), ())
    Q = [u0]
    Pred = {}
    while Q:
        u = Q.pop()
        d, b, RemTargs, PendBombs, PendTargs = u
        if not RemTargs:
            break
        if b==0 or d==rounds-Delay:
            continue
        PendB1 = [(p,t-1) for p,t in PendBombs if t!=1]
        PendT1 = [(p,t-1) for p,t in PendTargs if t!=1]
        # Waiting (time d+1)
        vwait = (d+1, b, RemTargs, tuple(PendB1), tuple(PendT1))
        if vwait not in Pred:
            Pred[vwait] = (u,'WAIT')
            Q.append(vwait)
        # Candidate positions at time d
        Pos = {}
        for p in TPos[d]:
            L = [t for t in TPos[d][p] if t in RemTargs]
            if L:
                Pos[p] = L
        # Placing one bomb at time d
        Occupied = [targ_at_time(t,d) for t in RemTargs] + [p for p,_ in PendBombs] + [targ_at_time(p,d) for p,_ in PendTargs]
        Avail = sorted((p for p in Pos if p not in Occupied), key=(lambda p: len(Pos[p])))
        for p in Avail:
            in_bomb_radius = False
            for q,_ in PendBombs:
                if q[0]==p[0] or q[1]==p[1]:
                    if abs(q[0]-p[0])+abs(q[1]-p[1])<=Radius:
                        in_bomb_radius = True
                        break
            if not in_bomb_radius:
                PendBv = tuple(PendB1 + [(p,Delay)])
                PendTv = tuple(PendT1 + [(i,Delay) for i in Pos[p]])
                RemTv = tuple(i for i in RemTargs if i not in Pos[p])
                v = (d+1, b-1, RemTv, PendBv, PendTv)
                if v not in Pred:
                    Pred[v] = (u, '%d %d' % p[::-1])
                    Q.append(v)
    # Extracting final plan
    Plan = []
    while u in Pred:
        u,x = Pred[u]
        Plan.append(x)
    Plan.reverse()
    return Plan

def dijkstra_fewest_bombs(t0, bombs, Targs0, rounds):
    u0 = (0, t0, Targs0, (), ())
    Q = [u0]
    Pred = {}
    while Q:
        u = heappop(Q)
        b, d, RemTargs, PendBombs, PendTargs = u
        if not RemTargs:
            break
        if b==bombs or d==rounds-Delay:
            continue
        PendB1 = [(p,t-1) for p,t in PendBombs if t!=1]
        PendT1 = [(p,t-1) for p,t in PendTargs if t!=1]
        # Waiting (time d+1)
        vwait = (b, d+1, RemTargs, tuple(PendB1), tuple(PendT1))
        if vwait not in Pred:
            Pred[vwait] = (u,'WAIT')
            heappush(Q,vwait)
        # Candidate positions for bombs at time d
        Pos = {}
        for p in TPos[d]:
            L = [t for t in TPos[d][p] if t in RemTargs]
            if L:
                Pos[p] = L
        # Placing one bomb at time d
        Occupied = [targ_at_time(t,d) for t in RemTargs] + [p for p,_ in PendBombs] + [targ_at_time(p,d) for p,_ in PendTargs]
        Avail = [p for p in Pos if p not in Occupied]
        for p in Avail:
            in_bomb_radius = False
            for q,_ in PendBombs:
                if q[0]==p[0] or q[1]==p[1]:
                    if abs(q[0]-p[0])+abs(q[1]-p[1])<=Radius:
                        in_bomb_radius = True
                        break
            if not in_bomb_radius:
                PendBv = tuple(PendB1 + [(p,Delay)])
                PendTv = tuple(PendT1 + [(i,Delay) for i in Pos[p]])
                RemTv = tuple(i for i in RemTargs if i not in Pos[p])
                v = (b+1, d+1, RemTv, PendBv, PendTv)
                if v not in Pred:
                    Pred[v] = (u, '%d %d' % p[::-1])
                    heappush(Q,v)
    # Extracting final plan
    Plan = []
    while u in Pred:
        u,x = Pred[u]
        Plan.append(x)
    Plan.reverse()
    return Plan

def components():
    global TComp
    Comp = [[None]*W for _ in range(H)]
    C = 0
    for i,j in MovingTargets + [(i,j) for i in range(H) for j in range(W)]:
        if Grid[i][j]=='.' and Comp[i][j] is None and (i,j) not in FixedTargets:
            Comp[i][j] = C
            Q = [(i,j)]
            while Q:
                x,y = Q.pop()
                target = (x,y) in FixedTargets
                for vx,vy in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                    if 0<=vx<H and 0<=vy<W and Grid[vx][vy]=='.' and Comp[vx][vy] is None and (not target or (vx,vy) in FixedTargets):
                        Comp[vx][vy] = C
                        Q.append((vx,vy))
            C += 1
    TComp = defaultdict(list)
    for k,(x,y) in enumerate(Targets):
        TComp[Comp[x][y]].append(k)
    TComp = [TComp[c] for c in TComp]

def cycle(i,j,di,dj):
    c = 0
    C = []
    vi,vj = i,j
    while c!=2:
        C.append((vi,vj))
        if not 0<=vi+di<H or not 0<=vj+dj<W or Grid[vi+di][vj+dj]=='#':
            di,dj = -di,-dj
        vi,vj = vi+di,vj+dj
        if (vi,vj)==(i,j):
            c += 1
    return C

def main():
    global W, H, Grid, Targets, NbTargets, TCycle, FixedTargets, MovingTargets
    W,H = map(int,input().split())
    # game loop
    ready = False
    t = c = 0
    Plan = TCycle = None
    while True:
        # rounds: number of rounds left before the end of the game
        # bombs: number of bombs left
        rounds,bombs = map(int,input().split())
        if t==0:  # first turn
            Grid = [list(input()) for _ in range(H)]
            Targets = []
            for i in range(H):
                for j in range(W):
                    if Grid[i][j]=='@':
                        Targets.append((i,j))
                        Grid[i][j] = '.'
            NbTargets = len(Targets)
            print('WAIT')
        elif not ready:  # we are still figuring what moves and how
            if TCycle is None:  # init
                TCycle = [[[(i,j)]]+[cycle(i,j,di,dj) for di,dj in Dirs if 0<=i+di<H and 0<=j+dj<W and Grid[i+di][j+dj]=='.'] for i,j in Targets]
            Grid1 = [input() for _ in range(H)]  # checking/updating info
            for k in range(NbTargets):
                C = []
                for L in TCycle[k]:
                    x,y = L[t%len(L)]
                    if Grid1[x][y]=='@':
                        C.append(L)
                TCycle[k] = C
            if all(len(C)==1 for C in TCycle):  # we know the cycles!
                TCycle = [C[0] for C in TCycle]
                ready = True
                FixedTargets = [Targets[p] for p in range(NbTargets) if len(TCycle[p])==1]
                MovingTargets = [Targets[p] for p in range(NbTargets) if len(TCycle[p])>1]
                # we precomp the potential bomb positions at each time
                precomp_positions(t,rounds)
                # we compute the components
                components()
            print('WAIT')
        else:
            if Plan is None and c<len(TComp):
                t0 = t
                if len(TComp)<=3:  # Case 1: Ignore components when there are too few of them
                    Plan = dfs(t0,bombs,rounds)
                    c = len(TComp)
                else:              # Case 2: Planning each component independently, minimizing bombs
                    Plan = dijkstra_fewest_bombs(t0, bombs, tuple(TComp[c]), rounds)
                    c += 1
            for _ in range(H):     # reading (and throwing away) the current grid
                input()
            if Plan is not None and t-t0<len(Plan):
                print(Plan[t-t0])
            else:
                Plan = None
                print('WAIT')
        t += 1

main()
