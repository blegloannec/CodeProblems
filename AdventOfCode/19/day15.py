#!/usr/bin/env python3

import sys
from collections import deque

P = list(map(int,sys.stdin.readline().strip().split(',')))


class IntcodeComputer:
    def __init__(self, P, In=None):
        self.P = P[:] + [0]*10**3  # program copy & padding
        self.i = 0
        if In is None:
            self.In = deque()
        elif isinstance(In, list):
            self.In = deque(In)
        else:
            assert isinstance(In, deque)
            self.In = In
        self.Out = deque()
        self.halt = False
        self.base = 0
    
    def run(self):
        assert not self.halt
        value = lambda k: self.P[self.i+k]
        mode  = lambda k: (value(0)//10**(1+k))%10
        addr  = lambda k: self.base+value(k) if mode(k)==2 else value(k)
        param = lambda k: value(k) if mode(k)==1 else self.P[addr(k)]
        while True:
            op = value(0) % 100
            if   op==1:  # add
                self.P[addr(3)] = param(1) + param(2)
                self.i += 4
            elif op==2:  # mul
                self.P[addr(3)] = param(1) * param(2)
                self.i += 4
            elif op==3:  # input
                if self.In:
                    x = self.In.popleft()
                    #print('input %d' % x)
                    self.P[addr(1)] = x
                    self.i += 2
                else:
                    break
            elif op==4:  # output
                self.Out.append(param(1))
                #print(self.Out[-1])
                self.i += 2
            elif op==5:  # jnz
                if param(1)!=0:
                    self.i = param(2)
                else:
                    self.i += 3
            elif op==6:  # jz
                if param(1)==0:
                    self.i = param(2)
                else:
                    self.i += 3
            elif op==7:  # lt
                self.P[addr(3)] = 1 if param(1)<param(2) else 0
                self.i += 4
            elif op==8:  # eq
                self.P[addr(3)] = 1 if param(1)==param(2) else 0
                self.i += 4
            elif op==9:  # incr base
                self.base += param(1)
                self.i += 2
            else:
                assert op==99
                self.halt = True
                break


def dfs(Droid, Map, x,y):
    for d,(vx,vy) in enumerate(((x-1,y),(x+1,y),(x,y-1),(x,y+1))):
        if Map[vx][vy] is None:
            Droid.In.append(d+1)
            Droid.run()
            Map[vx][vy] = Droid.Out.popleft()
            if Map[vx][vy]!=0:
                dfs(Droid, Map, vx,vy)
                Droid.In.append((1,0,3,2)[d]+1)
                Droid.run()
                stat = Droid.Out.popleft()
                assert stat == Map[x][y]

# NB: turns out the labyrinth is a tree, the dfs could have been recycled
#     to compute the distances, but one could not know beforehand...
def bfs(Map, x0,y0, stop2=False):
    S = len(Map)
    Dist = [[None]*S for _ in range(S)]
    Dist[x0][y0] = 0
    Q = deque([(x0,y0)])
    max_dist = 0
    while Q:
        x,y = Q.popleft()
        if stop2 and Map[x][y]==2:
            return x,y,Dist[x][y]
        max_dist = max(max_dist, Dist[x][y])
        for vx,vy in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
            if Map[vx][vy]!=0 and Dist[vx][vy] is None:
                Dist[vx][vy] = Dist[x][y] + 1
                Q.append((vx,vy))
    return max_dist

def droid():
    S = 50
    x0 = y0 = S//2
    Map = [[None]*S for _ in range(S)]
    Map[x0][y0] = 1
    Droid = IntcodeComputer(P)
    dfs(Droid, Map, x0,y0)
    xo,yo,d = bfs(Map, x0,y0, True)
    print(d)
    print(bfs(Map, xo,yo))
    #print('\n'.join(''.join(' ' if c is None else '#.O'[c] for c in L) for L in Map))

droid()
