#!/usr/bin/env python3

# chaque serpent a soit un role de protection horizontale,
# soit un role de protection verticale, mais pas les 2 a la fois
# attention, cela ne depend pas de la direction du serpent, mais
# de sa position (un serpent horizontal situe a droite ou a gauche
# du bloc central a un role de protection vertical d'1 case) et
# un serpent completement inclus dans un "bloc de coin" n'a en realite
# aucun role, on peut l'eliminer directement
# on peut donc associer a chaque serpent un intervalle de protection
# vertical ou horizontal suivant sa situation
# il s'agit ensuite de trouver une couverture minimale par intervalles
# du bloc central horizontalement d'une part et verticalement
# d'autre part (de facon completement independante)

# glouton pour une couverture minimale de [L,R]
# par les intervalles de I
def cover(L,R,I):
    I.sort()
    X = L  # premiere position non couverte
    cpt = 0
    i = 0
    while X<=R and i<len(I):
        X1 = -1
        while i<len(I) and I[i][0]<=X:
            # pour les intervalles demarrant avant X
            # on retient la position maximale X1 que
            # l'on peut atteindre
            X1 = max(X1,I[i][1])
            i += 1
        if X1<X:  # X ne peut etre couvert
            return -1
        X = X1+1  # nouvelle position non couverte
        cpt += 1
    return cpt if X>R else -1

def main():
    T = int(input())
    for _ in range(T):
        N,K,M = map(int,input().split())
        L,R = (N-K)//2,(N-K)//2+K-1
        H,V = [],[]
        for _ in range(M):
            X1,Y1,X2,Y2 = map(int,input().split())
            X1,Y1,X2,Y2 = X1-1,Y1-1,X2-1,Y2-1
            # on fabrique l'intervalle associe au serpent
            if X1==X2:
                if L<=X1<=R:
                    V.append((X1,X1))
                else:
                    A,B = min(Y1,Y2),max(Y1,Y2)
                    if not (B<L or A>R):
                        H.append((A,B))
            else:
                if L<=Y1<=R:
                    H.append((Y1,Y1))
                else:
                    A,B = min(X1,X2),max(X1,X2)
                    if not (B<L or A>R):
                        V.append((A,B))
        cpt1 = cover(L,R,H)
        cpt2 = cover(L,R,V)
        if cpt1<0 or cpt2<0:
            print(-1)
        else:
            print(cpt1+cpt2)

main()
