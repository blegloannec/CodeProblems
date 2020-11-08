#!/usr/bin/env python3

import sys
input = sys.stdin.readline

Dir = {'N':(-1,0), 'S':(1,0), 'E':(0,1), 'W':(0,-1)}

def simu(A):
    for r,a,t in A:
        for _ in range(t):
            x,y,dx,dy = Pos[r]
            if a=='F':
                Map[x][y] = None
                x += dx; y += dy
                if 0<=x<H and 0<=y<W:
                    if Map[x][y] is not None:
                        return f'Robot {r+1} crashes into robot {Map[x][y]+1}'
                    Map[x][y] = r
                else:
                    return f'Robot {r+1} crashes into the wall'
            else:
                dx,dy = (-dy,dx) if a=='L' else (dy,-dx)
            Pos[r] = (x,y,dx,dy)
    return 'OK'

def main():
    global H,W, Map, Pos
    T = int(input())
    for _ in range(T):
        W,H = map(int, input().split())
        N,M = map(int, input().split())
        Pos = []
        Map = [[None]*W for _ in range(H)]
        for i in range(N):
            y,x,d = input().split()
            x = H-int(x); y = int(y)-1
            dx,dy = Dir[d]
            Pos.append((x,y,dx,dy))
            Map[x][y] = i
        A = []
        for _ in range(M):
            r,a,t = input().split()
            A.append((int(r)-1, a, int(t)))
        print(simu(A))

main()
