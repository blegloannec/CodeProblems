#!/usr/bin/env python3

import sys, os
from collections import deque, defaultdict
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


def robot_pic(x0,y0, x1,y1, A=4, init=1):
    C = defaultdict(int)
    R = IntcodeComputer(P)
    x = y = 0
    dx,dy = 0,1
    C[x,y] = init
    W,H = x1-x0+1, y1-y0+1
    Img = Image.new('RGB',(W,H))
    Col = [(0,0,0), (220,220,220), (255,0,0)]
    Pix = Img.load()
    Pix[0-x0,H-1-(0-y0)] = Col[2]
    t = 0
    Img.resize((A*W,A*H)).save('anim11/frame%04d.gif' % t)
    while not R.halt:
        R.In.append(C[x,y])
        R.run()
        C[x,y] = R.Out.popleft()
        d = R.Out.popleft()
        if d==0:
            dx,dy = -dy,dx
        else:
            dx,dy = dy,-dx
        Pix[x-x0,H-1-(y-y0)] = Col[C[x,y]]
        x += dx
        y += dy
        Pix[x-x0,H-1-(y-y0)] = Col[2]
        t += 1
        Img.resize((A*W,A*H)).save('anim11/frame%04d.gif' % t)
    Img.close()

os.system('mkdir anim11')
os.system('rm anim11.gif')
robot_pic(-2,-8,42,3)
#os.system('convert -loop 0 -delay 5 anim11/*.gif anim11.gif')
os.system('gifsicle -O3 -d5 -l anim11/*.gif > anim11.gif')
os.system('rm -r anim11')
