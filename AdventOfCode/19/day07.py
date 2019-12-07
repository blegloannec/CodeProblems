#!/usr/bin/env python3

from itertools import permutations
from collections import deque

P = list(map(int,input().split(',')))


class IntcodeComputer:
    def __init__(self, P, In=None):
        self.P = P[:]  # program copy
        self.i = 0
        if In is None:
            self.In = deque()
        elif isinstance(In, list):
            self.In = deque(In)
        else:
            assert isinstance(In, deque)
            self.In = In
        self.Out = []  # could be deque too
        self.halt = False
    
    def run(self):
        assert not self.halt
        value = lambda k: self.P[self.i+k]
        param = lambda k: value(k) if (value(0)//10**(1+k))%10 else self.P[value(k)]
        while True:
            op = value(0) % 100
            if   op==1:  # add
                self.P[value(3)] = param(1) + param(2)
                self.i += 4
            elif op==2:  # mul
                self.P[value(3)] = param(1) * param(2)
                self.i += 4
            elif op==3:  # input
                if self.In:
                    x = self.In.popleft()
                    #print('input %d' % x)
                    self.P[value(1)] = x
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
                self.P[value(3)] = 1 if param(1)<param(2) else 0
                self.i += 4
            elif op==8:  # eq
                self.P[value(3)] = 1 if param(1)==param(2) else 0
                self.i += 4
            else:
                assert op==99
                self.halt = True
                break


def part1():
    smax = 0
    for I in permutations(range(5)):
        S = [0]
        for i in I:
            C = IntcodeComputer(P,[i]+S)
            C.run()
            S = C.Out
        smax = max(smax, S[0])
    return smax

print(part1())


# Part 2
def part2():
    smax = 0
    for I in permutations(range(5,10)):
        C = [IntcodeComputer(P,[i]) for i in I]
        for i in range(len(C)):
            C[i].Out = C[(i+1)%len(C)].In
        C[0].In.append(0)
        while not C[-1].halt:
            for c in C:
                c.run()
        smax = max(smax, C[-1].Out[0])
    return smax

print(part2())
