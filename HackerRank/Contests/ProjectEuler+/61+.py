#!/usr/bin/env python

import sys
from collections import defaultdict

Nums = [[n*(n+1)/2 for n in range(45,141)],
        [n*n for n in range(32,100)],
        [n*(3*n-1)/2 for n in range(26,82)],
        [n*(2*n-1) for n in range(23,71)],
        [n*(5*n-3)/2 for n in range(21,64)],
        [n*(3*n-2) for n in range(19,59)]]

def split(n):
    return (n/100,n%100)

# recursive generator using Heap's algo, quite ugly
# better in python 3: syntax "yield from <recursive call>"
def heap(n,A):
    if n==1:
        yield A
    else:
        for i in xrange(n-1):
            for B in heap(n-1,A):
                yield B
            if n%2==0:
                A[i],A[n-1] = A[n-1],A[i]
            else:
                A[0],A[n-1] = A[n-1],A[0]
        for B in heap(n-1,A):
            yield B

# other generator for fun
def loop(a0,P,i,x1):
    if i==len(P):
        if a0==x1:
            yield [a0]
    else:
        for y1 in Nums2[P[i]][x1]:
            for l in loop(a0,P,i+1,y1):
                l.append(x1)
                yield l
                
# ATTENTION: les categories de nb ne sont pas exclusives
# (un nb peut etre dans plusieurs categories)
# donc faire attention a bien eliminer les doublons
# en termes d'ensembles de nombres
                
def main():
    global Nums,Nums2
    Nums = map((lambda l: map(split,l)), Nums)
    Nums2 = [defaultdict(list) for _ in xrange(6)]
    for i in xrange(1,6):
        for x,y in Nums[i]:
            Nums2[i][x].append(y)
    T = int(sys.stdin.readline())
    X = map((lambda x: int(x)-3),sys.stdin.readline().split())
    Sol = set()
    S = []
    for i in xrange(len(Nums[X[0]])):
        a0,a1 = Nums[X[0]][i]
        for P in heap(T-1,X[1:]):
            for l in loop(a0,P,0,a1):
                # construction ne l'ensemble de nb correspondant
                E = []
                for j in xrange(len(l)):
                    E.append(l[j]*100+l[(j+1)%len(l)])
                if len(set(E))!=len(E):
                    # no duplicates allowed inside E
                    continue
                Sol.add(tuple(sorted(E)))
    S = []
    for e in Sol:
        S.append(sum(e))
    S.sort()
    for s in S:
        print s

main()
