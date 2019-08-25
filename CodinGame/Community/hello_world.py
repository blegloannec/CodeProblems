#!/usr/bin/env python3

from math import *

# https://en.wikipedia.org/wiki/Great-circle_distance
# see also CG/defibrillators.py
def dist(lola1, lola2):
    lo1,la1 = lola1
    lo2,la2 = lola2
    return 6371.*acos(sin(la1)*sin(la2)+cos(la1)*cos(la2)*cos(lo1-lo2))

parse_la = lambda la: (-1 if la[0]=='S' else 1) * radians(float(la[1:3]) + float(la[3:5])/60. + float(la[5:])/60.**2)
parse_lo = lambda lo: (-1 if lo[0]=='W' else 1) * radians(float(lo[1:4]) + float(lo[4:6])/60. + float(lo[6:])/60.**2)

def main():    
    N = int(input())
    M = int(input())
    Caps = []
    for _ in range(N):
        _,la,lo = input().split()
        Caps.append((parse_lo(lo), parse_la(la)))
    Hello = [input() for _ in range(N)]
    for _ in range(M):
        la,lo = input().split()
        lola = (parse_lo(lo), parse_la(la))
        D = [round(dist(lola,cap)) for cap in Caps]
        dmin = min(D)
        print(' '.join(Hello[i] for i in range(N) if D[i]==dmin))

main()
