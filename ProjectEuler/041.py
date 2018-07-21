#!/usr/bin/env python

from math import sqrt

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

# simple inversion de la relation d'ordre sur les T[i]
def prev_permutation(T):
    pivot = len(T)-2
    while pivot>=0 and T[pivot]<=T[pivot+1]:
        pivot -= 1
    if pivot<0:
        return False
    swap = len(T)-1
    while T[swap]>=T[pivot]:
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
    for n in range(4,10):
        T = range(n,0,-1)
        while prev_permutation(T):
            p = tab2num(T)
            if prime(p):
                res = p
                break
    print res

main()
