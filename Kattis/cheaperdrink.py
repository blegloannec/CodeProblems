#!/usr/bin/env python3

import sys
input = sys.stdin.readline

def min_flip(m):
    f = []
    for c in m:
        if   c == '6':   f.append('9')
        elif c == '9':   f.append('6')
        elif c in '018': f.append(c)
        else:            return m
    f = ''.join(reversed(f))
    return min(m, f)

class Magnet:
    def __init__(self, m):
        self.m = min_flip(m)
    def __lt__(self, B):
        return self.m+B.m < B.m+self.m
    def __str__(self):
        return self.m

N = int(input())
print(*sorted(Magnet(input().strip()) for _ in range(N)), sep='')
