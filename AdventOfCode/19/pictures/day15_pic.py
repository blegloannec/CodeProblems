#!/usr/bin/env python3

import sys, os
from collections import deque
from PIL import Image

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

S = 41
Col = [(50,50,50), (220,220,220), (0,0,255), (255,0,0)]
T = 0

def frame(x,y):
    global T
    Pix[x,y] = Col[-1]
    Img.resize((4*S,4*S)).save('anim15/frame%04d.gif' % T)
    Pix[x,y] = Col[Map[x][y]]
    T += 1

def dfs(x,y):
    for d,(vx,vy) in enumerate(((x-1,y),(x+1,y),(x,y-1),(x,y+1))):
        if Map[vx][vy] is None:
            Droid.In.append(d+1)
            Droid.run()
            Map[vx][vy] = Droid.Out.popleft()
            Pix[vx,vy] = Col[Map[vx][vy]]
            frame(x,y)
            if Map[vx][vy]!=0:
                dfs(vx,vy)
                Droid.In.append((1,0,3,2)[d]+1)
                Droid.run()
                frame(x,y)
                stat = Droid.Out.popleft()
                assert stat == Map[x][y]

def droid():
    global Droid, Map, Img, Pix
    x0 = y0 = (S+1)//2
    Map = [[None]*S for _ in range(S)]
    Map[x0][y0] = 1
    Droid = IntcodeComputer(P)
    Img = Image.new('RGB',(S,S))
    Pix = Img.load()
    os.system('mkdir anim15')
    dfs(x0,y0)
    os.system('convert -loop 0 -delay 2 anim15/frame*.gif anim15.gif')
    os.system('rm -r anim15')
    Img.close()

droid()
