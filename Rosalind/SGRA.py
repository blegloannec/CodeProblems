#!/usr/bin/env python3

import sys, rosalib

def arrondi(x):
    return round(x,4)

# dictionaire des masses des AA
PW = {arrondi(rosalib.W[a]):a for a in rosalib.W}

# le graphe est un DAG dont les masses triees par ordre croissant
# forment un tri topologique
W = sorted(float(L) for L in sys.stdin.readlines())
G = [[] for _ in range(len(W))]
# construction des aretes
for i in range(len(W)):
    for j in range(i+1,len(W)):
        w = arrondi(W[j]-W[i])
        if w in PW:
            G[i].append((j,PW[w]))  # on ajoute l'AA comme etiquette du lien

# prog. dyn. sur le DAG suivant l'ordre topo inverse pour calculer
# une plus grande chaine
L = [0]*len(W)        # longueur de la plus grande chaine demarrant en i
Succ = [None]*len(W)  # un successeur optimal possible
i0 = len(W)-1         # un depart d'une plus grande chaine
for i in range(len(W)-2,-1,-1):
    # on calcule L[i]
    for (j,a) in G[i]:
        if L[j]+1>L[i]:
            L[i] = L[j]+1
            Succ[i] = (j,a)
    # on met a jour le meilleur
    if L[i]>L[i0]:
        i0 = i

# construction d'une plus grande proteine
P = []
while Succ[i0]!=None:
    i0,a = Succ[i0]
    P.append(a)
print(''.join(P))
