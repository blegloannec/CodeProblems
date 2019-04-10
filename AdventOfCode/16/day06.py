#!/usr/bin/env python

import sys

def main():
    C = None
    for M in sys.stdin.readlines():
        M = M.strip()
        if C==None:
            C = [[0 for _ in xrange(26)] for _ in xrange(len(M))]
        for i in xrange(len(M)):
            C[i][ord(M[i])-ord('a')] += 1
    M1,M2 = [],[]
    for i in xrange(len(C)):
        A = [(C[i][j],j) for j in xrange(26)]
        M1.append(chr(max(A)[1]+ord('a')))
        M2.append(chr(min(A)[1]+ord('a')))
    print ''.join(M1)
    print ''.join(M2)

main()
