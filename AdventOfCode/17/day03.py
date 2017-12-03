#!/usr/bin/env python3

from math import sqrt
from collections import defaultdict

I = 347991  # Input

# Part 1 -- O(1) formula
def pos(n):
    s = int(sqrt(n-1))+1
    if s%2==0:
        s += 1
    k = s//2
    if n>=s*s-s+1:
        return (-k+n-(s*s-s+1),-k)
    elif n>=s*s-2*s+2:
        return (-k,k-(n-(s*s-2*s+2)))
    elif n>=s*s-3*s+3:
        return (k-(n-(s*s-3*s+3)),k)
    else:
        return (k,k-(s*s-3*s+3-n))

def dist(n):
    x,y = pos(n)
    return abs(x)+abs(y)

print(dist(I))


# Part 2 -- O(n)
def part2(n):
    D = defaultdict(int)
    D[0,0] = 1
    i = 2
    while True:
        x,y = pos(i)
        for dx in range(-1,2):
            for dy in range(-1,2):
                if not dx==dy==0:
                    D[x,y] += D[x+dx,y+dy]
        if D[x,y]>n:
            return D[x,y]
        i += 1

print(part2(I))
