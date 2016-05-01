#!/usr/bin/env python

import sys

def bords(W):
    B = [0 for _ in xrange(len(W)+1)]
    for i in xrange(1,len(W)):
        k = B[i]
        while W[k]!=W[i] and k>0:
            k = B[k]
        if W[k]==W[i]:
            B[i+1] = k+1
        else:
            B[i+1] = 0
    return B

def main():
    T = int(sys.stdin.readline())
    for t in range(1,T+1):
        K,L,S = map(int,sys.stdin.readline().split())
        Keyboard = sys.stdin.readline().strip()
        # occurrences dans le clavier pour proba de chaque lettre
        Cpt = {}
        for k in Keyboard:
            if k in Cpt:
                Cpt[k] += 1
            else:
                Cpt[k] = 1
        Target = sys.stdin.readline().strip()
        # KMP pour calcul des bords max de la cible
        B = bords(Target)
        max_occ = (S-B[-1])/(L-B[-1])
        # proba d'avoir le mot cible en position i fixee
        # dans le mot ecrit par le singe
        proba_target = 1.
        for c in Target:
            if not (c in Cpt):
                # il manque une lettre de la cible au clavier !
                proba_target = 0.
                max_occ = 0
                break
            proba_target *= float(Cpt[c])/K
        # par linearite de l'esperance
        exp_occ = proba_target*(S-L+1)
        print 'Case #%d: %f' % (t,max_occ-exp_occ)

main()
