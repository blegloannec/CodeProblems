#!/usr/bin/env python3

# la construction peut se faire en O(n), mais c'est un peu complique
# ici on realise une construction naive en O(n^2)

# insere le suffixe S[i:] dans le sous-arbre de ST enracine en u
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

# .dot output for fun
def ST2dot(S,ST):
    G = ['digraph {']
    for u in ST:
        for (v,i,l) in ST[u]:
            G.append('%d -> %d [label="%s"]' % (u,v,S[i:i+l]))
    G.append('}')
    return '\n'.join(G)

def main():
    S = input()
    ST = {0:[(1,0,len(S))],1:[]}
    for i in range(1,len(S)):
        add(S,ST,i)
    for u in ST:
        for (_,i,l) in ST[u]:
            print(S[i:i+l])

main()
