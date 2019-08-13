#!/usr/bin/env python3

S = 6
Dirs = ((-1,0),(1,0),(0,-1),(0,1))

class Piece:
    def __init__(self, pos, dir):
        self.i,  self.j = pos
        self.di, self.dj = dir
        self.loops = 0

    def pos(self):
        return (self.i, self.j)

    def dir(self):
        return (self.di, self.dj)

    def move(self):
        self.i, self.j = self.i+self.di, self.j+self.dj               # step
        if not (0<=self.i<S and 0<=self.j<S):                         # out of bounds
            if self.i==0 or self.j==0 or self.i==S-1 or self.j==S-1:  # out of a corner
                self.i, self.j = self.i-self.di, self.j-self.dj       # reverse move
                return False
            if (self.i< S//2 and self.j< S//2) or \
               (self.i>=S//2 and self.j>=S//2):                       # top-left or bottom-right
                self.i, self.j = self.j, self.i
                self.di, self.dj = -self.dj, -self.di
            else:                                                     # bottom-left or top-right
                self.i, self.j = S-1-self.j, S-1-self.i
                self.di, self.dj = self.dj, self.di
            self.i, self.j = self.i+self.di, self.j+self.dj           # step
            self.loops += 1
        return True

def main():
    G = [input() for _ in range(S)]
    res = 0
    for i0 in range(S):
        for j0 in range(S):
            if G[i0][j0]=='X':
                p0 = (i0,j0)
                for d0 in Dirs:
                    P = Piece(p0,d0)
                    while P.move() and (G[P.i][P.j]=='.' or (P.pos()==p0 and P.dir()!=d0)):
                        pass
                    if P.loops>0 and G[P.i][P.j]=='O':
                        res += 1
    print(res)

main()
