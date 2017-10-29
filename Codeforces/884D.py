#!/usr/bin/env python3

from heapq import *

def score(A):
    heapify(A)
    res = 0
    if len(A)%2==0:
        a0,a1 = heappop(A),heappop(A)
        a = a0+a1
        res += a
        heappush(A,a)
    while len(A)>1:
        a0,a1,a2 = heappop(A),heappop(A),heappop(A)
        a = a0+a1+a2
        res += a
        heappush(A,a)
    return res

def main():
    n = int(input())
    A = list(map(int,input().split()))
    print(score(A))

main()
