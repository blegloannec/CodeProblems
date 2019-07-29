#!/usr/bin/env python3

Dir = {'^': (-1,0), 'v': (1,0), '<': (0,-1), '>': (0,1)}

def edge(s, i, j):
    if s==0:
        if   i==-1: return (5,N-1,j), Dir['^']
        elif i== N: return (2,0,j), Dir['v']
        elif j==-1: return (1,0,i), Dir['v']
        elif j== N: return (3,0,N-1-i), Dir['v']
    elif s==1:
        if   i==-1: return (0,j,0), Dir['>']
        elif i== N: return (4,N-1-j,0), Dir['>']
        elif j==-1: return (5,N-1-i,0), Dir['>']
        elif j== N: return (2,i,0), Dir['>']
    elif s==2:
        if   i==-1: return (0,N-1,j), Dir['^']
        elif i== N: return (4,0,j), Dir['v']
        elif j==-1: return (1,i,N-1), Dir['<']
        elif j== N: return (3,i,0), Dir['>']
    elif s==3:
        if   i==-1: return (0,N-1-j,N-1), Dir['<']
        elif i== N: return (4,j,N-1), Dir['<']
        elif j==-1: return (2,i,N-1), Dir['<']
        elif j== N: return (5,N-1-i,N-1), Dir['<']
    elif s==4:
        if   i==-1: return (2,N-1,j), Dir['^']
        elif i== N: return (5,0,j), Dir['v']
        elif j==-1: return (1,N-1,N-1-i), Dir['^']
        elif j== N: return (3,N-1,i), Dir['^']
    elif s==5:
        if   i==-1: return (4,N-1,j), Dir['^']
        elif i== N: return (0,0,j), Dir['v']
        elif j==-1: return (1,N-1-i,0), Dir['>']
        elif j== N: return (3,N-1-i,N-1), Dir['<']

def path(s0, i0, j0, di, dj):
    s,i,j = s0,i0,j0
    start = True
    while start or (s,i,j)!=(s0,i0,j0):
        start = False
        if left_side:
            DV = ((-dj,di), (di,dj), (dj,-di), (-di,-dj))
        else:
            DV = ((dj,-di), (di,dj), (-dj,di), (-di,-dj))
        for dx,dy in DV:
            x, y = i+dx, j+dy
            if not (0<=x<N and 0<=y<N):
                (s,x,y),(dx,dy) = edge(s,x,y)
            if G[s][x][y]!='#':
                i,j = x,y
                di,dj = dx,dy
                G[s][i][j] += 1
                break

if __name__=='__main__':
    N = int(input())
    G = [[[0 if c=='0' else c for c in input()] for _ in range(N)] for _ in range(6)]
    left_side = input()=='L'
    s0,i0,j0 = next((s,i,j) for s in range(6) for i in range(N) for j in range(N) if G[s][i][j] in Dir)
    di,dj = Dir[G[s0][i0][j0]]
    G[s0][i0][j0] = 0
    path(s0,i0,j0,di,dj)
    print('\n'.join('\n'.join(''.join(map(str, L)) for L in S) for S in G))
