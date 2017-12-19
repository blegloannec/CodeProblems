#!/usr/bin/env python3

import sys

G = [L[:-1] for L in sys.stdin.readlines()]
H,W = len(G),len(G[0])

def valid(x,y):
    return 0<=x<H and 0<=y<W and G[x][y]!=' '

def path():
    x,y = 0,G[0].index('|')
    dx,dy = 1,0
    S,s = [],0
    while True:
        s += 1
        if 'A'<=G[x][y]<='Z':
            S.append(G[x][y])
        if not valid(x+dx,y+dy):
            dx,dy = dy,dx
            if not valid(x+dx,y+dy):
                dx,dy = -dx,-dy
                if not valid(x+dx,y+dy):
                    break
        x += dx
        y += dy
    return ''.join(S),s

print(*path())  # Part 1 & 2
