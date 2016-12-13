#!/usr/bin/env python

from collections import deque

Input = 1364

def is_open(x,y):
    n = x*x + 3*x + 2*x*y + y + y*y + Input
    r = 0
    while n>0:
        r ^= n&1
        n >>= 1
    return (r==0)

def bfs(start,dest):
    Q = deque([start])
    dist = {start:0}
    while Q:
        x,y = Q.popleft()
        d = dist[(x,y)]
        for (vx,vy) in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            if (vx,vy)==dest:
                # output for Part One is >50 so we already
                # have the solution for Part Two when the dest
                # is reached
                return d+1,sum(int(dist[p]<=50) for p in dist)
            if vx>=0 and vy>=0 and (vx,vy) not in dist and is_open(vx,vy):
                dist[(vx,vy)] = d+1
                Q.append((vx,vy))

start = (1,1)
assert(is_open(*start))
dest = (31,39)
assert(is_open(*dest))
print bfs(start,dest)
