#!/usr/bin/env python3

import sys, bisect

def case(A,Q):
    S = [float('-inf'), float('inf')]
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            S.append(A[i]+A[j])
    S.sort()
    for q in Q:
        i = bisect.bisect_left(S,q)
        s = S[i] if S[i]-q<=q-S[i-1] else S[i-1]
        print('Closest sum to %d is %d.' % (q,s))

def main():
    I = list(map(int,sys.stdin.readlines()))
    c = 1
    i = 0
    while i<len(I):
        n = I[i]
        A = I[i+1:i+1+n]
        i += n+1
        m = I[i]
        Q = I[i+1:i+1+m]
        i += m+1
        print('Case %d:' % c)
        case(A,Q)
        c += 1

main()
