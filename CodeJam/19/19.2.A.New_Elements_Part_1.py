#!/usr/bin/env pypy

from fractions import Fraction

def slopes():
    S = set()
    for i in xrange(N):
        Ci,Ji = CJ[i]
        for j in xrange(i+1,N):
            Cj,Jj = CJ[j]
            if Ci!=Cj and Ji!=Jj:
                F = Fraction(Jj-Ji,Ci-Cj)
                if F>0:
                    S.add(F)
    return len(S)+1

if __name__=='__main__':
    T = int(raw_input())
    for t in xrange(1,T+1):
        N = int(raw_input())
        CJ = [tuple(map(int,raw_input().split())) for _ in xrange(N)]
        print 'Case #%d: %d' % (t,slopes())
