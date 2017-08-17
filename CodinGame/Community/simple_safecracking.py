#!/usr/bin/env python3

# en fait c'est un simple decalage alphabetique (chiffre de Cesar) et
# non une substitution quelconque (ce qu'on a suppose ici), donc on
# pouvait faire un peu plus simple...

D = 'thesafecombinationis'
Dig = {'_e_o':0,'one':1,'t_o':2,'th_ee':3,'fo__':4,'fi_e':5,'si_':6,'se_en':7,'ei_ht':8,'nine':9}

A,B = input().lower().split(':')
A = ''.join(A.split())
B = B.strip().split('-')
K = {chr(i+ord('a')):'_' for i in range(26)}
for i in range(len(D)):
    K[A[i]] = D[i]
print(''.join(str(Dig[''.join(K[c] for c in X)]) for X in B))
