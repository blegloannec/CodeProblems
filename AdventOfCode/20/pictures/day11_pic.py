#!/usr/bin/env python3

import sys, subprocess
from PIL import Image

I = [L.strip() for L in sys.stdin.readlines()]
H = len(I)
W = len(I[0])

def pic(C):
    Img = Image.new('RGB', (W,H))
    Pix = Img.load()
    for i in range(H):
        for j in range(W):
            if   C[i][j]=='.': Pix[j,i] = (200,200,200)
            elif C[i][j]=='L': Pix[j,i] = (125,150,255)
            else:              Pix[j,i] = (255,50,50)
    return Img.resize((5*W,5*W), resample=0)


def part1():
    C = [list(L) for L in I]
    pic(C).save(f'/tmp/frame{0:03d}.gif')
    change = True
    f = 1
    while change:
        C0 = tuple(tuple(L) for L in C)
        change = False
        for i in range(H):
            for j in range(W):
                if C0[i][j]=='.':
                    continue
                o = 0
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if di==dj==0:
                            continue
                        vi = i+di
                        vj = j+dj
                        if 0<=vi<H and 0<=vj<W and C0[vi][vj]=='#':
                            o += 1
                if C0[i][j]=='L' and o==0:
                    C[i][j] = '#'
                    change = True
                elif C0[i][j]=='#' and o>=4:
                    C[i][j] = 'L'
                    change = True
        if f%2==0:
            pic(C).save(f'/tmp/frame{f:03d}.gif')
        f += 1
    subprocess.run('gifsicle -O3 -d15 -l /tmp/frame*.gif > anim11_1.gif', shell=True)
    subprocess.run('rm /tmp/frame*.gif', shell=True)
    return sum(L.count('#') for L in C)

print(part1())


def part2():
    C = [list(L) for L in I]
    pic(C).save(f'/tmp/frame{0:03d}.gif')
    f = 1
    change = True
    while change:
        C0 = tuple(tuple(L) for L in C)
        change = False
        for i in range(H):
            for j in range(W):
                if C0[i][j]=='.':
                    continue
                o = 0
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if di==dj==0:
                            continue
                        vi = i+di
                        vj = j+dj
                        while 0<=vi<H and 0<=vj<W and C0[vi][vj]=='.':
                            vi += di
                            vj += dj
                        if 0<=vi<H and 0<=vj<W and C0[vi][vj]=='#':
                            o += 1
                if C0[i][j]=='L' and o==0:
                    C[i][j] = '#'
                    change = True
                elif C0[i][j]=='#' and o>=5:
                    C[i][j] = 'L'
                    change = True
        if f%2==0:
            pic(C).save(f'/tmp/frame{f:03d}.gif')
        f += 1
    subprocess.run('gifsicle -O3 -d15 -l /tmp/frame*.gif > anim11_2.gif', shell=True)
    subprocess.run('rm /tmp/frame*.gif', shell=True)
    return sum(L.count('#') for L in C)

print(part2())
