#!/usr/bin/env python3

# Rappel (cf INOD): Rajouter une feuille a un arbre binaire non-enracine,
# c'est choisir une arete, ajouter un nouveau noeud interne au milieu
# et y connecter la nouvelle feuille.

def dfs_gen(T,u,new_leaf,new_trees):
    for iv in range(len(T[u])):
        v = T[u][iv]
        nv = len(T)     # nouveau noeud interne
        T0 = T.copy()   # shallow copy! so...
        T0[u] = T[u][:] # ...copy needed here
        T0[u][iv] = nv
        T0[nv] = [v,new_leaf]
        T0[new_leaf] = []
        new_trees.append(T0)
        dfs_gen(T,v,new_leaf,new_trees)

def newick_str(T,u=0):
    if isinstance(u,int): # internal node
        return '('+','.join(newick_str(T,v) for v in T[u])+')'
    else:
        return u
        
def main():
    S = list(input().split())
    assert(len(S)>=3)
    Tinit = {S[i]:[] for i in range(3)}
    Tinit[0] = S[:3]
    L = [Tinit]
    for i in range(3,len(S)):
        newL = []
        for T in L:
            dfs_gen(T,0,S[i],newL)
        L = newL
    for T in L:
        print(newick_str(T)+';')

main()
