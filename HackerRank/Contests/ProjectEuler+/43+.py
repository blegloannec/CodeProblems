#!/usr/bin/env python

import sys

# permutation suivante (ordre lex) d'un tableau quelconque
# (repetitions autorisees)
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

def divitest(T,N):
    P = [2,3,5,7,11,13,17]
    for i in xrange(1,N-1):
        if (100*T[i]+10*T[i+1]+T[i+2])%P[i-1]!=0:
            return False
    return True

def tab2num(T):
    res = 0
    for t in T:
        res = 10*res+t
    return res

def main():
    N = int(sys.stdin.readline())
    res = 0
    T = range(N+1)
    while next_permutation(T):
        if divitest(T,N):
            res += tab2num(T)
    print res

main()
