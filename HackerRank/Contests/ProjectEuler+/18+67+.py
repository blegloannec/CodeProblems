#!/usr/bin/env python

import sys
        
def path(M):
    N = len(M)
    for i in range(1,N):
        M[i][0] += M[i-1][0]
        for j in range(1,i+1):
            M[i][j] += max(M[i-1][j-1],M[i-1][j])
    return max(M[N-1])

def main():
    T = int(sys.stdin.readline())
    for t in xrange(T):
        N = int(sys.stdin.readline())
        M = [[0 for _ in xrange(N)] for _ in xrange(N)]
        for i in xrange(N):
            L = map(int,sys.stdin.readline().split())
            for j in xrange(len(L)):
                M[i][j] = L[j]
        print path(M)

main()
