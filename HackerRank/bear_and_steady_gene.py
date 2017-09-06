#!/usr/bin/env python3

# Un facteur est acceptable pour equilibrer la chaine ssi le nb d'occurrences
# de chaque lettre a l'exterieur de ce facteur est <= n/4.
# Pour chaque position de depart l, on recherche la plus petite position de fin
# verifiant cette condition pour chacune des quatre lettres en avancant un
# pointeur de fin r.
# O(A*n) pour A = 4 la taille de l'alphabet

Num = {'A':0,'C':1,'G':2,'T':3}

n = int(input())
n4 = n//4
DNA = input()
Cpt = [0]*4  # compteur total pour chaque lettre
for a in DNA:
    Cpt[Num[a]] += 1
LCpt,RCpt = [0]*4,[0]*4  # compteurs courants en positions l et r
r,m = 0,float('inf')
for l in range(n):
    if l>0:
        LCpt[Num[DNA[l-1]]] += 1
    # on avance le pointeur r tant que l'exterieur de DNA[l:r]
    # contient > n/4 occurrences de l'une des quatre lettres
    while r<l or (r<n and any(Cpt[a]-(RCpt[a]-LCpt[a])>n4 for a in range(4))):
        RCpt[Num[DNA[r]]] += 1
        r += 1
    if all(Cpt[a]-(RCpt[a]-LCpt[a])<=n4 for a in range(4)) and r-l<m:
        m = r-l
print(m)
