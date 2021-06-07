#!/usr/bin/env python3

x,y = map(int, input().split())
u,v = map(int, input().split())

dx = abs(x-u)
dy = abs(y-v)
dx = min(dx, 200-dx)
dy = min(dy, 150-dy)
dd = min(dx, dy)
dx -= dd
dy -= dd
t = 3*dx + 4*dy + 5*dd

i,f = divmod(t, 10)
print(f'{i}.{f}')
