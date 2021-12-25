#!/usr/bin/env python3

import sys

Map = [list(L.strip()) for L in sys.stdin.readlines()]
H,W = len(Map),len(Map[0])

def step(C):
    move = False
    # move east
    for i in range(H):
        L = Map[i].copy()
        for j in range(W):
            k = (j+1)%W
            if L[j]=='>' and L[k]=='.':
                Map[i][j] = '.'
                Map[i][k] = '>'
                move = True
    # move south
    for j in range(W):
        C = [Map[i][j] for i in range(H)]
        for i in range(H):
            k = (i+1)%H
            if C[i]=='v' and C[k]=='.':
                Map[i][j] = '.'
                Map[k][j] = 'v'
                move = True
    return move

t = 1
while step(Map):
    t += 1
print(t)
