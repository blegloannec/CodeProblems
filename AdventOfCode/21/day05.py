#!/usr/bin/env python3

import sys, re

R = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)\n')
I = [tuple(map(int, re.fullmatch(R, L).groups())) for L in sys.stdin.readlines()]
S = max(max(L) for L in I)+1

def sign(x):
    return -1 if x<0 else 0 if x==0 else +1

def cnt_pts(grid=False):
    res = 0
    C = [[0]*S for _ in range(S)]
    for x,y,xf,yf in I:
        if grid and x!=xf and y!=yf:
            continue
        dx = sign(xf-x)
        dy = sign(yf-y)
        while True:
            C[x][y] += 1
            if C[x][y]==2:
                res += 1
            if x==xf and y==yf:
                break
            x += dx
            y += dy
    return res

print(cnt_pts(True))  # Part 1
print(cnt_pts())      # Part 2
