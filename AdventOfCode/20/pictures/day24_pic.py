#!/usr/bin/env python3

import sys, re
import cairo, cmath
import subprocess
from multiprocessing import Process

I = [L.strip() for L in sys.stdin.readlines()]


## Part 1 ##
Ux = complex(0, -1)
Uy = cmath.rect(1, 5*cmath.pi/6)
Uz = cmath.rect(1, cmath.pi/6)
Theta = cmath.rect(1, cmath.pi/3)

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
    def draw(self, ctx, color=(0.25, 0.25, 0.25), border=True):
        c = self.x*Ux + self.y*Uy + self.z*Uz
        b = c + Ux
        ctx.move_to(b.real, b.imag)
        for _ in range(5):
            b = (b-c)*Theta + c
            ctx.line_to(b.real, b.imag)
        ctx.close_path()
        ctx.set_source_rgb(*color)
        if border:
            ctx.fill_preserve()
            ctx.set_source_rgb(1, 1, 1)
            ctx.stroke()
        else:
            ctx.fill()

D = { 'w': P(0,1,-1),  'e': P(0,-1,1), 'nw': P(1,0,-1),
     'se': P(-1,0,1), 'sw': P(-1,1,0), 'ne': P(1,-1,0)}

def draw_frame(Pts, frame=0, size=500, alpha=10, border=True):
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, size, size)
    ctx = cairo.Context(surf)
    ctx.set_source_rgb(1, 1, 1)
    ctx.rectangle(0, 0, size, size)
    ctx.fill()
    ctx.translate(size/2, size/2)
    ctx.scale(alpha, alpha)
    ctx.set_line_width(1/alpha)
    for p in Pts:
        p.draw(ctx, border=border)
    return surf, ctx

def save_frame(surf, frame=0):
    fname = f'/tmp/frame{frame:04d}'
    surf.write_to_png(f'{fname}.png')
    subprocess.run(('convert', f'{fname}.png', f'{fname}.gif'))

def part1():
    f = 0
    B = set()
    SP = []
    for L in I:
        surf, ctx = draw_frame(B)
        X = P()
        for d in re.findall(r'e|se|sw|w|nw|ne', L):
            X.draw(ctx, color=(0.4, 0.4, 1))
            X += D[d]
        if X in B:
            B.remove(X)
            X.draw(ctx, color=(1, 0.3, 0.3))
        else:
            B.add(X)
            X.draw(ctx, color=(0.3, 0.9, 0.3))
        SP.append(Process(target=save_frame, args=(surf, f)))
        SP[-1].start()
        f += 1
    for sp in SP:
        sp.join()
    print(len(B))
    return B

B = part1()
subprocess.run('gifsicle -O3 -d20 -l --colors 256 /tmp/frame*.gif > anim24_1.gif', shell=True)
subprocess.run('rm -f /tmp/frame*', shell=True)


## Part 2 ##
def part2(C, T=100):
    SP = []
    for f in range(T):
        surf, ctx = draw_frame(C, f, size=700, alpha=4.7, border=False)
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
                    u.draw(ctx, color=(1, 0.5, 0.5), border=False)
            else:
                if c==2:
                    C.add(u)
                    u.draw(ctx, color=(0.3, 0.7, 0.7), border=False)
        SP.append(Process(target=save_frame, args=(surf, f)))
        SP[-1].start()
    for sp in SP:
        sp.join()
    return len(C)

print(part2(B))
subprocess.run('gifsicle -O3 -d15 -l --colors 256 /tmp/frame*.gif > anim24_2.gif', shell=True)
subprocess.run('rm -f /tmp/frame*', shell=True)
