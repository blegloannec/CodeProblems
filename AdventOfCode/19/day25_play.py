#!/usr/bin/env python3

# use:
# $ cat rec0 - | tee rec1 | python3 day25_play.py input25
# to register your moves in rec1 while replaying rec0 at the start
# of the current session

import sys
from collections import deque

P = list(map(int,open(sys.argv[1],'r').readline().strip().split(',')))

to_ascii = lambda s: list(map(ord,s))
to_str = lambda l: ''.join(map(chr,l))

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
                if not self.In:
                    self.In += to_ascii(sys.stdin.readline())
                x = self.In.popleft()
                sys.stdout.write(chr(x))
                self.P[addr(1)] = x
                self.i += 2
            elif op==4:  # output
                self.Out.append(param(1))
                sys.stdout.write(chr(self.Out[-1]))
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


IC = IntcodeComputer(P)
IC.run()
