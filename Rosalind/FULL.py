#!/usr/bin/env python3

import sys, rosalib

def arrondi(x):
    return round(x,5)

L = sys.stdin.readlines()
Wtot = float(L[0])  # masse de la proteine complete
W = sorted(float(L[i]) for i in range(1,len(L)))
# W contient les masses des prefixes et des suffixes.
# Si le troncon de proteine recherche est de taille n
# alors on a n+1 emplacements de coupe, donc n+1 prefixes
# et n+1 suffixes, donc 2(n+1) masses dans W.
# Prendre le miroir de la proteine echange prefixes/suffixes.
# On pourra donc supposer que W[0] est la masse du plus petit prefixe
# (le w1 de l'enonce).
# Si wp est la masse d'un prefixe et ws la masse du suffixe complementaire,
# alors wp + ws = Wtot. Donc trier les elements permet de former les paires
# (la ieme plus petite masse a pour complementaire la ieme plus grande).

# dans SPEC on faisait une recherche dichotomique, ici pour changer
# utiliser un dictionnaire et des arrondis des masses
PW = {arrondi(rosalib.W[a]):a for a in rosalib.W}

Sol = []
used = [False]*(len(W)//2)
def backtrack(i,wcurr):
    if i==len(W)-1:
        return ''.join(Sol)
    if i<len(W)//2:
        # premiere moitie de liste, plus petites masses de chaque paire
        assert(not used[i])
        w = arrondi(W[i]-wcurr)
        if w in PW:
            # on peut prendre la masse en prefixe, on essaye et on continue
            used[i] = True
            Sol.append(PW[w])
            X = backtrack(i+1,W[i])
            if X!=None:
                return X
            Sol.pop()
            used[i] = False
        # on essaye sans prendre cette masse comme prefixe, en la considerant
        # donc comme suffixe, sa masse complementaire DEVRA etre prefixe
        X = backtrack(i+1,wcurr)
        if X!=None:
            return X
    else:
        j = len(W)-1-i
        if not used[j]:
            # la masse complementaire a ete consideree comme suffixe,
            # on DOIT prendre cette masse comme prefixe
            w = arrondi(W[i]-wcurr)
            if w in PW:
                # inutile de mettre a jour used ici...
                Sol.append(PW[w])
                X = backtrack(i+1,W[i])
                if X!=None:
                    return X
                Sol.pop()
            # sinon return None implicite
        else:
            # la masse courante a deja ete consideree comme suffixe,
            # on l'ignore et on continue
            return backtrack(i+1,wcurr)

print(backtrack(1,W[0]))
