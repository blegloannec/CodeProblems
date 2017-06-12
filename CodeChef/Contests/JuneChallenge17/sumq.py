#!/usr/bin/env python3

from bisect import *

P = 10**9+7

def main():
    T = int(input())
    for _ in range(T):
        p,q,r = map(int,input().split())
        A = list(map(int,input().split()))
        B = list(map(int,input().split()))
        C = list(map(int,input().split()))
        A.sort()
        C.sort()
        SA,SC = A[:],C[:]
        for i in range(1,p):
            SA[i] += SA[i-1]
        for i in range(1,r):
            SC[i] += SC[i-1]
        res = 0
        for y in B:
            i = bisect_right(A,y)
            j = bisect_right(C,y)
            if i>0 and j>0:
                res = (res + ((j*(SA[i-1]*y)%P)%P + ((i*(j*(y*y)%P)%P)%P + (SA[i-1]*SC[j-1] + (i*(SC[j-1]*y)%P)%P)%P)%P)%P)%P
        print(res)

main()
