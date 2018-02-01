#!/usr/bin/env python3

import sys

def find(x):
    if x not in T:
        return x
    T[x] = find(T[x])
    return T[x]

def union(x,y):
    T[find(y)] = find(x)

def main():
    global T
    I = sys.stdin.readlines()
    t = 0
    while t<len(I):
        G = []
        while t<len(I) and I[t].strip()!='%':
            G.append(I[t].split())
            t += 1
        t += 1
        T = {}
        H,W = len(G),len(G[0])
        for i in range(H):
            for j in range(W):
                for (vi,vj) in [(i+1,j-1),(i,j+1),(i+1,j),(i+1,j+1)]:
                    if vi<H and 0<=vj<W and G[i][j]==G[vi][vj] and find((i,j))!=find((vi,vj)):
                        union((i,j),(vi,vj))
        R = [[0]*W for _ in range(H)]
        C = 1
        for i in range(H):
            for j in range(W):
                i0,j0 = find((i,j))
                if not R[i0][j0]:
                    R[i0][j0] = C
                    C += 1
                R[i][j] = R[i0][j0]
        F = ['{:>'+str(len(str(max(R[i][j] for i in range(H)))))+'}' for j in range(W)]
        for i in range(H):
            print(' '.join(F[j].format(R[i][j]) for j in range(W)))
        print('%')

main()
