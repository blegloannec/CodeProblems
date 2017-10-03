#!/usr/bin/env python3

P = 10**9+7

def inv_mod(a):
    return pow(a,P-2,P)
    
F,Finv = [1],[1]
for n in range(1,301):
    F.append((F[-1]*n)%P)
    Finv.append(inv_mod(F[-1]))

def binom(n,p):
    assert(0<=p<=n)
    return (F[n]*Finv[p]*Finv[n-p])%P

def main():
    T = int(input())
    for _ in range(T):
        N,M = map(int,input().split())
        X = [int(x)-1 for x in input().split()]
        D = list(map(int,input().split()))
        S = [0]*(M+1)
        S[0] = 1
        for d in range(N):
            # on ajoute la dimension d
            # C[m][x] = nb de manieres d'arriver en x apres m pas dans la d-ieme dimension
            # O(M * D[d])
            C = [[0]*D[d] for _ in range(M+1)]
            C[0][X[d]] = 1
            for m in range(1,M+1):
                for x in range(D[d]):
                    C[m][x] = ((C[m-1][x-1] if x>0 else 0) + (C[m-1][x+1] if x+1<D[d] else 0)) % P
            # on somme sur les differentes positions finales pour chaque m
            SC = [0]*(M+1)
            for m in range(M+1):
                for x in range(D[d]):
                    SC[m] = (SC[m] + C[m][x]) % P
            # on integre ca au resultat global, O(M^2)
            # a la fin S[m] sera le nb de chemins de taille m dans les dimensions <= d
            # de la grille
            S0 = [0]*(M+1)
            for m in range(M+1):
                # convolution
                for a in range(m+1):
                    # faire a pas parmi m dans la dimension d
                    S0[m]  = (S0[m] + binom(m,a)*SC[a]*S[m-a]) % P
            S = S0
        print(S[M])

main()
