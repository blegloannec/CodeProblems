#!/usr/bin/env python3

D = {'|':  {(0,-1):[(0,1)], (-1,-1):[(0,1)], (1,-1):[(0,1)],
            (0,1):[(0,-1)], (-1,1):[(0,-1)], (1,1):[(0,-1)]},
     '-':  {(-1,0):[(1,0)], (-1,-1):[(1,0)], (-1,1):[(1,0)],
            (1,0):[(-1,0)], (1,-1):[(-1,0)], (1,1):[(-1,0)]},
     '/':  {(-1,0):[(1,0),(1,1),(0,1)], (-1,-1):[(1,0),(1,1),(0,1)], (0,-1):[(1,0),(1,1),(0,1)],
            (0,1):[(-1,0),(-1,-1),(0,-1)], (1,1):[(-1,0),(-1,-1),(0,-1)], (1,0):[(-1,0),(-1,-1),(0,-1)]},
     '\\': {(-1,0):[(1,0),(1,-1),(0,-1)], (-1,1):[(1,0),(1,-1),(0,-1)], (0,1):[(1,0),(1,-1),(0,-1)],
            (1,0):[(-1,0),(-1,1),(0,1)], (1,-1):[(-1,0),(-1,1),(0,1)], (0,-1):[(-1,0),(-1,1),(0,1)]}}

N = int(input())
G = [input().split() for _ in range(N)]

# DFS
Seen = [[False]*N for _ in range(N)]
Q = [((0,0),(-1,-1))]
Seen[0][0] = True
while Q:
    (ux,uy),du = Q.pop()
    c = G[ux][uy]
    for dvx,dvy in D[c][du]:
        v = vx,vy = ux+dvx,uy+dvy
        dv = -dvx,-dvy 
        if 0<=vx<N and 0<=vy<N and not Seen[vx][vy] and G[vx][vy]!='.' and dv in D[G[vx][vy]]:
            Seen[vx][vy] = True
            Q.append((v,dv))
print(sum(int(G[x][y]!='.' and not Seen[x][y]) for x in range(N) for y in range(N)))
