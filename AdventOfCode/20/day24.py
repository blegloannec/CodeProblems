#!/usr/bin/env pypy3

import sys, re

I = [L.strip() for L in sys.stdin.readlines()]


# Part 1 - Inspired by AoC 17 / Day 11 (hex grid)
class P:
    def __init__(self, x=0, y=0, z=0):
        #assert x+y+z==0
        self.x = x; self.y = y; self.z = z
        self.h = hash((x,y,z))
    def __add__(self, B):
        return P(self.x+B.x, self.y+B.y, self.z+B.z)
    def __hash__(self):
        return self.h
    def __eq__(self, Q):
        return self.x==Q.x and self.y==Q.y #and self.z==Q.z

D = { 'w': P(0,1,-1),  'e': P(0,-1,1), 'nw': P(1,0,-1),
     'se': P(-1,0,1), 'sw': P(-1,1,0), 'ne': P(1,-1,0)}

B = set()
for L in I:
    X = P()
    for d in re.findall(r'e|se|sw|w|nw|ne', L):
        X += D[d]
    if X in B: B.remove(X)
    else:      B.add(X)
print(len(B))


# Part 2 - Recycled from Day 17.2 (third CA this year!)
def part2(C, T=100):
    for _ in range(T):
        Vcnt = {}
        for X in C:
            Vcnt[X] = Vcnt.get(X, 0) + 1
            for V in D.values():
                Y = X+V
                Vcnt[Y] = Vcnt.get(Y, 0) + 1
        for u,c in Vcnt.items():
            if u in C:
                if not 1<=c-1<=2:
                    C.remove(u)
            else:
                if c==2:
                    C.add(u)
    return len(C)

print(part2(B))
