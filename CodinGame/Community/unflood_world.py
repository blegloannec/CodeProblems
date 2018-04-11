#!/usr/bin/env python3

# Approche optimale et generique en O(n) :
#  - construire le graphe oriente avec une arete d'une case A vers une de
#    ses voisines B ssi la hauteur de A est <= a celle de B (ce graphe
#    contient m = O(n) aretes) ;
#  - calculer le DAG des composantes fortement connexes ;
#  -> la solution est le nb de composantes connexes puits (sans successeur).

# Approche gloutonne ad-hoc plus simple utilisée ici, en O(n log n) :
#  - trier les sommets de la grille par hauteur croissante ;
#  - considerer les sommets dans l'ordre obtenu :
#    si le sommet courant n'est pas encore marque, l'utiliser comme puits et
#    marquer par un DFS tous les sommets non encore marques qui se vident
#    dedans.

# NB : cette seconde approche est "analogue" a la premiere, le tri selon la
#      hauteur constitue un pseudo-tri-topologique acceptable pour l'algo
#      des composantes fortement connexes et la boucle gloutonne est analogue
#      au marquage des composantes fortement connexes suivant un 
#      pseudo-ordre-topologique apres inversion des aretes.

W,H = map(int,input().split())
G = [list(map(int,input().split())) for _ in range(H)]

seen = [[False]*W for _ in range(H)]
def dfs(i,j):
    seen[i][j] = True
    for (vi,vj) in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
        if 0<=vi<H and 0<=vj<W and not seen[vi][vj] and G[i][j]<=G[vi][vj]:
            dfs(vi,vj)

V = sorted(((i,j) for j in range(W) for i in range(H)), key=(lambda X: G[X[0]][X[1]]))
c = 0
for (i,j) in V:
    if not seen[i][j]:
        dfs(i,j)
        c += 1
print(c)
