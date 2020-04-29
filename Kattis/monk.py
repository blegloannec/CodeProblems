#!/usr/bin/env python3

import sys

def main():
    A,D = map(int, sys.stdin.readline().split())
    YXA = [tuple(map(int, sys.stdin.readline().split())) for _ in range(A)][::-1]
    YXD = [tuple(map(int, sys.stdin.readline().split())) for _ in range(D)][::-1]
    x = ha = 0
    hd = sum(y for y,_ in YXD)
    while True:
        ya,xa = YXA.pop()
        yd,xd = YXD.pop()
        if xa<xd:
            YXD.append((yd*(xd-xa)/xd, xd-xa))
            yd,xd = yd*xa/xd, xa
        elif xd<xa:
            YXA.append((ya*(xa-xd)/xa, xa-xd))
            ya,xa = ya*xd/xa, xd
        if hd-yd<=ha+ya:
            x += (hd-ha)/(ya/xa+yd/xd)
            break
        x += xa
        ha += ya
        hd -= yd
    print(x)

main()
