#!/usr/bin/env python

# rather naive approach
# runs in < 2 mins with pypy

def pan(n,b):
    C = [False for _ in xrange(b)]
    cpt = 0
    while n>0 and cpt<b:
        d = n%b
        if not C[d]:
            C[d] = True
            cpt += 1
        n /= b
    return (cpt==b)

def superpan(n,b):
    for i in xrange(b,1,-1):
        if not pan(n,i):
            return False
    return True

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

def gen(b):
    cpt = 0
    s = 0
    A = [0]+range(b-1,0,-1)
    while cpt<10 and next_permutation(A):
        n = 0
        for i in xrange(b):
            n = b*n+A[i]
        if superpan(n,b-1):
            #print n
            s += n
            cpt += 1
    return s

print gen(12)
