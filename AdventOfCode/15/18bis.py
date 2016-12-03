#!/usr/bin/env python

import sys

S = 100
t = [[[0 for j in range(S)] for i in range(S)] for x in range(2)]

def step(x):
    for i in range(S):
        for j in range(S):
            if (i,j) in [(0,0),(0,99),(99,0),(99,99)]:
                t[(x+1)%2][i][j] = 1
                continue
            n = -t[x][i][j]
            for k in [-1,0,1]:
                for l in [-1,0,1]:
                    if 0<=i+k and i+k<S and 0<=j+l and j+l<S:
                        n += t[x][i+k][j+l]
            if t[x][i][j]==1 and (n<2 or n>3):
                t[(x+1)%2][i][j] = 0
            elif t[x][i][j]==0 and n==3:
                t[(x+1)%2][i][j] = 1
            else:
                t[(x+1)%2][i][j] = t[x][i][j]

def cpt(x):
    return sum(map(sum,t[x]))
                
def main():
    global t
    f = open(sys.argv[1],'r')
    l = f.readlines()
    f.close()
    for i in range(S):
        for j in range(S):
            t[0][i][j] = 1 if l[i][j]=='#' else 0
    for i in [0,99]:
        for j in [0,99]:
            t[0][i][j] = 1
    for i in range(100):
        step(i%2)
    print cpt(0)

main()
