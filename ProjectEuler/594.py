#!/usr/bin/env python3

# voir par exemple (pour une approche basee sur la la dualisation de De Bruijn) :
# Destainville et al., A formula for the number of tilings of an octagon by rhombi, TCS 2004
# https://arxiv.org/abs/math/0302105
# on n'implemente pas la formule ici, on se contente d'enumerer brutalement
# les chemins du dual et de choisir les points d'intersection

# runs in ~14s with pypy

N = 4

def paths(x,y):
    if (x,y)==(0,0):
        yield [(0,0)]
    else:
        if x>0:
            for P in paths(x-1,y):
                P.append((x,y))
                yield P
        if y>0:
            for P in paths(x,y-1):
                P.append((x,y))
                yield P

# chemins (0,0) -> (N,N)
P = list(paths(N,N)) 

# liste des chemins "inferieurs" a chaque chemin
I = [[] for _ in range(len(P))]
for i in range(len(P)):
    for j in range(len(P)):
        if all(P[i][k][1]>=P[j][k][1] for k in range(len(P[i]))):
            I[i].append(j)

# chemin symetrises (0,N) -> (N,0)
S = []
for p in P:
    s = []
    for (x,y) in p:
        s.append((x,N-y))
    S.append(s)

# ensembles de sommets
SP = [set(p) for p in P]
SS = [set(p) for p in S]

# enumeration
# i1,j1 les 2 chemins (0,0) -> (N,N)
# i2,j2 les 2 chemins (0,N) -> (N,0)
# x1,x2,x3,x4 les points d'intersections choisis
cpt = 0
for i1 in range(len(P)):
    for j1 in I[i1]:
        for i2 in range(len(P)):
            for j2 in I[i2]:
                for x1 in SP[i1]&SS[i2]:
                    for x2 in SP[i1]&SS[j2]:
                        if x1[0]<=x2[0] and x1[1]<=x2[1]:
                            for x3 in SP[j1]&SS[i2]:
                                if x1[0]<=x3[0] and x1[1]>=x3[1]:
                                    for x4 in SP[j1]&SS[j2]:
                                        if x3[0]<=x4[0] and x3[1]<=x4[1] and x2[0]<=x4[0] and x2[1]>=x4[1]:
                                            cpt += 1
print(cpt)
