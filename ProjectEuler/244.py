#!/usr/bin/env python

from collections import *

class Conf:
    def __init__(self,T=None,x=0,y=0):
        self.T = T
        if self.T==None:
            self.T = int('1100110011001100',2)
        self.x,self.y = x,y

    @staticmethod
    def P(x,y):
        return 4*x+y

    def get(self,x,y):
        return (self.T>>Conf.P(x,y))&1

    def swap_bit(self,x,y):
        self.T ^= 1<<Conf.P(x,y)

    def set_bit(self,x,y,v):
        if self.get(x,y)!=v:
            self.swap_bit(x,y)

    def swap(self,x1,y1,x2,y2):
        v1,v2 = self.get(x1,y1),self.get(x2,y2)
        self.set_bit(x1,y1,v2)
        self.set_bit(x2,y2,v1)

    def L(self):
        if self.y==0:
            return None
        C = self.copy()
        C.swap(C.x,C.y,C.x,C.y-1)
        C.y -= 1
        return C

    def R(self):
        if self.y==3:
            return None
        C = self.copy()
        C.swap(C.x,C.y,C.x,C.y+1)
        C.y += 1
        return C

    def U(self):
        if self.x==0:
            return None
        C = self.copy()
        C.swap(C.x,C.y,C.x-1,C.y)
        C.x -= 1
        return C

    def D(self):
        if self.x==3:
            return None
        C = self.copy()
        C.swap(C.x,C.y,C.x+1,C.y)
        C.x += 1
        return C

    def copy(self):
        return Conf(self.T,self.x,self.y)

    def sgn(self):
        return (self.T,self.x,self.y)

    def __eq__(self,C):
        return self.sgn()==C.sgn()


def bfs():    
    dest = Conf(int('0101101001011010',2))
    #dest = Conf(int('1100100011101100',2),2,1)
    D = defaultdict(int)
    Q = deque()
    c0 = Conf()
    D[c0.sgn()] = 0
    Q.append((c0,0,0))
    while Q:
        c0,d,path = Q.popleft()
        if c0==dest:
            yield path
            continue
        for (c,p) in [(c0.U(),ord('D')),(c0.D(),ord('U')),(c0.L(),ord('R')),(c0.R(),ord('L'))]:
            if c!=None:
                s = c.sgn()
                if s not in D:
                    D[s] = d+1
                if D[s]==d+1:
                    Q.append((c,d+1,(243*path+p)%100000007))

def main():
    print(sum(bfs()))

main()
