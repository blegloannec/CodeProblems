#!/usr/bin/env python3

# on complete l'ensemble des colonnes d'une ligne non vide
# ???X???Y???Z??? --> XXXXYYYYZZZZZZZ
# puis on applique la meme completion sur l'ensemble des lignes
# de la grille pour completer les lignes vides en y repliquant
# des lignes completes

def complete(R,C,G):
    L = [] # lignes non vides completees
    for i in range(R):
        j0 = 0 # premiere colonne non vide de la ligne i
        while j0<C and G[i][j0]=='?':
            j0 += 1
        if j0<C: # ligne non vide, on complete
            for j in range(C):
                if G[i][j]!='?':
                    j0 = j
                else:
                    G[i][j] = G[i][j0]
            L.append(i)
    # on complete les lignes vides
    i0 = 0
    for i in range(R):
        if i0==len(L):
            G[i] = G[L[-1]]
        elif i<L[i0]:
            G[i] = G[L[i0]]
        else:
            i0 += 1

def main():
    T = int(input())
    for t in range(1,T+1):
        R,C = map(int,input().split())
        G = []
        for _ in range(R):
            G.append(list(input()))
        complete(R,C,G)
        print('Case #%d:' % t)
        for L in G:
            print(''.join(L))

main()
