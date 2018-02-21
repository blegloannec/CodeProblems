#!/usr/bin/env python3

from collections import defaultdict

def disjoint_union(I):
    I.sort()
    U = []
    for (l,r) in I:
        if not U or l>U[-1][1]+1:
            U.append((l,r))
        elif r>U[-1][1]:
            l0,_ = U.pop()
            U.append((l0,r))
    return U

def raw_count(I):
    U = disjoint_union(I)
    return sum(r-l+1 for (l,r) in U)

def main():
    n,m,k = map(int,input().split())
    D = defaultdict(list)
    for _ in range(k):
        i,l,r = map(int,input().split())
        D[i].append((l,r))
    res = (n-len(D))*m
    for i in D:
        res += m-raw_count(D[i])
    print(res)

main()
