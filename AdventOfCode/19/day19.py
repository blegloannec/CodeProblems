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


def part1():
    S = 50
    G = [['.']*S for _ in range(S)]
    cnt = 0
    for x in range(S):
        for y in range(S):
            D = IntcodeComputer(P,[x,y])
            D.run()
            if D.Out[0]==1:
                cnt += 1
                G[y][x] = '#'
    print(cnt)
    #print('\n'.join(''.join(L) for L in G))
    # finding slopes of the beam
    for x in range(S-1,0,-1):
        y1 = next(y for y in xrange(S) if G[y][x]=='#')
        y2 = next(y for y in xrange(S-1,-1,-1) if G[y][x]=='#')
        if y2<S-1:
            return (float(y1)/x, float(y2)/x)

s1,s2 = part1()


# Part 2
# (I had the right point early enough for top 100 here but lost twice
#  the time before noticing I had swapped x/y in the answer...)
def part2():
    EPS = 1./50.
    N = 100
    S = 1200
    G = [[0]*S for _ in range(S)]
    x0 = int(N/(s2-s1))
    for x in range(x0,S):
        # top end of the beam
        y1 = max(1, int((s1-EPS)*x))
        while True:
            D = IntcodeComputer(P,[x,y1])
            D.run()
            if D.Out[0]==1:
                break
            y1 += 1
        # bottom end of the beam
        y2 = min(S-1, int((s2+EPS)*x))
        while True:
            D = IntcodeComputer(P,[x,y2])
            D.run()
            if D.Out[0]==1:
                break
            y2 -= 1
        # DP for largest square of 1 in a 0/1 grid
        for y in range(y1,y2+1):
            G[x][y] = 1 + min(G[x-1][y],G[x][y-1],G[x-1][y-1])
            if G[x][y]>=N:
                return (x-N+1)*10000 + y-N+1

print(part2())
