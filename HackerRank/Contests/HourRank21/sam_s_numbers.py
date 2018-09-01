#!/usr/bin/env python3

Mod = 10**9+9
s,m,d = map(int,input().split())

# P[n][a] = nb de combinaisons de n se terminant par a
def dp(s):
    P = [[0]*(m+1) for _ in range(s+1)]
    for i in range(1,m+1):
        P[i][i] = 1
    for n in range(2,s+1):
        for a in range(1,min(m,n)+1):
            for b in range(max(1,a-d),min(a+d,m,n-a)+1):
                P[n][a] = (P[n][a] + P[n-a][b])%Mod
    return P

def main_subtask():
    P = dp(s)
    print(sum(P[s][a] for a in range(1,min(m,s)+1))%Mod)

#main_subtask()

# on a P(n,a) = sum( P(n-a,b), 1<=b<=m et |a-b|<=d )
# en posant le vecteur X(n) = [P(n,1),...,P(n,m)]
# X(n)_a = sum( X(n-a)_b, 1<=b<=m et |a-b|<=d )
# X(n) verifie donc un systeme de dependance lineaire en les
# composantes des X(n-1),...,X(n-m)
# cela conduit a une matrice carree de taille m^2 x m^2

def genM():
    M = [[0]*(m*m) for _ in range(m*m)]
    for i in range((m-1)*m):
        M[i][m+i] = 1
    for a in range(1,m+1):
        for b in range(max(1,a-d),min(a+d,m)+1):
            M[(m-1)*m+a-1][m*(m-a)+b-1] = 1
    return M

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
                    C[i][j] = (C[i][j]+self[i][k]*A[k][j])%Mod
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
    M = Matrice(genM())**(s-m)
    I = [[0] for _ in range(m*m)]
    P = dp(m+1)
    for a in range(1,m+1):
        for b in range(1,m+1):
            I[m*(a-1)+b-1][0] = P[a][b]
    I = Matrice(I)
    J = M*I
    print(sum(J[i][0] for i in range((m-1)*m,m*m))%Mod)

main()
