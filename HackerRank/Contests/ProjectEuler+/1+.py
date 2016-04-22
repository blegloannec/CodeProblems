#!/usr/bin/env python

import sys

def sumult(k,N):
    return k*(N/k)*(N/k+1)/2

def main():
    T = int(sys.stdin.readline())
    for t in xrange(T):
        N = int(sys.stdin.readline())-1
        # multiples de 3 + multiples de 5 - multiples de 15
        print sumult(3,N) + sumult(5,N) - sumult(15,N)

main()
