#!/usr/bin/env python3

# On peut aisement construire un automate, mais il faudrait naivement
# 3^10, ou plutot 3^5*2^5 etats afin de distinguer la presence ou non
# des chiffres impairs.
# En fixant les chiffres impairs utilises, on peut se ramener a la
# construction de 6 automates avec 2^i*2^5 etats ou 0<=i<=5 est le
# nb de chiffres impairs utilises, mais 2^10 etats reste un peu grand.
# Au lieu de ca, on va reduire le nb d'etats en "factorisant" de la
# facon suivante.
# Fixons le nb O de chiffres impairs utilises et considerons comme
# etats les couples (a,b) ou 0<=a<=O est le nb de chiffres impairs
# actuellement en nb pair et 0<=b<=5 le nb de chiffres pairs actuellement en
# nb impair.
# Partant d'un etat (a,b), on a :
#  - a transitions vers (a-1,b)
#  - O-a transitions vers (a+1,b)
#  - b transitions vers (a,b-1)
#  - 5-b transitions vers (a,b+1)
# Il faut un etat initial special pour manger les 0 initiaux (afin de compter
# plus tard les mots correspondant a des nb de taille <=n).
# On se ramene donc a la construction de 6 automates dont le plus grand est de
# taille seulement 6^2 = 36.

def genM(O):
    N = 6*(O+1)+1
    M = [[0]*N for _ in range(N)]
    for a in range(O+1):
        for b in range(6):
            if a>0:
                M[6*a+b][6*(a-1)+b] = a
            if a<O:
                M[6*a+b][6*(a+1)+b] = O-a
            if b>0:
                M[6*a+b][6*a+b-1] = b
            if b<5:
                M[6*a+b][6*a+b+1] = 5-b
    # N-1 etat initial pour manger les 0 initiaux
    M[N-1][N-1] = 1      # N-1 -0-> N-1
    M[N-1][O*6+1] = 4    # lecture d'une lettre paire =/= 0
    if O>0:
        M[N-1][(O-1)*6] = O  # lecture d'une lettre impaire
    return M

def binom(n,p):
    return 1 if p==0 else n*binom(n-1,p-1)//p

P = 10**9+123

class Matrice:
    def __init__(self,M):
        self.M = M
        self.m = len(M)
        self.n = len(M[0])

    def __getitem__(self,i):
        return self.M[i]
        
    def __mul__(self,A):
        assert(self.n==A.m)
        C = Matrice([[0 for _ in range(A.n)] for _ in range(self.m)])
        for i in range(self.m):
            for j in range(A.n):
                for k in range(self.n):
                    C[i][j] = (C[i][j]+self[i][k]*A[k][j])%P
        return C

    def copy(self):
       return Matrice([self[i][:] for i in range(self.m)])
    
    def __pow__(self,b):
        assert(self.m==self.n)
        result = Matrice([[int(i==j) for j in range(self.n)] for i in range(self.n)])
        A = self.copy()
        while b:
            if b & 1:
                result *= A
            A *= A
            b >>= 1
        return result

def Q(N):
    cpt = 0
    for O in range(6):
        M = Matrice(genM(O))**N
        # on choisit 0 chiffres impairs parmi 5
        cpt = (cpt + binom(5,O)*(M[6*(O+1)][0]))%P
    return cpt

def main():
    N = 100
    res = 0
    for u in range(1,40):
        res = (res + Q(1<<u))%P
    print(res)

main()
