#!/usr/bin/env python3

# approche optimale alternative hashing + dicho search en O(n log n)

# preparation du hashage
NMAX = 10**5+2
B0 = 29
P0 = 10**9+7
Bpow0 = [1]*NMAX
for i in range(1,NMAX):
    Bpow0[i] = (B0*Bpow0[i-1]) % P0

# hash de S[i:j+1] (pour H le tableau des hash prefixes)
def range_hash(H,i,j):
    return (H[j]-((H[i-1]*Bpow0[j-i+1])%P0 if i>0 else 0))%P0

# recherche dichotomique du plus grand prefixe de meme hash de S et S[i0:]
def dicho(H,i0):
    l,r = 1,len(H)-i0
    while l<r:
        m = (l+r+1)//2
        if range_hash(H,i0,i0+m-1)==H[m-1]:
            l = m
        else:
            r = m-1
    return l

def suff_similarity(S):
    S = [ord(c)-ord('a') for c in S]
    # calcul des hash des prefixes
    Hash = [0]*len(S)
    Hash[0] = S[0]
    for i in range(1,len(S)):
        Hash[i] = (B0*Hash[i-1] + S[i]) % P0
    # resultat
    SuffSim = [dicho(Hash,i) if S[i]==S[0] else 0 for i in range(len(S))]
    return SuffSim

def main():
    T = int(input())
    for _ in range(T):
        S = input().strip()
        print(sum(suff_similarity(S)))

main()
