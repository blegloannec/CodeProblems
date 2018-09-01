#!/usr/bin/env python

import sys
sys.setrecursionlimit(3000)
from collections import defaultdict

P = 10**9+7

memo = {(0,0):1,(1,0):1}
def count(s,d):
    if (s,d) in memo:
        return memo[s,d]
    res = 0
    if s>0: # lettre simple a la fin
        res = (res + s*count(s-1,d))%P
    if d>0: # lettre double a la fin
        res = (res + d*(count(s+1,d-1)-count(s,d-1)))%P
    memo[s,d] = res
    return res

def main():
    q = int(sys.stdin.readline())
    for _ in xrange(q):
        n = int(sys.stdin.readline())
        A = map(int,sys.stdin.readline().split())
        D = defaultdict(int)
        for a in A:
            D[a] += 1
        s,d = 0,0 # simples & doubles
        for a in D:
            if D[a]==1:
                s += 1
            else:
                d += 1
        print count(s,d)

main()
