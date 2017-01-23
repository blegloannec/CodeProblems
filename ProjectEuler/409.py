#!/usr/bin/env python

# Le pb n'a pas de lien "direct" avec Nim...
# Il s'agit de compter le nb de configurations de n tas dont les
# valeurs sont *distinctes* et comprises entre 1 et 2^n-1 dont le
# xor est =/= 0.

# Une remarque en passant :
# Considerons E = {1,...,2^n-1} l'ensemble de valeurs possibles
# pour les tas, et posons B = {2^0,2^1,...,2^(n-1)} les puissances
# de 2 dans E (i.e. les valeurs avec exactement 1 bit a 1) et A = E\B.
# Si X est inclu dans E, alors X est parfaitement caracterise par
# XA = X inter A et xor(X), car on sait alors exactement completer
# XA en X avec des elements de B en calculant xor(XA) xor xor(X)...

# Construisons les configurations element par element (distincts).
# Une configuration de xor non nul peut soit contenir son xor,
# soit pas. Ajoutons un nouvel element.
# Dans le premier cas on peut ajouter n'importe quel nouvel element, on
# arrivera toujours a un xor non nul.
# Dans le second cas, on peut tout ajouter sauf le xor pour eviter
# le xor nul.
# Une configuration du premier type est toujours une configuration
# de xor nul + un element valant le xor.

P = 10**9+7

n = 10**7
N = pow(2,n,P)-1 # nb de valeurs possibles (1 a 2^n-1)
C,NZ,NZX,Z = 1,0,0,1
for k in xrange(n): # confs a k+1 elements
    # confs de xor non nul
    NZ = ( (Z+NZX)*(N-k) + (NZ-NZX)*(N-k-1) )%P
    # confs de xor non nul contenant leur xor
    # (on insere le xor dans une conf de xor nul)
    NZX = ((((k+1)*Z)%P)*(N-k))%P
    # nb total de confs
    C = (C*(N-k))%P
    # confs de xor nul
    Z = (C-NZ)%P
print NZ
