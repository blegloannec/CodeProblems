#!/usr/bin/env python3

# Quelle que soit la combinaison de deplacements,
# les positions sont permutees par ensembles de 4 :
# pour tous 0 <= i,j < n, les elements en positions
# (i,j), (2n-1-i,j), (i,2n-1-j) et (2n-1-i,2n-1-j)
# restent permutes entre-eux.
# Pour chaque (i,j), on peut choisir le max de ces 4 positions
# et l'amener dans le quadrant superieur gauche sans modifier le
# reste de ce quadrant de la maniere suivante :
#  - amener ce max X dans le quadrant superieur droit par des operations
#    ne touchant pas au quadrant superieur gauche ;
#    X est alors en position (i,2n-1-j) ;
#  - descendre (inverser) toutes les colonnes du quadrant superieur gauche
#    sauf la colonne j ;
#  - inverser la ligne i ;
#  - remonter (inverser de nouveau) toutes les colonnes du quadrant superieur
#    gauche sauf la colonne j.

def main():
    q = int(input())
    for _ in range(q):
        n = int(input())
        M = [list(map(int,input().split())) for _ in range(2*n)]
        S = sum(max(M[i][j],M[2*n-1-i][j],M[i][2*n-1-j],M[2*n-1-i][2*n-1-j]) for i in range(n) for j in range(n))
        print(S)

main()
