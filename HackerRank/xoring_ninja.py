#!/usr/bin/env python

import sys

P = 10**9+7

def subset_xor_sum(A):
    # C[j] contient le nb de sous-ensembles dont le j-ieme bit
    # du xor des elements vaut 1
    C = [0]*30
    for i in xrange(len(A)):
        a = A[i]
        for j in xrange(len(C)):
            if a&1==0:
                # C[j] += C[j]
                C[j] = (2*C[j])%P
            else:
                # C[j] += 2**i-C[j]
                C[j] = pow(2,i,P)
            a >>= 1
    res = 0
    for j in xrange(len(C)):
        res = (res + C[j]*pow(2,j,P))%P
    return res  

def main():
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        n = int(sys.stdin.readline())
        A = map(int,sys.stdin.readline().split())
        print subset_xor_sum(A)

main()
