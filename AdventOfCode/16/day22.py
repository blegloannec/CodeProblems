#!/usr/bin/env python

import sys
from collections import deque

# Grrrrr, could have made top 5 on part 2, yet thought
# we had to move the data from (0,H-1) instead of (W-1,0)...
# took me an eternity to find out the mistake :-p

P = [L.split() for L in sys.stdin.readlines()][2:]
# they are in (x,y) lexicographical order
last = P[-1][0].split('-')
W,H = int(last[1][1:])+1,int(last[2][1:])+1
Size = [int(N[1][:-1]) for N in P]
Used = [int(N[2][:-1]) for N in P]
Avail = [int(N[3][:-1]) for N in P]


# Part One
cpt,S = 0,set()
for i in xrange(len(P)):
    for j in xrange(len(P)):
        if i==j:
            continue
        if 0<Used[i]<=Avail[j]:
            cpt += 1
            S.add(j)
print cpt


# Part Two
# we can see that, as in the example, there is actually only one
# viable destination node, which is empty, so that the only way to
# solve the problem is by "moving around" the empty node
assert(len(S)==1)
empty = S.pop()
# also observe that if (x0,y0) is the empty node position
# we have to move (W-1,0) to (0,0) so that it costs at least
# (W-1-x0) + y0 + 5*(W-2)
# move the empty to (W-1,0) (and the wanted data to (W-2,0))
# then come back before it by moving under as many times as
# necessary (5 moves each time)
# yet due to the node sizes, all the moves of this ideal-optimal
# path might not be possible
# here x0,y0 = 26,22, so that the optimal solution is >= 177
# yet in my data set there is a simple "wall" of 7 too big nodes
# from (31,6) to (25,6) that simply costs 4 additional moves to
# get around (so that the solution 181 = 177 + 4 can easily be 
# calculated by hand)

# yet another bfs
def bfs():
    start = (empty/H,empty%H,W-1,0)
    Q = deque([start])
    dist = {start:0}
    while Q:
        # current position of the empty node & required data
        x,y,gx,gy = Q.popleft()
        d = dist[(x,y,gx,gy)]
        if (gx,gy)==(0,0):
            return d
        for (vx,vy) in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            if 0<=vx<W and 0<=vy<H and Used[vx*H+vy]<=Size[x*H+y]:
                vgx,vgy = gx,gy
                if (vx,vy)==(vgx,vgy):
                    vgx,vgy = x,y
                if (vx,vy,vgx,vgy) not in dist:
                    dist[(vx,vy,vgx,vgy)] = d+1
                    Q.append((vx,vy,vgx,vgy))

print bfs()
