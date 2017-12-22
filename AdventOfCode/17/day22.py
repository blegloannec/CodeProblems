#!/usr/bin/env python3

# yet another Langton ant...

import sys
from collections import defaultdict

G = [L.strip() for L in sys.stdin.readlines()]
N = len(G)

# Part 1
I = {(i,j) for i in range(N) for j in range(N) if G[i][j]=='#'}

def simu1(n):
    x = y = N//2
    dx,dy = -1,0
    cpt = 0
    for _ in range(n):
        if (x,y) in I:
            dx,dy = dy,-dx
            I.remove((x,y))
        else:
            dx,dy = -dy,dx
            I.add((x,y))
            cpt += 1
        x += dx
        y += dy
    return cpt

print(simu1(10000))


# Part 2
S = defaultdict(int)
for i in range(N):
    for j in range(N):
        if G[i][j]=='#':
            S[i,j] = 2

def simu2(n):
    x = y = N//2
    dx,dy = -1,0
    cpt = 0
    for _ in range(n):
        if S[x,y]==0:
            dx,dy = -dy,dx
        elif S[x,y]==1:
            cpt += 1
        elif S[x,y]==2:
            dx,dy = dy,-dx
        elif S[x,y]==3:
            dx,dy = -dx,-dy
        S[x,y] = (S[x,y]+1)%4
        x += dx
        y += dy
    return cpt

print(simu2(10**7))
