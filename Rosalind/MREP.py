#!/usr/bin/env python3

# Au pb LREP, on listait les motif repetes ne pouvant etre etendus
# vers la droite (comme signale dans le commentaire du code de ce pb).
# Ici, on veut de plus que ces facteurs ne puissent etre etendus vers la gauche.
# Pour cela on fait la meme chose sur le miroir de la chaine : on liste alors
# les miroirs des motifs ne pouvant etre etendus vers la gauche.
# On prend alors l'intersection des deux pour avoir les motifs repetes maximaux.

# suffix tree building from SUFF
def add(S,ST,i,u=0):
    iv = 0
    while iv<len(ST[u]) and S[ST[u][iv][1]]!=S[i]:
        iv += 1
    if iv==len(ST[u]):
        # il n'y a pas d'arete a suivre en u
        # on connecte donc une nouvelle feuille pour S[:i] ici
        v = len(ST)
        ST[u].append((v,i,len(S)-i))
        ST[v] = []
    else:
        v,k0,l = ST[u][iv]
        k = k0
        l += k
        j = i
        while j<len(S) and k<l and S[j]==S[k]:
            j += 1
            k += 1
        if k==l:
            # on est alle au bout de l'arete
            add(S,ST,j,v)
        else:
            # on cree un sommet intermediaire et on bifurque
            nv = len(ST)
            ST[nv] = [(v,k,l-k)]
            ST[u][iv] = (nv,k0,k-k0)
            w = len(ST)
            ST[nv].append((w,j,len(S)-j))
            ST[w] = []

def build_ST(S):
    ST = {0:[(1,0,len(S))],1:[]}
    for i in range(1,len(S)):
        add(S,ST,i)
    return ST

# modified repeated pattern detection from LREP
def dfs(S,T,k,u=0,w=''):
    if T[u]:  # internal node
        if len(w)>=k:
            yield w
        for (v,i,j) in T[u]:
            yield from dfs(S,T,k,v,w+S[i:i+j])

def main():
    S0 = input()
    S = S0+'$'
    ST = build_ST(S)
    RP = set(dfs(S,ST,20))
    Srev = S0[::-1]+'$'
    STrev = build_ST(Srev)
    RPrev = set(P[::-1] for P in dfs(Srev,STrev,20))
    MRP = RP & RPrev
    for P in MRP:
        print(P)

main()
