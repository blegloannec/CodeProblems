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


W,H = 43,23
sgn = lambda x: 0 if x==0 else 1 if x>0 else -1
def breakout_gif():
    Color = [(0,0,0),(50,50,50),(120,120,255),(220,220,220),(255,80,80)]
    Game = IntcodeComputer(P)
    Game.P[0] = 2  # set credits
    Img = Image.new('RGB',(W,H))
    Pix = Img.load()
    f = 0
    while not Game.halt:
        Game.run()
        while Game.Out:
            x,y,t = (Game.Out.popleft() for _ in range(3))
            if t==3:
                px = x
            elif t==4:
                bx = x
            if x<0:
                score = t
            else:
                Pix[x,y] = Color[t]
        Game.In.append(sgn(bx-px))
        Img.resize((4*W,4*H)).save('anim13/frame%04d.gif' % f)
        f += 1

os.system('mkdir anim13')
breakout_gif()
#os.system('convert -loop 0 -delay 4 anim13/*.gif anim13.gif')
os.system('gifsicle -O3 -d3 -l anim13/*.gif > anim13.gif')
os.system('rm -r anim13')
