#!/usr/bin/env python3

# Ternary search for the min max.
# NB (a posteriori): there are lots of possible approaches
#   http://pc.fdi.ucm.es/swerc/swerc09/SWERC-expl.pdf

import sys
input = sys.stdin.readline

EPS = 1e-5
MAX = 2e5

def main():
    while True:
        N = int(input())
        if N==0:
            break
        P = [tuple(map(float, input().split())) for _ in range(N)]
        input()
        dmax = lambda x: max((x-xi)*(x-xi)+yi*yi for xi,yi in P)
        l, r = -MAX, MAX
        while r-l>EPS:
            m1 = (2.*l+r)/3.
            m2 = (l+2.*r)/3.
            if dmax(m1)<dmax(m2):
                r = m2
            else:
                l = m1
        print(f'{r:.6f} {dmax(r)**0.5:.6f}')

main()
