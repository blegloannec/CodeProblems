#!/usr/bin/env python

import sys

# Pb tres basique avec une belle astuce dans le calcul de la complexite !
# L'idee est que si l'on simule betement, on descend dans X et Y (equipes
# comparees) en O(|X|+|Y|), mais on peut accelerer la descente en remarquant
# que si l'on connait les forces maximales FX et FY des combattants restant
# dans X et Y et les nb NX, NY de combattants restants ayant cette force, alors
# on est certain de faire k = min(NY/FX, NX/FY) etapes de ping-pong entre
# les 2 equipes a ce "palier de force", que l'on peut simuler en une seule
# etape. Ainsi on est certain de descendre strictement d'au moins un palier de
# force dans X ou Y a chaque etape de simulation. Si l'on note Fi les K forces
# considerees dans A et B et Ni le nb d'etapes (simulees) de descente associees,
# alors S = sum( Ni*Fi, 1<=i<=K ) = O(|A|+|B|)
# et la complexite est O(K) car on descend d'au moins un palier a chaque fois,
# ie. car a chaque pas on ajoute + kx*FX + ky*FY avec kx ou ky >= 1 a
# la somme et l'on est certain d'en avoir fini avec FX ou FY, d'ou O(K) etapes
# pour tout boucler.
# De plus une meme valeur est presente au plus 2 fois parmi les Fi
# (1 fois pour X et 1 fois pour Y).
# Au pire, tout Ni = 1 et Fi = 1,1,2,2,3,3,4,4,... d'ou S ~ Omega(K^2)
# et donc la complexite est O(K) = O(sqrt(|A|+|B|)) !

def winner(x,y):
    X,Y = T[x],T[y]
    ix,iy = len(X)-1,len(Y)-1
    while ix>=0 and iy>=0:
        # descente rapide de k tours jusqu'a la limite du palier
        k = min(X[ix][1]/Y[iy][0],Y[iy][1]/X[ix][0])
        ix -= k*Y[iy][0]
        iy -= k*X[ix][0]
        # descente d'un tour avec garantie de descente de palier
        # pour l'une des 2 equipes
        iy -= X[ix][0]
        if iy>=0:
            ix -= Y[iy][0]
    return (x if iy<0 else y)

def main():
    global T
    n,k,q = map(int,sys.stdin.readline().split())
    T = [[] for _ in xrange(k)]
    for _ in xrange(n):
        s,t = map(int,sys.stdin.readline().split())
        T[t-1].append(s)
    for t in T:
        if len(t)>0:
            # on trie les combattants par force croissante
            t.sort()
            # t[i] = (force du combattant i, nb de combattants <i de meme force)
            t[0] = (t[0],0)
            for i in xrange(1,len(t)):
                if t[i]==t[i-1][0]:
                    t[i] = (t[i],t[i-1][1]+1)
                else:
                    t[i] = (t[i],0)
    for _ in xrange(q):
        c,x,y = map(int,sys.stdin.readline().split())
        if c==1:
            if len(T[y-1])==0 or T[y-1][-1][0]!=x:
                T[y-1].append((x,0))
            else:
                T[y-1].append((x,T[y-1][-1][1]+1))
        else:
            print winner(x-1,y-1)+1

main()
