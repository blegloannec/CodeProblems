#!/usr/bin/env python3

import sys, re

form = re.compile('position=< *(-?\d+), *(-?\d+)> velocity=< *(-?\d+), *(-?\d+)>')
I = [tuple(map(int,form.match(L.strip()).groups())) for L in sys.stdin.readlines()]

# Part 1 & 2
def pic(t, out=False):
    X = [px+t*vx for px,_,vx,_ in I]
    Y = [py+t*vy for _,py,_,vy in I]
    x0,y0 = min(X),min(Y)
    W,H = max(X)-x0+1,max(Y)-y0+1
    if out:
        assert(max(W,H)<=100)
        O = [[' ']*W for _ in range(H)]
        for x,y in zip(X,Y):
            O[y-y0][x-x0] = '#'
        print('\n'.join(''.join(L) for L in O))
    return (W,H)

tmin = min(range(15000),key=pic)
pic(tmin,True)
print(tmin)
