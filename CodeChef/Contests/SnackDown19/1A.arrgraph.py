#!/usr/bin/env python3

# Tout nb premier est connecte a tout le monde sauf ses multiples,
# or les nb sont limites a [2,50] donc tout nb premier >25 (au choix 29,
# 31, 37, 41, 43 ou 47) est connecte a tout le monde sauf lui-meme.
# Si le graphe n'est pas deja connexe :
#  - soit il ne contient pas 29 (ou autre), auquel cas il suffit de remplacer
#    n'importe quel nb par 29 ;
#  - soit il contient 29, auquel cas il n'est en fait constitue que de 29 (car
#    la seule presence d'une autre valeur assurerait la connexite), et on
#    on remplace une valeur par n'importe quoi =/= 29.

import fractions, functools

@functools.lru_cache()
def gcd(a,b):
    return fractions.gcd(a,b)

def connected(A):
    seen = [False]*len(A)
    S = [0]
    seen[0] = True
    while S:
        u = S.pop()
        for v in range(len(A)):
            if not seen[v] and gcd(A[u],A[v])==1:
                seen[v] = True
                S.append(v)
    return all(seen)

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int,input().split()))
        res = 0
        if not connected(A):
            res = 1
            A[0] = 2 if A[0]==29 else 29
        print(res)
        print(*A)

main()
