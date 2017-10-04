#!/usr/bin/env python3

# Prog. dyn. sur l'arbre en choisissant un enracinement arbitraire.
# Les valeurs R[u][.] et T[u][.] ne portent que sur l'arbre restreint
# au sous-arbre enracine en u.
# R[u][k] = nb de sous-arbres *contenant u* et ayant exatement k aretes de separation
#           avec leur complementaire *dans le sous-arbre enracine en u*
# T[u][k] = idem pour les sous-arbres *ne contenant pas u*
# O(n * K^2)

def dfs_dp(u,u0=None):
    # R[u] sera construit par une prog. dyn. locale dans la prog. dyn. generale
    # on mettra a jour R[u] en ajoutant un a un les fils v de u et les
    # aretes u--v
    # ainsi, initialement, u n'a encore aucun fils, d'ou pour {u} :
    R[u][0] = 1
    for v in G[u]:
        if v!=u0:
            dfs_dp(v,u)
            R0 = [0]*(K+1)
            # on met a jour les valeurs de T[u] en tenant compte de v
            # on y ajoute donc les T[v][.] et les R[v][.-1],
            # le decalage de 1 servant a compter l'arete u--v
            for k in range(K+1):
                T[u][k] += T[v][k] + (R[v][k-1] if k>0 else 0)
            # on calcule le nouveau R[u] apres "ajout" de v
            R0 = [0]*(K+1)
            for k in range(K+1):
                if k>0:
                    # pour compter les sous-arbres contenant u mais pas v
                    # decalage de 1 a cause de la nouvelle arete u--v
                    R0[k] += R[u][k-1]
                # convolution pour compter les sous-arbres contenant u et v
                for a in range(k+1):
                    R0[k] += R[v][a]*R[u][k-a]
            R[u] = R0

def main():
    global n,K,G,T,R
    n,K = map(int,input().split())
    G = [[] for _ in range(n)]
    for _ in range(n-1):
        u,v = map(int,input().split())
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)
    T = [[0]*(K+1) for _ in range(n)]
    R = [[0]*(K+1) for _ in range(n)]
    dfs_dp(0)
    res = 1 + sum(T[0][k]+R[0][k] for k in range(K+1))
    # +1 car le sous-arbre vide est toujours solution
    print(res)

main()
