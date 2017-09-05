#!/usr/bin/env python3

def binom(n,p):
    return 1 if p==0 else n*binom(n-1,p-1)//p

N,m,g,k = map(int,input().split())
# P[i] = proba que la generation courante contienne
#        exactement 0<=i<=2N alleles dominants
P = [0]*(2*N+1)
P[m] = 1
for _ in range(g):
    P1 = [0]*(2*N+1)  # probas de la nouvelle generation
    for m0 in range(2*N+1):
        p = m0/(2*N)  # proba de selection d'un allele dominant
        for m1 in range(2*N+1):
            # on ajoute la proba que la generation courante ait m0 alleles
            # dominants et en produise m1 a la generation suivante
            P1[m1] += P[m0] * binom(2*N,m1) * p**m1 * (1-p)**(2*N-m1)
    P = P1
pk = sum(P[i] for i in range(2*N-k+1))
print(pk)
