#!/usr/bin/env python3

L = int(input())
layout = input()
N,_ = map(int, input().split())
for _ in range(N):
    path = input().strip('#')
    sus = False
    i0 = 0
    i = d = 1
    while i<len(path):
        if path[i]=='#':
            d += 1
        else:
            dmin = (layout.index(path[i0])-layout.index(path[i]))%L
            dmin = min(dmin, L-dmin)
            if d<dmin:
                sus = True
                break
            i0 = i
            d = 1
        i += 1
    print('SUS' if sus else 'NOT SUS')
