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


def network():
    N = 50
    C = [IntcodeComputer(P,[i]) for i in range(N)]
    part1 = True
    NAT = NAT0 = None
    while True:
        idle = True
        for i in range(N):
            if not C[i].In:
                C[i].In.append(-1)
            C[i].run()
            while len(C[i].Out)>=3:
                j = C[i].Out.popleft()
                x = C[i].Out.popleft()
                y = C[i].Out.popleft()
                if 0<=j<N:
                    C[j].In.append(x)
                    C[j].In.append(y)
                elif j==255:
                    NAT = (x,y)
                    if part1:
                        print(y)
                        part1 = False
                idle = False
        if idle and NAT is not None:
            x,y = NAT
            C[0].In.append(x)
            C[0].In.append(y)
            if NAT==NAT0:
                print(y)
                return
            NAT,NAT0 = None,NAT

network()
