#!/usr/bin/env python3

from itertools import permutations

def visible(P):
    m = P[0]
    res = 1
    for i in range(1,len(P)):
        if P[i]>m:
            m = P[i]
            res += 1
    return res

def precomp():
    global Pos
    # Pos[i] contiendra les permutations possibles pour la ligne i
    # i.e. compatibles avec West[i], East[i] et Known[i]
    # Pour reduire ces nombres, on utilisera aussi les donnees verticales :
    # le plus grand building de la colonne j est toujours compris entre les
    # positions Vmin[j] = North[j]-1 et Vmax[j] = N-South[j]
    Vmin = [0]*N
    Vmax = [0]*N
    for j in range(N):
        if North[j]==1:
            Vmin[j] = Vmax[j] = 0
        elif South[j]==1:
            Vmin[j] = Vmax[j] = N-1
        else:
            Vmin[j] = North[j]-1
            Vmax[j] = N-South[j]
    Pos = [[] for _ in range(N)]
    for P in permutations(range(1,N+1)):
        w,e = visible(P),visible(P[::-1])
        for i in range(N):
            if West[i]==w and East[i]==e and all(Known[i][j]==0 or Known[i][j]==P[j] for j in range(N)):
                jmax = P.index(N)
                if Vmin[jmax]<=i<=Vmax[jmax]:
                    Pos[i].append(P)

def unused(U):
    for i in range(1,N+1):
        if U&(1<<i)==0:
            return i
    assert(False)

def backtrack(i=0):
    if i==N:
        # on verifie finalement les contraintes verticales
        return all(visible([Sol[i][j] for i in range(N)])==North[j] for j in range(N)) and all(visible([Sol[i][j] for i in range(N-1,-1,-1)])==South[j] for j in range(N))
    # on traite la ligne O[i]
    if i==N-1:
        # il ne reste qu'une ligne, on la deduit par elimination (au lieu d'essayer
        # les Pos[O[i]], d'autant que c'est le plus grand ensemble de possibilites
        # par construction de l'ordre O)
        Sol[O[i]] = tuple(unused(Used[j]) for j in range(N))
        if visible(Sol[O[i]])==West[O[i]] and visible(Sol[O[i]][::-1])==East[O[i]]:
            return backtrack(i+1)
    for P in Pos[O[i]]:
        # on ne teste ici que la condition de carre latin
        # les contraintes horizontales (et partiellement verticales)
        # sont garanties par le pre-calcul de Pos
        if all(Used[j]&(1<<P[j])==0 for j in range(N)):
            Sol[O[i]] = P
            for j in range(N):
                Used[j] ^= 1<<P[j]
            if backtrack(i+1):
                return True
            for j in range(N):
                Used[j] ^= 1<<P[j]
    return False

def main():
    global N,North,West,East,South,Known
    global Pos,O,Used,Sol
    N = int(input())
    North = list(map(int,input().split()))
    West = list(map(int,input().split()))
    East = list(map(int,input().split()))
    South = list(map(int,input().split()))
    Known = [list(map(int,input().split())) for _ in range(N)]
    precomp()
    # on traitera les lignes dans l'ordre des possibilites croissantes
    O = sorted(range(N), key=(lambda i: len(Pos[i])))
    Used = [0]*N
    Sol = [[0]*N for _ in range(N)]
    assert(backtrack())
    for L in Sol:
        print(*L)

main()
