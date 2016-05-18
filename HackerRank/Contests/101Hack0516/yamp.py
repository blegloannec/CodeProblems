#!/usr/bin/env python

import sys

# soit k le plus grand poids d'un bit qui n'est pas uniforme
# dans l'ensemble de nombres
# soit A/B l'ensemble des nombres pour lequel ce bit vaut 0/1
# le xor de 2 elements de A/B entre-eux est <2^k
# le xor d'un element de A avec un element de B est >=2^k
# dans une permutation, il y aura forcement un element de A
# a cote d'un element de B, c'est donc ce genre de transition qu'il
# faut minimiser
# il y a exactement un tel couple si on range tout A, puis tout B
# il suffit de choisir le couple de AxB pour lequel le xor est
# minimal pour la transition A/B

def main():
    n = int(sys.stdin.readline())
    A = map(int, sys.stdin.readline().split())
    k = None
    i = 30
    while i>=0 and k==None:
        v = (A[0]>>i)&1
        for j in xrange(1,n):
            if (A[j]>>i)&1 != v:
                k = i
                break
        i -= 1
    if k==None:
        print 0
    else:
        x = 1<<30
        for a in xrange(n):
            for b in xrange(a+1,n):
                if (A[a]>>k)&1 != (A[b]>>k)&1:
                    x = min(x,A[a]^A[b])
        print x

main()
