#!/usr/bin/env python3

# Solution assez basique basee sur du hashing facon Rabin-Karp
# (modulo un M assez grand).
# On considere meme hash = meme motif
# Si les hashs different alors supposons que les motifs V et
# W dans P ne different que d'une lettre en position j
# alors hash(W) - hash(V) = (W_j - V_j) * 26^j mod M
# avec -26 < W_j-V_j < 26 et W_j-V_j =/=0
# donc si l'on a pre-calcule les a*26^j mod M
# pour tout -26 < a < 26 et a =/= 0 et tout j < taille de V
# on peut identifier le point de difference potentiel j
# et passer a une verification : ici on verifie juste que les hashs
# et xor sans ces valeurs differentes sont egaux (car le hash seul
# conduit a des faux-positifs sur les 2 derniers testcases).

M = 2140000013
B = 26

# precalcul des B^k % M
Bpow = [1]
for _ in range(10**5+1):
    Bpow.append((Bpow[-1]*B)%M)

# precalcul des differences * B^i mod M
S = {}
for i in range(10**5):
    for a in range(1,B):
        k = (a*Bpow[i])%M
        #assert(k not in S)
        S[k] = i
        k = M-k
        #assert(k not in S)
        S[k] = i
                
def num(c):
    return ord(c)-ord('a')

def main():
    T = int(input())
    for _ in range(T):
        P,V = input().split()
        P = list(map(num,P))
        V = list(map(num,V))
        v = len(V)  # v la taille de V
        VH = 0      # hash de V
        VX = 0      # xor de V
        for i in V:
            VH = (B*VH+i)%M
            VX ^= i
        res = []
        h = 0  # hash de la fenetre de taille v courante
        x = 0  # xor de la fenetre de taille v courante
        for i in range(len(P)):
            h = (B*h + P[i] - (P[i-v] if i>=v else 0)*Bpow[v] ) % M
            x ^= P[i] ^ (P[i-v] if i>=v else 0)
            if i>=v-1:
                if h==VH:  # occurrence exacte de V trouvee
                    res.append(i-v+1)
                else:
                    d = (h-VH)%M  # calcul de la difference
                    if d in S and S[d]<v:  # difference connue
                        j = S[d]  # on en deduit l'emplacement potentiel de la difference
                        # verifications
                        if P[i-j]!=V[v-1-j] and (h-P[i-j]*Bpow[j])%M==(VH-V[v-1-j]*Bpow[j])%M and x^P[i-j]==VX^V[v-1-j]:
                            res.append(i-v+1)
        print(' '.join(map(str,res)) if res else 'No Match!')

main()
