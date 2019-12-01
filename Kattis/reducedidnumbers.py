#!/usr/bin/env python3

import sys

N = 10**6

G = int(sys.stdin.readline())
I = [int(sys.stdin.readline()) for _ in range(G)]

# marking pairwise differences
D = [False]*N
for i in range(G):
    for j in range(i+1,G):
        D[abs(I[i]-I[j])] = True

# kinda-sieving for first number that has no marked multiple
m = 0
good = False
while not good:
    m += 1
    good = True
    for k in range(m,N,m):
        if D[k]:
            good = False
            break
sys.stdout.write('%d\n' % m)
