#!/usr/bin/env python

import sys

def optim(n,k,T):
    cpt = 0
    uncov = 0 # premiere position non couverte
    it = 0 # indice de la prochaine tour
    while uncov<n and it<len(T):
        if T[it]-k>=uncov:
            # prochaine tour trop loin pour couvrir uncov
            return -1
        while it<len(T) and T[it]-k<uncov:
            # on cherche la tour la plus a droite qui couvre encore uncov
            it += 1
        uncov = T[it-1]+k
        cpt += 1
    return (cpt if uncov>=n else -1)

def main():
    n,k = map(int,sys.stdin.readline().split())
    C = map(int,sys.stdin.readline().split())
    T = []
    for i in xrange(n):
        if C[i]==1:
            T.append(i)
    print optim(n,k,T)

main()
