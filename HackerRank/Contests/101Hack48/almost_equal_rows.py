#!/usr/bin/env python3

# si u et v on presque la meme ligne, alors u et v ont les memes voisins,
# a l'exception eventuelle d'eux-memes s'ils sont directement voisins
# si de plus u et v ont les memes voisins, alors leurs distances min avec
# tous les autres sommets sont les memes (les chemins min passeront
# par le meme voisin) donc c'est une CNS

# Attention, il peut y avoir des aretes en double dans l'input !

def main():
    n,m = map(int,input().split())
    V = [set() for u in range(n)]
    for _ in range(m):
        a,b = map(int,input().split())
        a -= 1
        b -= 1
        V[a].add(b)
        V[b].add(a)
    S = {}
    for u in range(n):
        k = tuple(sorted(V[u]))
        if k in S:
            S[k] += 1
        else:
            S[k] = 1
    res = 0
    # on compte les couples de sommets non voisins
    for k in S:
        res += S[k]*(S[k]-1)//2
    # on ajoute les voisins
    for u in range(n):
        V[u].add(u)
    for u in range(n):
        for v in V[u]:
            if u<v and V[u]==V[v]:
                res += 1
    print(res)

main()
