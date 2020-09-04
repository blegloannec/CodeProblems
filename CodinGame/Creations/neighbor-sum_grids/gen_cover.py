#!/usr/bin/env python3

import cairo
import random
random.seed(333)
from math import tau

def set_rand_col(ctx):
    d = 0.25
    rc = lambda: 1. - d*random.random()
    ctx.set_source_rgb(rc(), rc(), rc())

W, H = 1920, 1080

def drop_grid(ctx, grid):
    S = 38
    x, y = random.randint(0,W), random.randint(0,H)
    ctx.translate(x, y)
    ctx.rotate(tau*random.random())
    ctx.rectangle(0, 0, 5*S, 5*S)
    #ctx.set_source_rgb(1, 1, 1)
    set_rand_col(ctx)
    ctx.fill()
    ctx.set_source_rgb(0.3, 0.3, 0.3)
    ctx.set_line_width(2)
    for i in range(1,5):
        yi = i*S
        ctx.move_to(0, yi)
        ctx.line_to(5*S, yi)
        ctx.stroke()
        xi = i*S
        ctx.move_to(xi, 0)
        ctx.line_to(xi, 5*S)
        ctx.stroke()
    ctx.set_source_rgb(0.2, 0.2, 0.2)
    ctx.set_line_width(5)
    ctx.rectangle(0, 0, 5*S, 5*S)
    ctx.stroke()
    for i in range(5):
        for j in range(5):
            ctx.move_to(i*S+3, (j+1)*S-9)
            c = grid[5*i+j]
            if len(c)==1 or c[0]=='1':
                c = ' ' + c
            ctx.show_text(c)
    ctx.identity_matrix()

def main():
    Grids = open('grids', 'r').readlines()
    surf = cairo.ImageSurface(cairo.FORMAT_RGB24, W, H)
    ctx = cairo.Context(surf)
    ctx.select_font_face('Chilanka', cairo.FontSlant.NORMAL, cairo.FontWeight.BOLD)
    ctx.set_font_size(24)
    # background
    ctx.set_source_rgb(1, 1, 1)
    ctx.rectangle(0, 0, W, H)
    ctx.fill()
    # grids
    for _ in range(130):
        drop_grid(ctx, random.choice(Grids).split())
    # output
    surf.write_to_png('cover.png')

main()
