#!/usr/bin/env python3

def label(x):
    L = []
    while x>0:
        x,c = divmod(x-1, 26)
        L.append(chr(c+ord('A')))
    return ''.join(reversed(L))

def number(L):
    x = 0
    for c in L:
        x = 26*x + ord(c)-ord('A') + 1
    return x

def opposite(X):
    return label(int(X)) if '0'<=X[0]<='9' else str(number(X))

N = int(input())
print(' '.join(opposite(X) for X in input().split()))
