#!/usr/bin/env python3

import sys

Map = [list(L.strip()) for L in sys.stdin.readlines()]
H,W = len(Map),len(Map[0])

def step(C):
    move = False
    # move east
    for i in range(H):
        L = Map[i].copy()
        for j in range(W):
            k = (j+1)%W
            if L[j]=='>' and L[k]=='.':
                Map[i][j] = '.'
                Map[i][k] = '>'
                move = True
    # move south
    for j in range(W):
        C = [Map[i][j] for i in range(H)]
        for i in range(H):
            k = (i+1)%H
            if C[i]=='v' and C[k]=='.':
                Map[i][j] = '.'
                Map[k][j] = 'v'
                move = True
    return move


# Animated GIF
import subprocess
from PIL import Image

TMPDIR = '/tmp/aoc21anim25'
subprocess.run(('mkdir', TMPDIR))

Color = {'.': (0, 25, 50), 'v': (189, 51, 164), '>': (112, 41, 99)}

def make_frame():
    Img = Image.new('RGB', (W,H), Color['.'])
    Pix = Img.load()
    for i in range(H):
        for j in range(W):
            if Map[i][j]!='.':
                Pix[j,i] = Color[Map[i][j]]
    return Img

t = 1
while step(Map):
    make_frame().resize((4*W,4*H), Image.NEAREST).save(f'{TMPDIR}/frame{t:04d}.gif')
    t += 1
print(t)

subprocess.run(f'gifsicle -O3 -l -d8 {TMPDIR}/frame*.gif > anim25.gif', shell=True)
subprocess.run(('rm', '-rf', TMPDIR))
