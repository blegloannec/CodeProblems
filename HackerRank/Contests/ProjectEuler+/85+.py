#!/usr/bin/env python

import sys
from math import sqrt
from bisect import *

# rectangle caracterise par {x,x'} et {y,y'}
# nb rect = (2 parmi X) * (2 parmi Y)
# nb_rect > x^2/2
def nb_rect(x,y):
    return x*(x+1)*y*(y+1)/4

def main():
    N = 2000001
    R = []
    # borne sup sur x
    for x in xrange(1,int(sqrt(2*N))+1):
        for y in xrange(1,x+1):
            n = nb_rect(x,y)
            # on stocke pas les valeurs trop grandes
            if n>N+100:
                break
            R.append((nb_rect(x,y),x*y))
    R.sort()
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        target = int(sys.stdin.readline())
        i = bisect_left(R,(target,0))
        d = abs(target-R[i-1][0])
        m = R[i-1][1]
        while abs(target-R[i][0])<=d:
            if abs(target-R[i][0])<d:
                d = abs(target-R[i][0])
                m = R[i][1]
            else:
                m = max(m,R[i][1])
            i += 1
        print m

main()
