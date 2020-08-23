#!/usr/bin/env python3

from collections import deque

def pack_config(P):
    P = [P[0]] + sorted(P[1:])
    return sum((i*W+j)<<(7*n) for n,(i,j) in enumerate(P))

def unpack_config(p):
    return [divmod((p>>(7*n))&127,W) for n in range(N)]

def bfs(p0, pf, dmax):
    Dist = {p0: 0}
    Q = deque([p0])
    while Q:
        p = Q.popleft()
        P = unpack_config(p)
        for i,pi in enumerate(P):
            x,y = pi
            for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
                vx = x+dx; vy = y+dy
                while 0<=vx<H and 0<=vy<W and \
                      G[vx][vy]=='.' and (vx,vy) not in P:
                    vx += dx; vy += dy
                vx -= dx; vy -= dy
                if (vx,vy)!=pi:
                    P[i] = (vx,vy)
                    q = pack_config(P)
                    if q not in Dist:
                        Dist[q] = dq = Dist[p]+1
                        if i==0 and P[0]==pf:
                            return dq
                        if dq<dmax:
                            Q.append(q)
                    P[i] = pi
    return 'NO SOLUTION'

def main():
    global N,W,H,G
    N,W,H,dmax = map(int, input().split())
    G = [list(input()) for _ in range(H)]
    P = [None]*N
    for i,L in enumerate(G):
        for j,c in enumerate(L):
            if c=='X':
                pf = (i,j)
                G[i][j] = '.'
            elif c not in 'W.':
                r = int(c)-1
                P[r] = (i,j)
                G[i][j] = '.'
    p0 = pack_config(P)
    print(bfs(p0, pf, dmax))

main()
