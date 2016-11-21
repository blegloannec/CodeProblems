#!/usr/bin/env python

import sys

# Verification de la seconde propriete en O(n*log(n)) :
# on trie l'ensemble et pour tout k <= n/2
# on verifie simplement que la plus grande somme d'un ensemble
# de taille k-1 est stritement plus petite que la plus petite
# somme d'un ensemble de taille k

# Verification de la premiere propriete :
# meme en admettant la seconde propriete et en utilisant le
# meta-testing du pb 106, il y a trop d'ensembles (presque 10^9)
# a comparer.
# Mais il y a une actuce car les elements sont <= 10^6
# donc la somme de tout sous-ensemble <= n*10^6
# et le nb de sous-ensembles est 2^n
# donc on doit avoir n*10^6 >= 2^n, sinon on a forcement
# 2 sous-ensembles de meme somme.
# cela impose en fait n <= 25 !
# ce qui ne fait au pire que 2^25 ~ 32*10^6 sous-ensembles
# dont on peut calculer et stocker les sommes...

def condition2(A):
    S1,S2 = A[0],0
    i1,i2 = 1,len(A)-1
    while i1<i2:
        S1 += A[i1]
        S2 += A[i2]
        if S1<S2:
            return False
        i1 += 1
        i2 -= 1
    return True

def condition1(A):
    S = set([0])
    for a in A:
        L = list(S)
        for s in L:
            s0 = s+a
            if s0 in S:
                return False
            S.add(s0)
    return True

def main():
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        n = int(sys.stdin.readline())
        A = map(int,sys.stdin.readline().split())
        A.sort()
        S = sum(A)
        if len(set(A))<n or S<2**n or not condition2(A) or not condition1(A):
            print 'NO'
        else:
            print 'YES'

main()
