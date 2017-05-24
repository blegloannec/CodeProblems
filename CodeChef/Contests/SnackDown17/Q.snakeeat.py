#!/usr/bin/env python3

from bisect import *

# On commence par trier suivant les tailles.
# De facon evidente, si la reponse a une requete est
# de X serpents, alors il existe une solution optimale
# utilisant les X plus grands serpents.
# Chaque requete K peut etre traitee en O(N) de facon gloutonne :
# on parcourt les serpents par tailles decroissantes en maintenant
# un compteur de serpents a manger. Si le serpent courant i est
# plus grand que K (K <= Li), on n'ajoute rien au compteur.
# Si le serpent courant i est plus petit que K (K > Li), on
# ajoute K-Li au compteur. On continue tant que le compteur
# de serpents a manger est inferieur au nb de serpents restant.
# La solution optimale est alors le rang auquel on s'arrete.
# Si l'on pre-calcule les sommes des suffixes du tableau des tailles,
# ainsi que le rang a partir duquel les Li >= K,
# alors chaque rang peut etre teste independemment en O(1).
# On peut donc resoudre chaque requete en O(log N) par recherche
# dichotomique du rang optimal.
# Complexite O(N log N + Q log N)

def main():
    T = int(input())
    for _ in range(T):
        N,Q = map(int,input().split())
        L = list(map(int,input().split()))
        L.sort() # tri (croissant) des tailles
        # pre-calcul des sommes des suffixes
        S = L[:]+[0]
        for i in range(len(L)-2,-1,-1):
            S[i] += S[i+1]
        for _ in range(Q):
            K = int(input())
            # rang b0 a partir duquel les Li >= k
            b0 = bisect_left(L,K)
            # recherche dichotomique du rang optimal
            a,b = 0,b0
            while a<b:
                m = (a+b)//2
                # nombre de serpents a manger pour que
                # tous les serpents de rang >= m atteignent
                # une taille >= K
                s = (b0-m)*K - (S[m]-S[b0])
                if s>m: # plus de serpents a manger que de serpents mangeables
                    a = m+1
                else:
                    b = m
            print(N-a)

main()
