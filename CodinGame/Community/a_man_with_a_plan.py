#!/usr/bin/env python3

from heapq import *

INF = float('inf')

def encode_state(x,y, b=0,s=0,p=0,d=0,t=0):
    return (x<<10) | (y<<5) | (b<<4) | (s<<3) | (p<<2) | (d<<1) | t

def decode_state(u):
    t,d,p,s,b = ((u>>i)&1 for i in range(5))
    y = (u>>5) & 0b11111
    x = u>>10
    return (x,y, b,s,p,d,t)

def dijkstra(u0):
    Dist = {u0: 0}
    Q = [(0, u0)]
    while Q:
        du,u = heappop(Q)
        if Dist[u] < du:
            continue
        x,y, b,s,p,d,t = decode_state(u)
        dt = 1
        if Map[x][y] == 'WIZARD':
            v = encode_state(wizzx,wizzy, b,s,p,d,t)
            if Dist.get(v, INF) > du+dt:
                Dist[v] = du+dt
                heappush(Q, (Dist[v], v))
            continue
        elif Map[x][y] == 'CASTLE':
            if (p and target == 'PRINCESS') or \
               (d and target == 'DRAGON')   or \
               (t and target == 'TREASURE'):
                return du
        elif Map[x][y] == 'BLACKSMITH':
            b = 1
        elif Map[x][y] == 'STABLE':
            s = 1
        elif Map[x][y] == 'PRINCESS':
            if not p:
                p = 1
                dt = 2 if b else 4
        elif Map[x][y] == 'DRAGON':
            if not d:
                d = 1
                dt = 2 if b else 4
        elif Map[x][y] == 'TREASURE':
            if not t:
                t = 1
                dt = 2 if b else 4
        elif Map[x][y] == 'G':
            dt = 1 if s else 2
        elif Map[x][y] == 'W':
            assert not b
            dt = 1 if s else 2
        elif Map[x][y] == 'M':
            assert not s
            dt = 4
        elif Map[x][y] == 'S':
            dt = 3 if s else 6
        for dx in (-1,0,1):
            for dy in (-1,0,1):
                if dx == dy == 0:
                    continue
                vx = x+dx; vy = y+dy
                if 0 <= vx < H and 0 <= vy < W      and \
                   Map[vx][vy] != 'R'               and \
                   (not (b and Map[vx][vy] == 'W')) and \
                   (not (s and Map[vx][vy] == 'M')):
                    v = encode_state(vx,vy, b,s,p,d,t)
                    if Dist.get(v, INF) > du+dt:
                        Dist[v] = du+dt
                        heappush(Q, (Dist[v], v))

def main():
    global W,H, target, Map, wizzx,wizzy
    W,H,N = map(int, input().split())
    target = input()
    Map = [list(input()) for _ in range(H)]
    wizz = None
    Pts = []
    for _ in range(N):
        interest,y,x = input().split()
        x = int(x); y = int(y)
        # overwriting the 'I' on the map
        Map[x][y] = interest
        if interest == 'WIZARD':
            wizz = (x,y)
        else:
            Pts.append((x,y))
            if interest == 'HOUSE':
                x0,y0 = x,y
    if wizz is not None:
        wizzx,wizzy = min(Pts, key=(lambda xy: abs(xy[0]-wizz[0])+abs(xy[1]-wizz[1])))
    u0 = encode_state(x0,y0)
    print(dijkstra(u0))

main()
