#!/usr/bin/env python3

from collections import Counter

def valid(S):
    C = Counter(S)
    CC = Counter(C[c] for c in C) # counting the counter is a nice trick here!
    # it leads to way simpler conditions than the 3 editorial solutions
    if len(CC)==2:
        a,b = sorted(CC)
        return (a+1==b and CC[b]==1) or (a==1 and CC[a]==1)
    return len(CC)==1

print('YES' if valid(input()) else 'NO')
