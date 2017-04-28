#!/usr/bin/env python3

from collections import deque,defaultdict

N = int(input())
S = []
for _ in range(N):
    S.append(input())

# NB: si l'on fixe l'ordre dans lequel apparaissent les facteurs
#     on peut aisement fabriquer une solution de facon gloutonne.
# Ici il n'y a que 5 facteurs au maximum (de taille maximale 10), donc
# seulement 5! = 120 permutations a essayer, cette approche serait viable...


# Code pour le probleme pose
# Approche DP/BFS utilisant Knuth-Morris-Pratt
# (BFS sinon on peut boucler)
def prefs(B): # fonction prefixe de KMP
    P = [0]*len(B)
    P[0] = -1
    k = -1
    for i in range(1,len(B)):
        while k>=0 and B[i-1]!=B[k]:
            k = P[k]
        k += 1
        P[i] = k
    return P

P = [prefs(s) for s in S]
def bfs():
    I0 = tuple(0 for _ in range(len(S)))
    Ifinal = tuple(len(s) for s in S)
    dist = {I0:0}
    Q = deque([I0])
    while Q:
        I = Q.popleft()
        if I==Ifinal:
            return dist[I]
        D = []
        for i in range(N):
            # lettres avec lesquelles on peut continuer
            # (ici il n'y en a que 4 donc cette phase est superficielle)
            if I[i]<len(S[i]):
                D.append(S[i][I[i]])
        for a in D:
            J = list(I)
            for i in range(N):
                if J[i]<len(S[i]):
                    while J[i]>=0 and S[i][J[i]]!=a: # KMP fail
                        J[i] = P[i][J[i]]
                    J[i] += 1
            J = tuple(J)
            if J not in dist:
                dist[J] = dist[I]+1
                Q.append(J)

print(bfs())

# Code pour le meme probleme en version sous-suite/mot (non-consecutif)
memo = {tuple(-1 for _ in range(N)):0}
def dp(I):
    if I in memo:
        return memo[I]
    D = defaultdict(list)
    for i in range(N):
        if I[i]>=0:
            D[S[i][I[i]]].append(i)
    res = float('inf')
    for a in D:
        J = list(I)
        for i in D[a]:
            J[i] -= 1
        res = min(res,dp(tuple(J))+1)
    memo[I] = res
    return res

#print(dp(tuple(len(S[i])-1 for i in range(N))))
