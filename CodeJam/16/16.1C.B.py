#!/usr/bin/env python

import sys

def main():
    T = int(sys.stdin.readline())
    for t in range(1,T+1):
        B,M = map(int,sys.stdin.readline().split())
        if M>(1<<(B-2)):
            print 'Case #%d: IMPOSSIBLE' % (t)
        else:
            G = [[0 for j in xrange(B)] for i in xrange(B)]
            # we create 2^(i-1) paths between u_0 and u_i
            for i in xrange(B-1):
                for j in xrange(i+1,B-1):
                    G[i][j] = 1
            D = []
            m = M-1 # to have at most B-2 bits to consider
            while m>0:
                D.append(m%2)
                m /= 2
            for i in xrange(len(D)):
                if D[i]:
                    # we connect directly u_(i+1) to 
                    # there are 2^i paths from u_0 to u_(i+1)
                    # this adds 2^i paths from u_0 to u_(B-1)
                    G[i+1][B-1] = 1
            G[0][B-1] = 1 # last path
            print 'Case #%d: POSSIBLE' % (t)
            for l in G:
                print ''.join(map(str,l))

main()
