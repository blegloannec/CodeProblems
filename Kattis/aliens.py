#!/usr/bin/env python3

import sys
input = sys.stdin.readline

def count_substrings(S, l, m):
    P = 10**9+9  # hash prime
    B = 29       # hash base
    Bl = pow(B, l, P)
    Cnt = {}
    h = 0
    last_idx = None
    for i,c in enumerate(S):
        h = (B*h + c) % P
        if i>=l:
            h = (h - S[i-l]*Bl) % P
        if i+1>=l:
            Cnt[h] = Cnt.get(h, 0) + 1
            if Cnt[h]>=m:
                last_idx = i-l+1
    return last_idx

def main():
    i = 1
    while True:
        M = int(input())
        if M==0:
            break
        S = [ord(c)-ord('a')+1 for c in input().strip()]
        l0, l1 = 1, len(S)
        while l0<l1:
            l = (l0+l1+1)//2
            if count_substrings(S, l, M) is not None:
                l0 = l
            else:
                l1 = l-1
        res = count_substrings(S, l0, M)
        if res is None:
            print('none')
        else:
            print(l0, res)

main()
