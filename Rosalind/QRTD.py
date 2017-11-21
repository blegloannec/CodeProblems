#!/usr/bin/env pypy

import rosalib

# O(N^2) DP approach
# runs in ~11s with pypy

# L'approche utilisee est assez simple et naturelle mais pourrait sembler naivement en O(N^3),
# la complexite en O(N^2) repose sur une prog. dyn. pour le calcul efficace des intersections.
# On ne detaille pas ici, on renvoie a l'explication claire et concise de (section 3.1) :
# Sand et al., Algorithms for Computing the Triplet and Quartet Distances for Binary and General Trees
# in Biology, 2013, http://www.cs.au.dk/~gerth/papers/biology13.pdf


## Input
S = raw_input().split()
N = len(S)
Sall = set(S)
A = {}
rosalib.parse_newick(raw_input(),A,True)
B = {}
rosalib.parse_newick(raw_input(),B,True)


## Fonctions de construction
def children(T,u,u0):
    return (v for v in T[u] if v!=u0)

# Pour chaque arete orientee e = (u0,u) de l'arbre T,
# S(e) = ensemble des feuilles du sous-arbre enracine en u
#        pointe par la direction de e
# Calcul des S(e) (et numerotation des aretes au passage)
def dfs(T,u,u0,E,Enum,S):
    if u[0]!='@':  # leaf
        l = {u}
    else:
        v1,v2 = children(T,u,u0)
        l = dfs(T,v1,u,E,Enum,S)|dfs(T,v2,u,E,Enum,S)
    Enum[u0,u] = len(E)
    E.append((u0,u))
    S.append(l)
    Enum[u,u0] = len(E)
    E.append((u,u0))
    S.append(Sall-l)
    return l

# Construction du graphe des aretes orientees (pour reference rapide
# par la suite)
def edges_graph(T,E,Enum):
    EG = []
    for e in xrange(len(E)):
        u0,u = E[e]
        if u[0]=='@':  # leaf
            u1,u2 = children(T,u,u0)
            EG.append((Enum[u,u1],Enum[u,u2]))
        else:
            EG.append(None)
    return EG


## Constructions effectives
u0 = S[0]
EA,EAnum,SA = [],{},[]
dfs(A,A[u0][0],u0,EA,EAnum,SA)
EGA = edges_graph(A,EA,EAnum)
EB,EBnum,SB = [],{},[]
dfs(B,B[u0][0],u0,EB,EBnum,SB)
EGB = edges_graph(B,EB,EBnum)


## DP pour le calcul de toutes les intersections des SA et SB en O(N^2)
I = [[-1 for _ in xrange(len(EB))] for _ in xrange(len(EA))]  # intersections
def dp_inter(ea,eb):
    if I[ea][eb]>=0:
        return I[ea][eb]
    a0,a = EA[ea]
    b0,b = EB[eb]
    if not EGA[ea]:    # a leaf
        res = int(a in SB[eb])
    elif not EGB[eb]:  # b leaf
        res = int(b in SA[ea])
    else:
        ea1,ea2 = EGA[ea]
        eb1,eb2 = EGB[eb]
        # formule recursive du calcul de l'intersection
        res = dp_inter(ea1,eb1) + dp_inter(ea1,eb2) + dp_inter(ea2,eb1) + dp_inter(ea2,eb2)
    I[ea][eb] = res
    return res


## Calcul de la distance en O(N^2)
def binom(n,p):
    return 1 if p==0 else n*binom(n-1,p-1)/p

q = 0  # quartets en commun (comptes en double)
for ea in xrange(len(EA)):
    if EGA[ea]:
        a0,a = EA[ea]
        ea1,ea2 = EGA[ea]
        ea_inv = EAnum[a,a0]
        for eb in xrange(len(EB)):
            if EGB[eb]:
                b0,b = EB[eb]
                eb1,eb2 = EGB[eb]
                eb_inv = EBnum[b,b0]
                # nb de quartets communs induits par ea et eb
                q += binom(dp_inter(ea_inv,eb_inv),2) * (dp_inter(ea1,eb1)*dp_inter(ea2,eb2) + dp_inter(ea1,eb2)*dp_inter(ea2,eb1))
# NB : ici les deux arbres contiennent les N feuilles
dist = 2*binom(N,4) - q
print(dist)
