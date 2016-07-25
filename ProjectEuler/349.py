#!/usr/bin/env python

#https://en.wikipedia.org/wiki/Langton%27s_ant

black = set()
x,y,o = 0,0,0
D = [(-1,0),(0,1),(1,0),(0,-1)]
def step():
    global x,y,o
    if (x,y) in black:
        black.remove((x,y))
        o = (o-1)%4
    else:
        black.add((x,y))
        o = (o+1)%4
    x += D[o][0]
    y += D[o][1]

def simu(n):
    # regime transitoire
    for _ in xrange(11000):
        step()
    A = len(black)
    # regime stationnaire
    for _ in xrange(104):
        step()
    B = len(black)-A
    n -= 11000
    # complement
    for _ in xrange(n%104):
        step()
    C = len(black)-(A+B)
    return A + (n/104)*B + C

print simu(10**18)
