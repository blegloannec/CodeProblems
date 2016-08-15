#!/usr/bin/env python

from collections import defaultdict

# Green Hackenbush on trees
# http://www.cs.cmu.edu/afs/cs/academic/class/15859-f01/www/notes/comb.pdf
# Une simple branche (chaine) est clairement equivalente a 1 tas de Nim
# de meme taille.
# Plusieurs simples branches de tailles n1,...,nk raccordees a un
# meme noeud sont equivalentes a un jeu de Nim a k tas de tailles
# nk, donc equivalentes a un jeu de Nim a 1 tas de taille xor(ni, i=1..k).
# Cela permet de reduire inductivement l'arbre a simple un nimber.

N = 10000
M = 10**18
Nimber = [0 for _ in xrange(N)]
Nimber[1] = 1
Moves = [defaultdict(int) for _ in xrange(N)]
Moves[1][0] = 1
def dp():
    for n in xrange(2,N):
        Nimber[n] = (Nimber[n-2]+1)^(Nimber[n-1]+1)
        # premier coup joue dans le sous-arbre d'ordre n-2
        for a in Moves[n-2]:
            x = (a+1)^(Nimber[n-1]+1)
            Moves[n][x] = (Moves[n][x]+Moves[n-2][a])%M
        # ou suppression complete de ce sous-arbre
        Moves[n][Nimber[n-1]+1] += 1
        # ou premier coup joue sur le sous-arbre d'ordre n-2
        for b in Moves[n-1]:
            x = (Nimber[n-2]+1)^(b+1)
            Moves[n][x] = (Moves[n][x]+Moves[n-1][b])%M
        # ou suppression complete de ce sous-arbre
        Moves[n][Nimber[n-2]+1] += 1
        # Ajout pour limiter l'utilisation memoire :
        Moves[n-2] = None

dp()
print Moves[-1][0]
