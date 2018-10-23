#!/usr/bin/env python3

from fractions import gcd

def period(A):
    if len(A)<2:
        return 0
    p = i = 0
    while i+1<len(A):
        i0 = i
        i += 1
        while i<len(A) and A[i]<0:
            i += 1
        d = i-i0
        D = A[i]-A[i0]
        if D>d:
            return -1
        p = gcd(p,d-D)  # updating p
    if p==0:
        return 0
    # checking the result
    if not all(A[i]<0 or (A[0]-1+i)%p+1==A[i] for i in range(len(A))):
        return -1
    return p

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int,input().split()))
        # removing leading and trailing -1
        while A and A[-1]<0:
            A.pop()
        i = 0
        while i<len(A) and A[i]<0:
            i += 1
        A = A[i:]
        # result
        p = period(A)
        print('inf' if p==0 else 'impossible' if p<0 else p)

main()
