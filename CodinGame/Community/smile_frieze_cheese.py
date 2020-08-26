#!/usr/bin/env python3

from math import gcd

lcm = lambda a,b: a*b//gcd(a,b)
per = lambda s: (s+s).index(s,1)

_fg = {0b0000: 'p111', 0b1000: 'p1m1', 0b0100: 'pm11', 0b0010: 'p112', 0b1110: 'pmm2', 0b0001: 'p1a1', 0b0111: 'pma2'}
grp = lambda H,V,R,G: _fg[(H<<3) | (V<<2) | (R<<1) | G]

def main():
    N = int(input())
    F = [input() for _ in range(N)]
    # extracting a smallest periodic pattern
    p = 1
    for L in F:
        p = lcm(p, per(L))
    P = [L[:p] for L in F]
    # testing symmetries
    H = all(P[N-1-i]==P[i] for i in range(N//2))
    V = all(L[::-1]==L for L in P)
    G = p%2==0 and all(P[i][:p//2]==P[N-1-i][p//2:] for i in range(N))
    R = (V and G) or all(P[N-1-i][::-1]==P[i] for i in range(N//2))
    print(grp(H,V,R,G))

main()
