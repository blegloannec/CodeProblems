#!/usr/bin/env python

import sys

T = int(sys.stdin.readline())
for t in range(1,T+1):
    mot = sys.stdin.readline().strip()
    d = {}
    cpt = 1
    for c in mot:
        if c not in d: # interpretation minimale des symboles
            d[c] = cpt
            if cpt==1: # le premier symbole sera 1
                cpt = 0 # le deuxieme 0
            elif cpt==0:
                cpt = 2 # le troisieme 2, car 1 deja utilise
            else:
                cpt += 1 # les suivants pris dans l'ordre croissant
    # choix d'une base minimale d'interpretation
    base = max(2,len(d)) # unaire interdit !
    res = 0
    for c in mot: # interpretation
        res = base*res+d[c]
    print 'Case #%d: %d' % (t,res)
