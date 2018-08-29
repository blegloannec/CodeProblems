#!/usr/bin/env python3

from collections import deque

L = 4
SMAX = 49

def next_conf(x,s,l):
    if s<SMAX:
        nx = min(x+s+1,W-1)
        yield 'SPEED',(nx,s+1,l&RangeG[x][nx])
    if s>0:
        nx = min(x+s-1,W-1)
        yield 'SLOW',(nx,s-1,l&RangeG[x][nx])
    nx = min(x+s,W-1)
    yield 'JUMP',(nx,s,l&G[nx])
    # WAIT is useless, it is stricly less powerful than jump
    #yield 'WAIT',(nx,s,l&RangeG[x][nx])
    # NB: it is unclear whether UP and DOWN should be allowed at s = 0
    nxm1 = max(0,nx-1)
    if l&1==0:
        yield 'UP',(nx,s,(l>>1)&RangeG[x][nxm1]&(RangeG[x][nxm1]>>1)&G[nx])
    if l>>(L-1)==0:
        yield 'DOWN',(nx,s,(l<<1)&RangeG[x][nxm1]&(RangeG[x][nxm1]<<1)&G[nx])

def living(l):
    return sum((l>>i)&1 for i in range(L))
        
def BFS(u0):
    Q = deque([u0])
    Pred = {u0:None}
    bestliv = V-1
    while Q:
        # position, speed, lanes mask (4 bits)
        u = Q.popleft()
        x,s,l = u
        if x==W-1:
            liv = living(l)
            # we can either break HERE if liv>=V to get the shortest
            # valid solution...
            # ...or continue with the following to get the shortest
            # solution maximizing the livings
            if liv>bestliv:
                bestliv = liv
                bestu = u
                if bestliv==M:
                    break
        elif living(l)>bestliv:
            for c,v in next_conf(x,s,l):
                if l and v not in Pred:
                    Pred[v] = (u,c)
                    Q.append(v)
    u = bestu
    Cmd = []
    while u!=u0:
        u,c = Pred[u]
        Cmd.append(c)
    return Cmd

def main():
    global M,V,W,G,RangeG
    M = int(input())  # the amount of motorbikes to control
    V = int(input())  # the minimum amount of motorbikes that must survive

    # L0 to L3 are lanes of the road.
    # A dot character . represents a safe space, a zero 0 represents a hole in the road.
    G0 = [input() for _ in range(L)]
    W = len(G0[0])

    # converting road columns to masks
    G = [0]*W
    for x in range(W):
        for l in range(L):
            G[x] |= int(G0[l][x]=='.')<<l

    # computing range AND masks in O(W^2)
    RangeG = [[(1<<L)-1]*W for _ in range(W)]
    for i in range(W):
        RangeG[i][i] = G[i]
        for j in range(i+1,W):
            RangeG[i][j] = RangeG[i][j-1] & G[j]
    
    first = True
    while True:
        S = int(input())  # the motorbikes' speed
        l = 0
        for _ in range(M):
            # x: x coordinate of the motorbike
            # y: y coordinate of the motorbike
            # a: indicates whether the motorbike is activated "1" or detroyed "0"
            x,y,a = map(int,input().split())
            if a==1:
                l |= 1<<y
        if first:
            # optimal path is precomputed at first round
            first = False
            Cmd = BFS((0,S,l))
        # for some reason the game can continue at x = W (out of bounds) 
        print(Cmd.pop() if Cmd else 'WAIT')

main()
