#!/usr/bin/env python

from math import sqrt

# inclusion-exclusion, runs in 8s with pypy

def sieve_list(N):
    P = [True for _ in xrange(N)]
    L = []
    P[0] = False
    P[1] = False
    for i in xrange(2,N):
        if P[i]:
            L.append(i)
            for k in xrange(2*i,N,i):
                P[k] = False
    return L

N = 2**50
P = sieve_list(2**25)

# genere tous les produits <N de k carres de nb premiers
# k<9 car 2^2 * 3^2 * ... * 23^2 > 2^50
def gen_prod(k,i=-1,n=1):
    if k==0:
        yield n
    else:
        for j in xrange(i+1,len(P)):
            # borne inf sur les nombres formes
            if n*P[j]**(2*k)>=N:
                break
            for x in gen_prod(k-1,j,n*P[j]**2):
                yield x

def main():
    s = 0
    # inclusion-exclusion pour compter les nb non-squarefree
    for k in xrange(1,9):
        s0 = 0
        for x in gen_prod(k):
            s0 += N/x
        s += s0 if k%2==1 else -s0
    print N-s

main()
