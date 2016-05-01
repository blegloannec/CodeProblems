#!/usr/bin/env python

import sys

def main():
    T = int(sys.stdin.readline())
    for t in range(1,T+1):
        N = int(sys.stdin.readline())
        cpt = {}
        for _ in xrange(2*N-1):
            L = map(int,sys.stdin.readline().split())
            for k in L:
                if k in cpt:
                    cpt[k] += 1
                else:
                    cpt[k] = 1
        sol = []
        for k in cpt:
            if cpt[k]%2==1:
                sol.append(k)
        print 'Case #%d: %s' % (t,' '.join(map(str,sorted(sol))))

main()
