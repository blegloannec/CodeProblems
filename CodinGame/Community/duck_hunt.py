#!/usr/bin/env python3

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __add__(self, B):
        return Point(self.x+B.x, self.y+B.y)
    def __sub__(self, B):
        return Point(self.x-B.x, self.y-B.y)

class Duck:
    def __init__(self, did, p, v):
        self.did = did
        self.p, self.v = p, v
    def move(self):
        self.p += self.v
        if 0<=self.p.x<W and 0<=self.p.y<H:
            return True
        else:
            self.p -= self.v
            return False
    def __str__(self):
        return f'{self.did} {self.p.x} {self.p.y}'

def main():
    global W,H
    W = int(input())
    H = int(input())
    G1 = [input() for _ in range(H)]
    G2 = [input() for _ in range(H)]
    D1 = {}
    D2 = {}
    for y in range(H):
        for x in range(W):
            if G1[y][x]!='.':
                D1[G1[y][x]] = Point(x,y)
            if G2[y][x]!='.':
                D2[G2[y][x]] = Point(x,y)
    D = []
    for c in D2:
        d = Duck(c, D2[c], D2[c]-D1[c])
        if d.move():
            D.append(d)
    # because we know the optimal solution is unique, there must
    # be  at most  one duck that disappears at each of the following steps
    # and    least                          except at the last step
    while D:
        D0, D = D, []
        for d in D0:
            if len(D0)==1 or not d.move():
                print(d)
            else:
                D.append(d)

main()
