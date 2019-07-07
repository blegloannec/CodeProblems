#!/usr/bin/env python3

import random
random.seed()
from PIL import Image, ImageFont, ImageDraw

R = ['.........................',
     '...........#.#.#.........',
     '...........#####.........',
     '............###..........',
     '............###..........',
     '............###..........',
     '...........#####.........',
     '..........#######........',
     '.........................']
RW, RH = len(R[0]), len(R)

def gen_char_matrix():
    A = 6
    W, H = A*RW, A*RH
    I = [['.']*W for _ in range(H)]
    for i in range(H):
        x = (i*RH)//H
        for j in range(W):
            y = (j*RW)//W
            p = 0.7 if R[x][y]=='#' else 0.1
            if random.random()<p:
                I[i][j] = '#'
    #print('\n'.join(''.join(L) for L in I))
    return I

def gen_png(I):
    H,W = len(I),len(I[0])
    fmono = '/usr/share/fonts/truetype/ttf-bitstream-vera/VeraMoBd.ttf'
    col = {'#':(127,127,127,255), '.':(220,220,220,255)}
    mono = ImageFont.truetype(fmono, 18)
    cw,ch = mono.getsize('#')
    Img = Image.new('RGBA',(W*cw,H*ch),0)
    draw = ImageDraw.Draw(Img)
    for i in range(H):
        for j in range(W):
            c = I[i][j]
            draw.text((j*cw,i*ch), c, font=mono, fill=col[c])
    Img.save('cover.png')

gen_png(gen_char_matrix())
