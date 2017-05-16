#!/usr/bin/env python3

# a(n,i) = nb de permutations de {1..n} avec exactement i "fractures"
# Partant d'une permutation de {1..n-1}, il s'agit de choisir une position
# d'insertion pour le n (qui sera la plus grande valeur courante).
# Si on l'insere au debut ou entre 2 blocs decroissants alors on ne cree pas
# de nouvelle fracture. Toute autre position cree une nouvelle fracture.
# D'où, en ecrivant ce raisonnement "a l'envers" :
# a(n,i) = (i+1)*a(n-1,i) + (n-i)*a(n-1,i-1)
# Eulerian numbers http://oeis.org/A008292
# voir aussi PE 595 pour une methode de denombrement similaire
# et PE 602 pour ces nombres (et d'autres formules)

# Les p(n,m) de l'enonce ne sont pas exactement ces nombres car
# on a une taille N fixee pour l'alphabet, donc il faut choisir
# les n lettres a utiliser :
# p(n,m) = binom(N,n) * a(n,m)

def main():
    N,q = map(int,input().split())
    M = list(map(int,input().split()))
    B = [[int(k==0) for k in range(N+1)] for _ in range(N+1)]
    P = [[int(k==0) for k in range(N+1)] for _ in range(N+1)]
    for n in range(1,N+1):
        for i in range(1,n+1):
            # coefficients binomiaux
            B[n][i] = B[n-1][i-1] + B[n-1][i]
            # nombres euleriens
            P[n][i] = (i+1)*P[n-1][i] + (n-i)*P[n-1][i-1]
    res = sum(max(B[N][n]*P[n][m] for n in range(1,N+1)) for m in M)
    print(res)

main()
