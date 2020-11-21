#!/usr/bin/env python3

# See also https://www.youtube.com/watch?v=vF_-ob9vseM
# The mouse, at distance Rm from O, is angularly faster
# than the cat iff Vm/Rm > Vc/R, i.e. Rm/R < ρ = Vm/Vc
# On the other hand, if the mouse is angularly on the
# opposite of the cat (i.e. O is aligned in between the mouse
# and the cat), it can escape going in straight line to the
# closest point on the border iff
# (R-Rm)/Vm < (πR-ε)/Vc where ε is a safety distance (DMIN below)
# i.e. Rm/R > 1-(π-ε/R)ρ
# Hence we must have 1-(π-ε/R)ρ < Rm/R < ρ to find a radius Rm
# at which we can go to the opposite of the cat and escape.
# For ε = 0, this is possible iff 1/ρ < π+1 ~ 4.14

import cmath

R = 500
Vm = 10
EPS = Vm
DMIN = 80 + 2*EPS

def main():
    Vc = int(input())
    Rlim = max(EPS, R - Vm/Vc * (cmath.pi*R - DMIN))
    o = None
    while True:
        mx,my, cx,cy = map(int, input().split())
        m = complex(mx, my)
        c = complex(cx, cy)
        if o is None:
            p = -Rlim/R * c
            if abs(m-p) < EPS:
                o = -2*c
                p = o
        else:
            p = o
        print(round(p.real), round(p.imag))

main()
