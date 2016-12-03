#!/usr/bin/env python

Input = 'R1, R3, L2, L5, L2, L1, R3, L4, R2, L2, L4, R2, L1, R1, L2, R3, L1, L4, R2, L5, R3, R4, L1, R2, L1, R3, L4, R5, L4, L5, R5, L3, R2, L3, L3, R1, R3, L4, R2, R5, L4, R1, L1, L1, R5, L2, R1, L2, R188, L5, L3, R5, R1, L2, L4, R3, R5, L3, R3, R45, L4, R4, R72, R2, R3, L1, R1, L1, L1, R192, L1, L1, L1, L4, R1, L2, L5, L3, R5, L3, R3, L4, L3, R1, R4, L2, R2, R3, L5, R3, L1, R1, R4, L2, L3, R1, R3, L4, L3, L4, L2, L2, R1, R3, L5, L1, R4, R2, L4, L1, R3, R3, R1, L5, L2, R4, R4, R2, R1, R5, R5, L4, L1, R5, R3, R4, R5, R3, L1, L2, L4, R1, R4, R5, L2, L3, R4, L4, R2, L2, L4, L2, R5, R1, R4, R3, R5, L4, L4, L5, L5, R3, R4, L1, L3, R2, L2, R1, L3, L5, R5, R5, R3, L4, L2, R4, R5, R1, R4, L3'.split(', ')

# Part One
def pos(I):
    x,y = 0,0
    dx,dy = 0,1
    for i in I:
        r = i[0]
        if r=='L':
            dx,dy = -dy,dx
        else:
            dx,dy = dy,-dx
        s = int(i[1:])
        x,y = x+s*dx,y+s*dy
    return (x,y)

x,y = pos(Input)
print abs(x)+abs(y)


# Part Two
def pos2(I):
    x,y = 0,0
    visited = set((x,y))
    dx,dy = 0,1
    for i in I:
        r = i[0]
        if r=='L':
            dx,dy = -dy,dx
        else:
            dx,dy = dy,-dx
        s = int(i[1:])
        for _ in xrange(s):
            x,y = x+dx,y+dy
            if (x,y) in visited:
                return (x,y)
            visited.add((x,y))

x,y = pos2(Input)
print abs(x)+abs(y)
