#!/usr/bin/env python3

from collections import *

N = 15
All = (1<<N)-1

def bfs(Spies,Attr):
    Pred = {}
    Q = deque([(frozenset(a for a in Attr),All)])
    while Q:
        A,Sus = Q.popleft()
        if Sus==Spies or Sus&Spies==0:
            break
        for a in A:
            I = Sus&Attr[a]
            if I and (I&Spies==I or I&Spies==0):
                K = (frozenset(b for b in A if b!=a),Sus^I)
                if K not in Pred:
                    Pred[K] = (A,Sus,('NOT ' if I&Spies==0 else '')+a)
                    Q.append(K)
    Sol = []
    while (A,Sus) in Pred:
        A,Sus,a = Pred[A,Sus]
        Sol.append(a)
    return Sol[::-1]

def main():
    SpiesNames = set(input().split())
    Spies = 0
    Attr = defaultdict(int)
    for i in range(N):
        L = input().split()
        if L[0] in SpiesNames:
            Spies |= 1<<i
        for a in L[2:]:
            Attr[a] |= 1<<i
    print('\n'.join(bfs(Spies,Attr)))

main()
