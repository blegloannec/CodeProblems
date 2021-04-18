#!/usr/bin/env pypy

from fractions import gcd
from collections import defaultdict

memo = {}
def cnt(q, s1,s2):
    if s1<0 or s2<0:
        return 0
    if q>=Q:
        return 1 if s1==s2==0 else 0
    K = (q,s1,s2)
    if K not in memo:
        if A1[q]==A2[q]:
            memo[K] = cnt(q+1, s1,s2) + cnt(q+1, s1-1,s2-1)
        else:
            memo[K] = cnt(q+1, s1-1,s2) + cnt(q+1, s1,s2-1)
    return memo[K]

def main():
    global Q, A1,A2
    T = int(raw_input())
    for t in xrange(1, T+1):
        N,Q = map(int, raw_input().split())
        assert N<=2
        A1,S1 = raw_input().split()
        A1 = list(A1)
        S1 = int(S1)
        if N==1:
            A2 = A1[:]
            S2 = S1
        else:
            A2,S2 = raw_input().split()
            A2 = list(A2)
            S2 = int(S2)
        Pairs = defaultdict(list)
        for i in xrange(Q):
            Pairs[A1[i]+A2[i]].append(i)
        E = 0
        Ans = [None]*Q
        cntAll = cnt(0, S1,S2)
        memo.clear()
        for pair,Idx in Pairs.items():
            A1[0],A1[Idx[0]] = A1[Idx[0]],A1[0]
            A2[0],A2[Idx[0]] = A2[Idx[0]],A2[0]
            cntT = cnt(1, S1-(pair[0]=='T'),S2-(pair[1]=='T'))
            memo.clear()
            A1[0],A1[Idx[0]] = A1[Idx[0]],A1[0]
            A2[0],A2[Idx[0]] = A2[Idx[0]],A2[0]
            cntF = cntAll-cntT
            if cntT>cntF:
                ans = 'T'
                E += cntT*len(Idx)
            else:
                ans = 'F'
                E += cntF*len(Idx)
            for i in Idx:
                Ans[i] = ans
        g = gcd(E, cntAll)
        print('Case #{}: {} {}/{}'.format(t, ''.join(Ans), E/g, cntAll/g))

main()
