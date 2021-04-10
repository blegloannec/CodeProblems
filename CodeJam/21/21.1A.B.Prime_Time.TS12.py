#!/usr/bin/env pypy

from heapq import *

def gen():
    s = sum(p*n for p,n in PN)
    H = [(-s,1)]
    Seen = {1}
    while H:
        s,p = heappop(H)
        s = -s
        if s==p:
            return s
        for pi,ni in PN:
            p0 = p
            n0 = 0
            while p0%pi==0:
                p0 /= pi
                n0 += 1
            if n0<ni:
                s1 = s-pi
                p1 = p*pi
                if p1<=s1 and p1 not in Seen:
                    Seen.add(p1)
                    heappush(H, (-s1,p1))
    return 0

def main():
    global PN
    T = int(raw_input())
    for t in xrange(1, T+1):
        M = int(raw_input())
        PN = [tuple(map(int, raw_input().split())) for _ in xrange(M)]
        print('Case #{}: {}'.format(t, gen()))

main()
