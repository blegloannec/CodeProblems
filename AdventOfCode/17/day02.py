#!/usr/bin/env python3

import sys

G = [list(map(int,L.split())) for L in sys.stdin.readlines()]

# Part 1
print(sum(max(L)-min(L) for L in G))

# Part 2
def line_val(L):
    for i in range(len(L)):
        for j in range(len(L)):
            if i!=j and L[i]%L[j]==0:
                return L[i]//L[j]

print(sum(map(line_val,G)))
