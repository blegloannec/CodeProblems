#!/usr/bin/env python3

import sys
from collections import deque

class MechBFS:
    def __init__(self, Mechs):
        self.Dist = [[-1]*W for _ in range(H)]
        for x,y in Mechs:
            self.Dist[x][y] = 0
        self.Q = deque(Mechs)
        self.R = set()  # reachable but not yet destroyed R
        self.time = 0

    def reachable(self, i,j):
        return self.Dist[i][j]>=0

    def reachableR(self, x, y):
        return (x,y) in self.R

    def step(self):
        while self.Q and self.Dist[self.Q[0][0]][self.Q[0][1]]==self.time:
            x,y = self.Q.popleft()
            for vx,vy in ((x-1,y),(x,y+1),(x+1,y),(x,y-1)):
                if 0<=vx<H and 0<=vy<W and self.Dist[vx][vy]<0:
                    if Map[vx][vy]=='.':
                        self.Dist[vx][vy] = self.time+1
                        self.Q.append((vx,vy))
                    else:
                        self.R.add((vx,vy))
        self.time += 1


def simulate(x,y, MechsPos):
    Mechs = MechBFS(MechsPos)
    ruinedR = 0
    visited = [[False]*W for _ in range(H)]
    while True:
        visited[x][y] = True
        V = tuple((vx,vy) for vx,vy in ((x-1,y),(x,y+1),(x+1,y),(x,y-1)) \
                  if 0<=vx<H and 0<=vy<W and not visited[vx][vy])
        moved = False
        for vx,vy in V:
            if Map[vx][vy]=='R':
                x,y = vx,vy
                ruinedR += 1
                if Mechs.reachableR(x,y):
                    return ruinedR
                Map[x][y] = '.'
                moved = True
                break
        if not moved and V:
            x,y = V[0]
        Mechs.step()
        # naive look for a reachable firing position for mechs
        for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
            i,j = x,y
            while 0<=i<H and 0<=j<W and Map[i][j]=='.':
                if Mechs.reachable(i,j):
                    return ruinedR
                i += di
                j += dj
    return ruinedR

def main():
    global H,W, Map
    T = int(sys.stdin.readline())
    for _ in range(T):
        W,H = map(int, sys.stdin.readline().split())
        Map = [list(sys.stdin.readline().strip()) for _ in range(H)]
        Mechs = []
        for i in range(H):
            for j in range(W):
                if Map[i][j]=='G':
                    Xg,Yg = i,j
                    Map[i][j] = '.'
                elif Map[i][j]=='M':
                    Mechs.append((i,j))
                    Map[i][j] = '.'
        print(simulate(Xg,Yg, Mechs))

main()
