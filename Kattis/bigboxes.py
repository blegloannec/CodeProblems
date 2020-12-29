#!/usr/bin/env python3

import sys
input = sys.stdin.readline

def boxes(bmax):
    b = 0
    k = 1
    for w in W:
        #assert w <= bmax
        if b+w <= bmax:
            b += w
        else:
            b = w
            k += 1
            if k > K:
                return False
    return True

def main():
    global K,W
    N,K = map(int, input().split())
    W = list(map(int, input().split()))
    wl = max(W); wr = sum(W)
    while wl<wr:
        wm = (wl+wr)//2
        if boxes(wm):
            wr = wm
        else:
            wl = wm+1
    print(wl)

main()
