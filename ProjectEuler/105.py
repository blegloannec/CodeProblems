#!/usr/bin/env python

import sys

def enum(n):
    i = 0
    s = []
    while n>0:
        if n&1:
            s.append(i)
        n >>= 1
        i += 1
    return s

def subsums(S):
    sums = []
    for s in xrange(1<<len(S)):
        ss = enum(s)
        sums.append((len(ss),sum(S[i] for i in ss)))
    return sums

def test(sums):
    for i in xrange(1,len(sums)):
        for j in xrange(i+1,len(sums)):
            if i&j==0:
                if sums[i][1]==sums[j][1]:
                    return False
                if sums[i][0]>sums[j][0] and sums[i][1]<sums[j][1]:
                    return False
                if sums[i][0]<sums[j][0] and sums[i][1]>sums[j][1]:
                    return False
    return True

def main():
    res = 0
    for l in sys.stdin.readlines():
        S = map(int,l.strip().split(','))
        if test(subsums(S)):
            res += sum(S)
    print res

main()
