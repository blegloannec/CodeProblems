#!/usr/bin/python

import sys

def progdyn(M):
    N = len(M)
    for i in range(1,N):
        M[0][i] += M[0][i-1]
        M[i][0] += M[i-1][0]
    for i in range(1,N):
        for j in range(1,N):
            M[i][j] += min(M[i-1][j],M[i][j-1])
    return M[N-1][N-1]

def main():
    N = int(sys.stdin.readline())
    M = []
    for _ in range(N):
        M.append(map(int,sys.stdin.readline().split()))
    print progdyn(M)

main()
