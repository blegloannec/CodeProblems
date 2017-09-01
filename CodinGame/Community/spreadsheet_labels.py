#!/usr/bin/env python3

def label(x):
    k = 0
    p = 1
    while x>=p:
        x -= p
        k += 1
        p *= 26
    L = []
    for _ in range(k):
        L.append(chr(x%26+ord('A')))
        x //= 26
    return ''.join(reversed(L))

def number(L):
    x = 0
    for c in L:
        x = 26*x + ord(c)-ord('A')
    return x + (26**len(L)-1)//25

def opposite(X):
    if '0'<=X[0]<='9':
        return label(int(X))
    else:
        return number(X)

n = int(input())
print(' '.join(str(opposite(X))  for X in input().split()))
