#!/usr/bin/env python3

n,k = map(int,input().split())
x0,y0 = map(int,input().split())
O = set(tuple(map(int,input().split())) for _ in range(k))

# O(n) approach, iterating over the cells until a border/obstacle
# O(k) would also be possible, iterating over the obstacles and
# remembering the closest in each direction
cpt = 0
for dx in [-1,0,1]:
    for dy in [-1,0,1]:
        if (dx,dy)!=(0,0):
            x,y = x0+dx,y0+dy
            while 1<=x<=n and 1<=y<=n and (x,y) not in O:
                cpt += 1
                x += dx
                y += dy
print(cpt)
