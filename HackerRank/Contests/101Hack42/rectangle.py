#!/usr/bin/env python

import sys

def main():
    q = int(sys.stdin.readline())
    for _ in xrange(q):
        n = int(sys.stdin.readline())
        X,Y = [],[]
        for _ in xrange(n):
            x,y = map(int,sys.stdin.readline().split())
            X.append(x)
            Y.append(y)
        xmin,xmax = min(X),max(X)
        ymin,ymax = min(Y),max(Y)
        print 'YES' if all(((x in [xmin,xmax] and ymin<=y<=ymax) or (y in [ymin,ymax] and xmin<=x<=xmax)) for (x,y) in zip(X,Y)) else 'NO'

main()
