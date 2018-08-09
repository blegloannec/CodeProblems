#!/usr/bin/env python

import sys

def main():
    N,K = map(int,sys.stdin.readline().split())
    S = map(int,list(sys.stdin.readline().strip()))
    M,P = [S[0]],[S[0]]
    for i in xrange(1,N):
        M.append(S[i]^P[i-1]^(0 if i-K<0 else P[i-K]))
        P.append(P[i-1]^M[i])
    print ''.join(map(str,M))

main()
