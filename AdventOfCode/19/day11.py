#!/usr/bin/env python3

import sys
from collections import deque, defaultdict

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


# Part 1
def robot(init=0):
    C = defaultdict(int)
    R = IntcodeComputer(P)
    x = y = 0
    dx,dy = 0,1
    C[x,y] = init
    while not R.halt:
        R.In.append(C[x,y])
        R.run()
        C[x,y] = R.Out.popleft()
        d = R.Out.popleft()
        if d==0:
            dx,dy = -dy,dx
        else:
            dx,dy = dy,-dx
        x += dx
        y += dy
    return C

print(len(robot()))


# Part 2
C = robot(1)
xmin, xmax = min(x for x,_ in C), max(x for x,_ in C)
ymin, ymax = min(y for _,y in C), max(y for _,y in C)
W,H = xmax-xmin+1, ymax-ymin+3
P = [['#']*W for _ in range(H)]
for (x,y),c in C.items():
    if c:
        P[H-1-(y-ymin+1)][x-xmin+1] = ' '
print('\n'.join(''.join(L) for L in P))
