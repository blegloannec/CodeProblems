#!/usr/bin/env python3

# Plusieurs observations sur le graphe d'une sequence :
#  - Une arete i -> j verifie toujours i < j, en particulier
#    il n'y a pas d'arete entrante en 0 ou sortante de N.
#  - Toutes les aretes entrantes au sommet i ont pour
#    etiquette la lettre A_i, en particulier il n'y a pas de multi-aretes
#    (que le label soit different ou non) dans un graphe valide.
#  - Pour tout i<N, on a une arete i -> j ssi l'indice j est la premiere
#    occurrence de A_j parmi les indices > i.
#  - Pour tout j>0, l'ensemble des i tels qu'il existe une arete
#    i -> j est le plus grand intervalle non vide [imin(j),j-1]
#    pour lequel les lettres A_i =/= A_j.
#    Si imin(j) = 0, alors A_j est une nouvelle lettre de la sequence.
#    Sinon, A_j = A_{imin(j)-1}.

def gen(N,E):
    G = [N+1 for _ in range(N+1)]
    S = [set() for _ in range(N+1)]
    for x,y in E:
        if x>=y or x in S[y]:
            return -1
        G[y] = min(G[y],x)
        S[y].add(x)
    C = []
    cpt = 1
    for i in range(1,N+1):
        if len(S[i])==0 or i-G[i]!=len(S[i]):
            return -1
        if G[i]==0:
            C.append(cpt)
            cpt += 1
        else:
            C.append(C[G[i]-1])
    # verif
    E = set(E)
    D = {}
    m = 0
    for i in range(N-1,-1,-1):
        D[C[i]] = i+1
        for x in D:
            if not (i,D[x]) in E:
                return -1
            m += 1
            if m>len(E):
                return -1
    if m!=len(E):
        return -1
    return ' '.join(map(str,C))

def main():
    T = int(input())
    for _ in range(T):
        N,M = map(int,input().split())
        E = [tuple(map(int,input().split())) for _ in range(M)]
        print(gen(N,E))

main()
