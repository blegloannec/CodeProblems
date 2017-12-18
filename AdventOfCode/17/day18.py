#!/usr/bin/env python3

import sys
from collections import defaultdict,deque

I = [L.split() for L in sys.stdin.readlines()]

# Part 1
R = defaultdict(int)

def val(x):
    return R[x] if 'a'<=x[0]<='z' else int(x)

def simu(P):
    i = 0
    s = None
    while 0<=i<len(P):
        C = P[i][0]
        if C=='snd':
            s = val(P[i][1])
            i += 1
        elif C=='set':
            R[P[i][1]] = val(P[i][2])
            i += 1
        elif C=='add':
            R[P[i][1]] += val(P[i][2])
            i += 1
        elif C=='mul':
            R[P[i][1]] *= val(P[i][2])
            i += 1
        elif C=='mod':
            R[P[i][1]] %= val(P[i][2])
            i += 1
        elif C=='rcv':
            if val(P[i][1])!=0:
                return s
            i += 1
        else:  # jgz
            if val(P[i][1])>0:
                i += val(P[i][2])
            else:
                i += 1

print(simu(I))


# Part 2
class Prog:
    def __init__(self,P,p):
        self.P = P
        self.R = defaultdict(int)
        self.R['p'] = p
        self.i = 0
        self.Q = deque()  # received messages queue
        self.O = None     # prog to send messages to
        self.cpt = 0      # sent messages counter

    def push(self,m):
        self.Q.append(m)

    def pop(self):
        assert(self.Q)
        return self.Q.popleft()

    def sval(self,j):
        return self.P[self.i][j]

    def val(self,j):
        x = self.sval(j)
        return self.R[x] if 'a'<=x[0]<='z' else int(x)

    def blocked(self):
        return not 0<=self.i<len(self.P) or (self.sval(0)=='rcv' and not self.Q)

    def run(self):
        if self.blocked():
            return False
        while not self.blocked():
            C = self.sval(0)
            if C=='snd':
                self.O.push(self.val(1))
                self.cpt += 1
                self.i += 1
            elif C=='set':
                self.R[self.sval(1)] = self.val(2)
                self.i += 1
            elif C=='add':
                self.R[self.sval(1)] += self.val(2)
                self.i += 1
            elif C=='mul':
                self.R[self.sval(1)] *= self.val(2)
                self.i += 1
            elif C=='mod':
                self.R[self.sval(1)] %= self.val(2)
                self.i += 1
            elif C=='rcv':
                self.R[self.sval(1)] = self.pop()
                self.i += 1
            else:  # jgz
                if self.val(1)>0:
                    self.i += self.val(2)
                else:
                    self.i += 1
        return True

P0,P1 = Prog(I,0),Prog(I,1)
P0.O,P1.O = P1,P0
while P0.run() or P1.run():
    pass
print(P1.cpt)
