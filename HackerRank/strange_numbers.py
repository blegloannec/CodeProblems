#!/usr/bin/env python3

from math import *

def gen_strange():
    S = list(range(10))
    for l in range(2,19):
        i = lx = 0
        while i<len(S) and lx<=l:
            x = S[i]*l
            lx = ceil(log10(x+1))
            # NB (after benchmark for ints of size ~10^18):
            #  - slightly faster than len(str(x))
            #  - significantly faster than ceil(log(x+1,10))
            if lx==l:
                S.append(x)
            i += 1
    return S

if __name__=='__main__':
    S = gen_strange()
    T = int(input())
    for _ in range(T):
        L,R = map(int,input().split())
        # |S| ~ 300, we drop the binary search
        print(sum(int(L<=x<=R) for x in S))
