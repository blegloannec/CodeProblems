#!/usr/bin/env python3

import sys

I = sys.stdin.readlines()
Num = list(map(int, I[0].strip().split(',')))

# Parsing grids and preparing data structures
Val = [[] for _ in range(max(Num)+1)]
Sum = []
Row = []
Col = []
for l in range(2, len(I), 6):
    G = [list(map(int, I[j].split())) for j in range(l, l+5)]
    k = len(Sum)
    Sum.append(0)
    Row.append([0]*5)
    Col.append([0]*5)
    for i in range(5):
        for j in range(5):
            Val[G[i][j]].append((k,i,j))
            Sum[k] += G[i][j]

# Drawing numbers
Win = [False]*len(Sum)
Ord = []
for n in Num:
    for k,i,j in Val[n]:
        if not Win[k]:
            Sum[k] -= n
            Row[k][i] += 1
            Col[k][j] += 1
            if Row[k][i]==5 or Col[k][j]==5:
                Win[k] = True
                Ord.append((k+1, Sum[k]*n))

print(Ord[ 0][1])  # Part 1
print(Ord[-1][1])  # Part 2
