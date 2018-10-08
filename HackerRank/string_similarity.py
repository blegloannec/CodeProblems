#!/usr/bin/env python3

# l'approche optimale est en O(n log n) via Suffix Array + LCP
# (cf https://www.hackerrank.com/challenges/string-similarity/topics )
# on utilise ici une approche sqrt-decomposition + hashing en O(n sqrt(n))
# (voir aussi string_similarity_bis.py pour une approche hashing + dicho search)

# preparation du hashage
NMAX = int(10**(5/2))+2
B0 = 29
P0 = 10**9+7
Bpow0 = [1]*NMAX
for i in range(1,NMAX):
    Bpow0[i] = (B0*Bpow0[i-1]) % P0

def suff_similarity(S):
    S = [ord(c)-ord('a') for c in S]
    N = max(1,int(len(S)**0.5))  # taille des blocs
    HS = len(S)//N               # nb de blocs
    # calcul des hash des blocs de S
    Hash = [0]*HS
    for i in range(HS):
        for j in range(N):
            Hash[i] = (B0*Hash[i] + S[i*N+j]) % P0
    Hash0 = Hash[:]
    # traitement des suffixes
    SuffSim = [0]*len(S)
    SuffSim[0] = len(S)
    for k in range(1,len(S)):
        # suffixe S[k:], on met a jour les hash roulants des blocs, O(sqrt(n))
        L = len(S)-k
        for i in range(L//N):
            Hash[i] = (B0*Hash[i] - Bpow0[N]*S[k-1+i*N] + S[k+(i+1)*N-1]) % P0
        # calcul du prefixe commun
        j = 0
        # comparaisons des hash des blocs, O(sqrt(n))
        while j<L//N and Hash[j]==Hash0[j]:
            j += 1
        j *= N
        # on termine caractere par caractere, O(sqrt(n))
        while j<L and S[k+j]==S[j]:
            j += 1
        SuffSim[k] = j
    return SuffSim

def main():
    T = int(input())
    for _ in range(T):
        S = input().strip()
        print(sum(suff_similarity(S)))

main()
