#!/usr/bin/env python3

import sys, math, cmath

DIR = {'N':complex(0,1), 'S':complex(0,-1), 'E':complex(1,0), 'W':complex(-1,0)}

I = [L.strip() for L in sys.stdin.readlines()]

def sail(d, part2=False):
    z = complex(0,0)
    for L in I:
        o, v = L[0], int(L[1:])
        if   o=='L': d *= cmath.rect(1, math.radians( v))
        elif o=='R': d *= cmath.rect(1, math.radians(-v))
        elif o=='F': z += v*d
        elif part2:  d += v*DIR[o]
        else:        z += v*DIR[o]
    return round(abs(z.real)+abs(z.imag))

print(sail(DIR['E']))
print(sail(complex(10,1), True))
