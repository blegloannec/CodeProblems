#!/usr/bin/env python

import sys
from heapq import *

def main():
    T = int(sys.stdin.readline())
    for t in range(1,T+1):
        N = int(sys.stdin.readline())
        P = map(int,sys.stdin.readline().split())
        S = sum(P)
        H = [(-P[i],chr(i+ord('A'))) for i in xrange(len(P))]
        heapify(H)
        plan = []
        while len(H)>0:
            if len(H)==2 and H[0][0]==H[1][0]:
                for _ in xrange(-H[0][0]):
                    plan.append(H[0][1]+H[1][1])
                break
            else:
                a,A = heappop(H)
                plan.append(A)
                if a<-1:
                    heappush(H,(a+1,A))
        print 'Case #%d: %s' % (t,' '.join(plan))


main()
