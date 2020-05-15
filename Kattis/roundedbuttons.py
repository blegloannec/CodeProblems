#!/usr/bin/env python3

import sys
from math import hypot

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        L = sys.stdin.readline().split()
        X,Y,W,H,R = map(float, L[:5])
        L = list(map(float, L[6:]))
        for i in range(0,len(L),2):
            x,y = L[i:i+2]
            inside = False
            if X<=x<=X+W and Y<=y<=Y+H:
                inside = True
                if X<=x<=X+R and Y<=y<=Y+R and hypot(X+R-x,Y+R-y)>R:
                    inside = False
                elif X+W-R<=x<=X+W and Y<=y<=Y+R and hypot(X+W-R-x,Y+R-y)>R:
                    inside = False
                elif X<=x<=X+R and Y+H-R<=y<=Y+H and hypot(X+R-x,Y+H-R-y)>R:
                    inside = False
                elif X+W-R<=x<=X+W and Y+H-R<=y<=Y+H and hypot(X+W-R-x,Y+H-R-y)>R:
                    inside = False
            sys.stdout.write('inside\n' if inside else 'outside\n')
        sys.stdout.write('\n')

main()
