#!/usr/bin/env python

import sys
from math import sqrt
from bisect import *

def next_permutation(T):
    pivot = len(T)-2
    while pivot>=0 and T[pivot]>=T[pivot+1]:
        pivot -= 1
    if pivot<0:
        return False
    swap = len(T)-1
    while T[swap]<=T[pivot]:
        swap -= 1
    T[swap],T[pivot] = T[pivot],T[swap]
    i = pivot+1
    j = len(T)-1
    while i<j:
        T[i],T[j] = T[j],T[i]
        i += 1
        j -= 1
    return True

def prime(n):
    if n%2==0:
        return False
    for i in xrange(3,int(sqrt(n))+1,2):
        if n%i==0:
            return False
    return True

def tab2num(T):
    res = 0
    for t in T:
        res = 10*res+t
    return res

def main():
    PP = []
    for n in xrange(4,8):
        T = range(1,n+1)
        while next_permutation(T):
            p = tab2num(T)
            if prime(p):
                PP.append(p)
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        N = int(sys.stdin.readline())
        p = bisect_right(PP,N)
        if p==0:
            print -1
        else:
            print PP[p-1]

main()
