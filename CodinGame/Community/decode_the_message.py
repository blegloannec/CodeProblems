#!/usr/bin/env python3

def label(Alpha, x):
    L = []
    while x>0:
        x,a = divmod(x-1, len(Alpha))
        L.append(Alpha[a])
    return ''.join(L)

P = int(input())
Alpha = input()
print(label(Alpha, P+1))
