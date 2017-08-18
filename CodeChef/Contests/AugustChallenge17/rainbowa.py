#!/usr/bin/env python3

from itertools import groupby
Uniq = list(range(1,8))+list(range(6,0,-1))

def rainbow(A):
    return A==A[::-1] and [G[0] for G in groupby(A)]==Uniq
    
def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int,input().split()))
        print('yes' if rainbow(A) else 'no')

main()
