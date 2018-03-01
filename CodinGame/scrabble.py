#!/usr/bin/env python3

from collections import Counter

P = [1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10]

def incl(C1,C2):
    return all(C1[c]<=C2[c] for c in C1)

def score(C):
    return sum(C[c]*P[ord(c)-ord('a')] for c in C)

n = int(input())
W = []
for i in range(n):
    w = input()
    c = Counter(w)
    W.append((w,c,(score(c),-i)))
L = Counter(input())

print(max(W,key=(lambda X: X[2] if incl(X[1],L) else (0,0)))[0])
