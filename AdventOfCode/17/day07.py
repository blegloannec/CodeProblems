#!/usr/bin/env python3

import sys
from collections import defaultdict

I = sys.stdin.readlines()

def parse_tree(I):
    T = {}
    W = {}
    for L in I:
        C = L.strip().split(' -> ')
        l = C[0].split()
        name = l[0]
        num = int(l[1][1:-1])
        W[name] = num
        r = C[1].split(', ') if len(C)>1 else []
        T[name] = r
    # root
    R = {u for u in T}
    for u in T:
        for v in T[u]:
            R.remove(v)
    assert(len(R)==1)
    R = R.pop()
    return T,W,R

def dfs_weight(T,W,u):
    if len(T[u])==0:  # leaf
        return W[u]
    wv = defaultdict(list)
    for v in T[u]:
        wv[dfs_weight(T,W,v)].append(v)
    if len(wv)==1:
        w = next(w for w in wv)
    else:
        # exactly one of the children weights is wrong
        assert(len(wv)==2)
        w,werr = (w for w in wv)
        if len(wv[w])<len(wv[werr]):
            w,werr = werr,w
        assert(len(wv[werr])==1)
        # and to know which one we must have several right children
        assert(len(wv[w])>1)
        verr = wv[werr][0]
        print('%s: %d -> %d' % (verr,W[verr],W[verr]+w-werr))
    return w*len(T[u])+W[u]

T,W,R = parse_tree(I)
print(R)           # Part 1
dfs_weight(T,W,R)  # Part 2
