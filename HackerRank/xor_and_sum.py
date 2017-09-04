#!/usr/bin/env python3

S = 314159
P = 10**9+7

A = list(map(int,reversed(input())))
B = list(map(int,reversed(input())))
LA,LB = len(A),len(B)
# sommes prefixes de B, i.e. nb de 1 parmi les bits de poids inferieurs
PB = B[:]
for i in range(1,LB):
    PB[i] += PB[i-1]
K = LB+S  # "taille" du resultat
res = 0
p2 = 1  # p2 = 2^k mod P
for k in range(K):
    # k-ieme bit de A
    bA = A[k] if k<LA else 0
    # nb de bits a 1 de B qui passeront par ici
    #nb1B = sum(B[max(0,k-(S)):min(k+1,LB)])
    nb1B = PB[min(k,LB-1)] - (PB[k-S-1] if k-S-1>=0 else 0)
    # nb de bits de B qui passeront par ici et donneront 1 apres xor avec bA
    nbB = nb1B if bA==0 else S+1-nb1B
    res = (res + nbB*p2) % P
    p2 = (2*p2)%P
print(res)
