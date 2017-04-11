#!/usr/bin/env python3

from collections import defaultdict

# analogie avec les echecs assez evidente
# x = tour, + = fou, o = reine <=> x et + simultanement

# cf l'analyse "officielle" du pb :
# l'astuce est de remarquer qu'avec les regles (qui "traversent" les pieces),
# les placements des x et des + sont completement independants !

# il s'agit donc de completer une configuration de tours jusqu'a
# arriver a une configuration maximale de n tours (facile, il suffit
# d'ajouter 1 tour par ligne et colonne non encore couverte, un placement
# de tours maximal est une matrice de permutation)

# et de completer une configuration de fous jusqu'a arriver a une
# configuration maximale (qui aura au plus 2n-2 fous, mais possiblement
# moins, cela depend de la configuration initiale)
# evidement les fous sur cases noires/blanches ne peuvent interferer,
# donc on peut les considerer comme 2 sous-pb independants

# on peut resoudre ca par couplage maximal biparti : les diagonales d'un
# cote et les anti-diagonales de l'autre, une arete entre une diag et une
# anti-diag si elles s'intersectent (chaque case est alors identifie de
# facon unique par une arete)

# mais on peut mieux faire
# si on "redresse" les diagonales d'une meme couleur sur un echiquier 8x8
# on a un "diamant" de la forme suivante sur lequel on doit resoudre un
# placement maximal de tours (au plus un fou par ligne et colonne)
# (diamant = sequence de lignes croissante puis decroissante, au sens de
#  l'inclusion des colonnes)
#    ..
#   ....
#  ......
# ........
#  ......
#   ....
#    ..
# ici on a 7 lignes et 8 colonnes, peut donc placer au plus 7 fous et l'on
# est sur de pouvoir placer un fou par ligne de facon gloutonne en choisissant
# une position quelconque sur une *plus petite* ligne, en retirant cette ligne
# et la colonne et en recommencant sur le nouveau diamant dont toutes les
# autres lignes on une taille reduite de 1 (c'est forcement un "diamant" car
# puisqu'on choisit une plus petite ligne, la colonne choisie traverse toutes
# les autres lignes)
# dans le cas ou il y a 2 plus petites lignes de taille 1, on ne peut
# placer de fou que sur une des deux, donc dans ce cas le nb de fous
# placable est le nb de lignes - 1

def greedy_bishops(N,Bishops):
    D = defaultdict(set)
    for r in range(N):
        for c in range(N):
            D[r+c].add((r,c))
    for (x,y) in Bishops:
        d,a = x+y,x-y
        del D[d]
        for i in list(D):
            if i%2==d%2:
                x0,y0 = (i+a)//2,(i-a)//2
                if 0<=x0<N and 0<=y0<N:
                    D[i].remove((x0,y0))
                    if len(D[i])==0:
                        del D[i]
    I = sorted(D.keys(),key=(lambda x: len(D[x])))
    for d in I:
        if d in D:
            x,y = D[d].pop()
            Bishops.add((x,y))
            a = x-y
            del D[d]
            for i in list(D):
                if i%2==d%2:
                    x0,y0 = (i+a)//2,(i-a)//2
                    if 0<=x0<N and 0<=y0<N:
                        D[i].remove((x0,y0))
                        if len(D[i])==0:
                            del D[i]

def main():
    T = int(input())
    for t in range(1,T+1):
        N,M = map(int,input().split())
        Init,Rooks,Bishops = {},set(),set()
        RookR,RookC = set(range(N)),set(range(N))
        for _ in range(M):
            Style,R,C = input().split()
            R,C = int(R)-1,int(C)-1
            Init[R,C] = Style
            if Style in ['x','o']:
                Rooks.add((R,C))
                RookR.remove(R)
                RookC.remove(C)
            if Style in ['+','o']:
                Bishops.add((R,C))
        # naive greedy Rooks
        while len(RookR)>0:
            Rooks.add((RookR.pop(),RookC.pop()))
        # Bishops
        greedy_bishops(N,Bishops)
        # Output
        P = []
        Queens = Rooks & Bishops
        for (x,y) in Queens:
            if (x,y) not in Init or Init[x,y]!='o':
                P.append((x,y,'o'))
        for (x,y) in Rooks - Queens:
            if (x,y) not in Init:
                P.append((x,y,'x'))
        for (x,y) in Bishops - Queens:
            if (x,y) not in Init:
                P.append((x,y,'+'))
        print('Case #%d: %d %d' % (t,len(Rooks)+len(Bishops),len(P)))
        for (x,y,s) in P:
            print('%s %d %d' % (s,x+1,y+1))

main()
