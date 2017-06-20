#!/usr/bin/env python3

# Posons f(n) la somme demandee et nb(n) le nb de tels nombres
# nb(n) est le nb de compositions (partitions ordonnees) de l'entier n
# dont les composantes sont de valeurs 1 a 9
# nb(n) = sum( nb(n-k), 1<=k<=9 )
# f(n) = sum( 10*f(n-k) + k*nb(n-k), 1<=k<=9 )
# systeme de relations de recurrence lineaires de taille 18

# prog. dyn. pour l'initialisation
def dp(n):
    F = [0]*(n+1)
    NB = [1]*(n+1)
    for a in range(1,n+1):
        NB[a] = sum(NB[a-k] for k in range(1,min(9,a)+1))
        F[a] = sum(10*F[a-k]+k*NB[a-k] for k in range(1,min(9,a)+1))
    return F,NB

def genM():
    M = [[0]*18 for _ in range(18)]
    for i in range(16):
        M[i][i+2] = 1
    for k in range(9):
        M[16][2*k] = 1
        M[17][2*k+1] = 10
        M[17][2*k] = 9-k
    return M

P = 10**9
class Matrice:
    def __init__(self,M):
        self.M = M
        self.m = len(M)
        self.n = len(M[0])

    def __getitem__(self,i):
        return self.M[i]
        
    def __mul__(self,A):
        #assert(self.n==A.m)
        C = Matrice([[0 for _ in range(A.n)] for _ in range(self.m)])
        for i in range(self.m):
            for j in range(A.n):
                for k in range(self.n):
                    C[i][j] = (C[i][j]+self[i][k]*A[k][j])%P
        return C

    def copy(self):
       return Matrice([self[i][:] for i in range(self.m)])
    
    def __pow__(self,b):
        #assert(self.m==self.n)
        result = Matrice([[int(i==j) for j in range(self.n)] for i in range(self.n)])
        A = self.copy()
        while b:
            if b & 1:
                result *= A
            A *= A
            b >>= 1
        return result

def main():
    M = Matrice(genM())
    F,NB = dp(8)
    I = [[0] for _ in range(18)]
    for i in range(9):
        I[2*i][0] = NB[i]
        I[2*i+1][0] = F[i]
    I = Matrice(I)
    res = 0
    for i in range(1,18):
        A = M**(13**i-8) * I
        res = (res + A[-1][0])%P
    print(res)

main()
