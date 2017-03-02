#!/usr/bin/env python3

# Quick Sort avec le premier element comme pivot.
# Representons le tableau sous la forme d'un arbre binaire :
# la racine est le premier pivot, i.e. le premier element du tableau,
# ses 2 fils sont les arbres definis recursivement de cette facon
# a partir des tableaux less et more de l'algo.
# La complexite du tri est la somme des profondeurs des noeuds.
# Etant donne un arbre binaire, il est aise de re-construire un tableau
# correspondant.
# Il s'agit donc de constuire un arbre binaire a n noeuds dont
# la somme des profondeurs des noeuds est une valeur cible.
# On peut partir de la complexite maximale (l'arbre est une simple
# chaine) et reduire la complexite jusqu'a la profondeur voulu en
# remplissant les profondeurs les plus hautes les unes apres les autres
# (de la gauche vers la droite, ordre militaire).

def build0(depth,d=0,u=0,c0=1):
    L = [c0]
    if d+1<len(depth) and 2*u<depth[d+1]:
        L += build0(depth,d+1,2*u,c0)
        L[0] += len(L)-1
        if 2*u+1<depth[d+1]:
            L += build0(depth,d+1,2*u+1,L[0]+1)
    return L

# version iterative
def build(depth):
    L = []
    Q = [(0,0,1,None)]
    while Q:
        d,u,c0,u0 = Q.pop()
        if u%2==1: # fils droit, m-a-j valeur pere
            L[u0] += len(L)-u0-1
            c0 += len(L)-u0
        if u<depth[d]: # noeud existant
            L.append(c0)
            if d+1<len(depth) and 2*u<depth[d+1]:
                Q.append((d+1,2*u+1,c0,len(L)-1))
                Q.append((d+1,2*u,c0,None))
    return L

def gen(n,c):
    depth = [1 for i in range(n)] # nb de noeuds a chaque profondeur
    m,M = 1,n-1 # min non full depth, max non empty depth
    c0 = n*(n-1)//2
    while c0>c and M>m:
        d = M-min(M-m,c0-c)
        assert(depth[M]==1)
        depth[M] -= 1
        M -= 1
        depth[d] += 1
        if d==m and depth[d]==1<<d:
            m += 1
        c0 -= M-d+1
    return ' '.join(map(str,build(depth))) if c0==c else -1

def main():
    q = int(input())
    for _ in range(q):
        l,c = list(map(int,input().split()))
        print(gen(l,c))

main()
