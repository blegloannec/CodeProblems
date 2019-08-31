#!/usr/bin/env python3

import sys, os.path
from PIL import Image
from math import gcd

def lcm(x,y):
    return x*y//gcd(x,y)

def photomaton(x,y,w,h):
    return x//2+(x%2)*(w//2), y//2+(y%2)*(h//2)

def photomaton_inv(x,y,w,h):
    if x<w//2:
        xx = x*2
    else:
        xx = 2*(x-w//2)+1
    if y<h//2:
        yy = 2*y
    else:
        yy = 2*(y-h//2)+1
    return xx,yy

def boulanger(x,y,w,h):
    if x<w//2:
        return 2*x+y%2, y//2
    else:
        return 2*(w-1-x)+(1-y%2), h-1-y//2

def boulanger_inv(x,y,w,h):
    if y<h//2:
        return x//2, 2*y+x%2
    else:
        return (w-1-x)//2+w//2, 2*(h-1-y)+(h-1-x)%2


class Morphimage:
    def __init__(self, img_file):
        self.Image = Image.open(img_file)
        self.W, self.H = self.size = self.Image.size

    def save(self, img_file):
        self.Image.save(img_file)

    def transform(self, f, n=1):
        for k in range(n):
            src = self.Image.copy()
            pix0 = src.load()
            pix = self.Image.load()
            for i in range(self.W):
                for j in range(self.H):
                    pix[f(i,j,self.W,self.H)] = pix0[i,j]


class Transformaccel:
    def __init__(self, transform, size):
        self.F = transform
        self.W, self.H = self.size = size
        self.precomp()

    def precomp(self):
        self.return_time = 1
        self.periods = {}
        self.cycles = [[None]*self.H for _ in range(self.W)]
        for x0 in range(self.W):
            for y0 in range(self.H):
                if self.cycles[x0][y0] is None:
                    c = []
                    p = 0
                    x,y = x0,y0
                    while self.cycles[x][y] is None:
                        self.cycles[x][y] = (c,p)
                        c.append((x,y))
                        x,y = self.F(x,y,self.W,self.H)
                        p += 1
                    self.return_time = lcm(self.return_time, p)
                    self.periods[p] = self.periods.get(p,0) + 1

    def iteration(self, n=1):
        def Fitr(x,y,w,h):
            c,p = self.cycles[x][y]
            return c[(p+n)%len(c)]
        return Fitr

    def inverse(self):
        return self.iteration(self.return_time-1)


if __name__=='__main__':
    try:
        niter = int(sys.argv[1])
        fname = sys.argv[2]
        Img = Morphimage(fname)
    except:
        print('usage: %s iterations path/to/imgfile' % sys.argv[0], file=sys.stderr)
        sys.exit(1)
    T = Transformaccel(photomaton, Img.size)
    print('Period: %d' % T.return_time)
    print(sorted(((p*c,p) for p,c in T.periods.items()), reverse=True))
    Img.transform(T.iteration(niter))
    oname = os.path.splitext(os.path.basename(fname))[0]
    Img.save('out_%s_%d.png' % (oname,niter))
