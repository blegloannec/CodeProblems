#!/usr/bin/env python3

import re

# Input
in_re = r'x=(\d+)\.\.(\d+), y=(-\d+)\.\.(-\d+)$'
x1,x2,y1,y2 = map(int, re.search(in_re, input()).groups())


# Precomp. on x: For each v0x, compute time intervals during which x1 ≤ x ≤ x2
# and store the v0x that lead to a position in [x1,x2] at each time.
tmax = 300  # arbitrary time bound...
T = [[] for _ in range(tmax)]
for v0x in range(1, x2+1):
    t = x = 0
    vx = v0x
    while x<=x2 and t<tmax:
        if x1<=x:
            T[t].append(v0x)
        x += vx
        if vx>0:
            vx -= 1
        t += 1


# Actual computation on y
# (Note: As there is not 0-cap on the y speed vy, we have:
#         vy(t) = v0y - t
#          y(t) = v0y*t - t*(t-1)//2
#  this would allow to test if a given v0y admits a compatible v0x
#  by binary searching for the t such that y1 ≤ y(t) ≤ y2.)
part1 = part2 = 0
for v0y in range(y1-1, 300):  # arbitrary upper bound...
    V0x = set()  # acceptable v0x for this v0y
    t = y = ymax = 0
    vy = v0y
    while y1<=y:
        if y<=y2:
            part1 = max(part1, ymax)
            assert t<tmax, 'increase tmax!'
            V0x.update(T[t])
        y += vy
        ymax = max(ymax, y)
        vy -= 1
        t += 1
    part2 += len(V0x)
print(part1, part2)
