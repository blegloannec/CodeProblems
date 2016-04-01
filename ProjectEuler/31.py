#!/usr/bin/env python

import sys

V = [1,2,5,10,20,50,100,200]

memo = {}
def C(s,k):
    if s==0:
        return 1
    if k<0:
        return 0
    if (s,k) in memo:
        return memo[(s,k)]
    res = 0
    for ss in range(s,-1,-V[k]):
        res += C(ss,k-1)
    memo[(s,k)] = res
    return res

print C(200,len(V)-1)
