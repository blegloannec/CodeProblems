#!/usr/bin/env python

import sys

def sol(S):
    maxt = [0 for i in xrange(len(S))]
    maxt[-1] = S[-1]
    for i in xrange(len(S)-2,-1,-1):
        maxt[i] = max(S[i],maxt[i+1])
    res = [S[0]]
    for i in xrange(1,len(S)):
        if S[i]>=res[0]:
            res = [S[i]]+res
        else:
            res.append(S[i])
    return ''.join(map(chr,res))


def main():
    T = int(sys.stdin.readline())
    for t in range(1,T+1):
        S = map(ord,sys.stdin.readline().strip())
        print 'Case #%d: %s' % (t,sol(S))

main()
