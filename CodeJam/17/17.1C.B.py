#!/usr/bin/env python3

# On commence par construire une solution minimale en nb de changements
# de la facon suivante (apres un tri des activites) :
# - lorsque 2 activites consecutives concernent la meme personne, on
#   compte l'intervalle intermediaire dans le temps alloue a cette personne,
#   on n'y fait pas d'echange pour l'instant et l'on retient la taille
#   de cet intervalle dans une liste des intervalles libres alloues a cette
#   personne ;
# - lorsque 2 activites consecutives ne concernent pas la meme personne, on
#   fait un echange et l'on ne compte l'intervalle intermediaire pour personne
#   (c'est une marge libre d'ajustement entre les 2 personnes).
# Cette solution est optimale en nb d'echanges, mais elle n'est pas acceptable
# ssi l'une des 2 personnes, disons A, a un temps alloue > 720, il faut alors
# allouer du temps a B en prelevant parmi les intervalles libres alloues a A.
# On trie donc ces intervalles par tailles decroissantes et on les attribue de
# facon gloutonne a B (en comptant 2 echanges supplementaires par intervalle)
# jusqu'a ce que le temps alloue a A tombe a 720.

def main():
    T = int(input())
    for t in range(1,T+1):
        nbA,nbB = map(int,input().split())
        A = []
        for _ in range(nbA):
            b,e = map(int,input().split())
            A.append((b,e,0))
        for _ in range(nbB):
            b,e = map(int,input().split())
            A.append((b,e,1))
        A.sort()
        cpt = 0     # nb d'echanges
        X = [0,0]   # temps alloue a chaque personne lors de la premiere passe
        F = [[],[]] # intervalles libres alloues a chaque personne lors de la premiere passe
        margin = 0  # marge libre d'ajustement
        curr,x = A[0][0],A[0][2]
        x0 = x
        for i in range(len(A)):
            b,e,y = A[i]
            if y==x: # activites consecutives pour la meme personne
                if b-curr>0:
                    F[x].append(b-curr)
                X[x] += e-curr
            else:    # echange
                cpt += 1
                x = y
                margin += b-curr
                X[x] += e-b
            curr = e
        # on ferme la boucle
        if x0==x: # pas d'echange entre le dernier et le premier intervalle
            d = A[0][0] + 24*60-A[-1][1]
            X[x] += d
            if d>0:
                F[x].append(d)
        else:     # echange (autour de minuit)
            cpt += 1
            margin += A[0][0] + 24*60-A[-1][1]
        assert(X[0]+X[1]+margin==24*60) # sanity check
        if X[0]>X[1]:
            X[0],X[1] = X[1],X[0]
            F[0],F[1] = F[1],F[0]
        # as always, STUPID MISTAKE here in the submitted code
        # (removed the margin from X[1]!...)
        if X[1]>720: # trop de temps alloue a une personne
            # on corrige de facon gloutonne
            D = X[1]-720
            F[1].sort(reverse=True)
            i = 0
            while D>0:
                D -= min(D,F[1][i])
                cpt += 2
                i += 1
        print('Case #%d: %d' % (t,cpt))

main()
