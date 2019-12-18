#!/usr/bin/env python3

import sys
from collections import deque

P = list(map(int,sys.stdin.readline().strip().split(',')))


class IntcodeComputer:
    def __init__(self, P, In=None):
        self.P = P[:] + [0]*10**6  # program copy & padding
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


Dir = {'<':(0,-1), '>':(0,1), '^':(-1,0), 'v':(1,0)}

def robot():
    D = IntcodeComputer(P)
    D.run()
    G = ''.join(map(chr,D.Out))
    #print(G)
    G = [list(L) for L in G.split()]
    H,W = len(G),len(G[0])
    i,j = next((i,j) for i in range(H) for j in range(W) if G[i][j] in Dir)
    di,dj = Dir[G[i][j]]
    G[i][j] = '#'
    Seen = set()
    Path = []
    part1 = step = 0
    while 0<=i<H and 0<=j<W and G[i][j]=='#':
        if (i,j) not in Seen:
            Seen.add((i,j))
        else:
            part1 += i*j
        if not (0<=i+di<H and 0<=j+dj<W and G[i+di][j+dj]=="#"):
            for vi,vj,lr in ((-dj,di,'L'),(dj,-di,'R')):
                if 0<=i+vi<H and 0<=j+vj<W and G[i+vi][j+vj]=='#':
                    if step:
                        Path.append(str(step))
                    Path.append(lr)
                    step = 0
                    di,dj = vi,vj
                    break
        i += di
        j += dj
        step += 1
    print(part1)
    Path.append(str(step-1))
    #print(','.join(Path))  # Path
    # easily "compressed" by hand:
    # A(R,10,R,10,R,6,R,4),B(R,10,R,10,L,4),A(R,10,R,10,R,6,R,4),C(R,4,L,4,L,10,L,10),A(R,10,R,10,R,6,R,4),B(R,10,R,10,L,4),C(R,4,L,4,L,10,L,10),B(R,10,R,10,L,4),C(R,4,L,4,L,10,L,10),B(R,10,R,10,L,4)
    
    # /!\ the following ONLY works for MY input!
    D = IntcodeComputer(P)
    D.P[0] = 2
    D.In += list(map(ord,'A,B,A,C,A,B,C,B,C,B\n'))  # MAIN
    D.In += list(map(ord,'R,10,R,10,R,6,R,4\n'))    # A
    D.In += list(map(ord,'R,10,R,10,L,4\n'))        # B
    D.In += list(map(ord,'R,4,L,4,L,10,L,10\n'))    # C
    D.In += list(map(ord,'n\n'))                    # no trace
    D.run()
    print(D.Out.pop())

robot()
