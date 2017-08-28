#!/usr/bin/env python3

import sys
from collections import defaultdict

# Si un facteur w est present au moins 2 fois dans u, alors numerotons ces
# positions :
# u = _.w.s1 = _.w.s2 = ...
# et supposons que w est "le plus grand facteur commun a ces positions",
# i.e. que les si ne commencent pas tous par la meme lettre.
# Alors :
#  - les w.si sont tous dans l'arbre (par definition)
#  - il existe un noeud correspondant exactement a la lecture de w depuis
#    la racine (car il y a au moins deux chemins w.si et w.sj qui se
#    distinguent en la premiere lettre de si/sj)
# Le motif recherche correspond donc a un plus grand chemin (au sens de la
# taille du mot correspondant) depuis la racine jusqu'a un sommet de l'arbre
# tel que le sous-arbre enracine en ce point contienne au moins k feuilles.

# renvoie le nombre de feuilles et un plus grand mot du sous arbre enracine
# en u
def dfs(S,T,k,u,w=''):
    if u not in T:  # leaf
        return 1,''
    l,b = 0,''
    for (v,i,j) in T[u]:
        lv,bv = dfs(S,T,k,v,w+S[i:i+j])
        l += lv
        if len(bv)>len(b):
            b = bv
    if l>=k and len(w)>len(b):
        b = w
    return l,b

def main():
    S = input()
    k = int(input())
    T = defaultdict(list)
    u0 = None  # racine
    for L in sys.stdin.readlines():
        u,v,i,l = L.split()
        # on suppose que la racine est le premier sommet de la liste
        if u0==None:
            u0 = u
        i,l = int(i)-1,int(l)
        T[u].append((v,i,l))
    _,w = dfs(S,T,k,u0)
    print(w)

main()
