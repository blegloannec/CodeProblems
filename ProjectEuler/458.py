#!/usr/bin/env python

# il y a 7 lettres dans l'alphabet et on doit eviter tout facteur de
# taille 7 contenant ces 7 lettres, donc tout facteur de taille 7 doit
# contenir une repetition de lettre
# pour tout mot u, notons p(u) la taille du plus grand suffixe de u
# sans repetition de lettre
# u verifie la propriete ssi p(v) < 7 pour tout prefixe v de u
# soit u non vide verifiant la propriete, on a 1 <= p(u) <= 6
# ajoutons une lettre x a la fin de u en maintenant la propriete
# on a p(u) choix pour x intoduisant une repetition et conduisant
# a p(ux) = 1,...,p(u)
# et 7-p(u) choix pour x conduisant a p(ux) = p(u)+1, ce qui est
# interdit si p(u) = 6

# matrice de transition a 6 etats selon la valeur de 1 <= p <= 6
# la colonne i donne les transitions depuis p = i+1
M = [[1,1,1,1,1,1],[6,1,1,1,1,1],[0,5,1,1,1,1],[0,0,4,1,1,1],[0,0,0,3,1,1],[0,0,0,0,2,1]]
# initialement 7 mots de 1 lettre
I = [[7],[0],[0],[0],[0],[0]]

P = 10**9

class Matrice:
    def __init__(self,M):
        self.M = M
        self.m = len(M)
        self.n = len(M[0])

    def __getitem__(self,i):
        return self.M[i]
        
    def __mul__(self,A):
        assert(self.n==A.m)
        C = Matrice([[0 for _ in xrange(A.n)] for _ in xrange(self.m)])
        for i in xrange(self.m):
            for j in xrange(A.n):
                for k in xrange(self.n):
                    C[i][j] = (C[i][j]+self[i][k]*A[k][j])%P
        return C

    def copy(self):
       return Matrice([self[i][:] for i in xrange(self.m)])
    
    def __pow__(self,b):
        assert(self.m==self.n)
        result = Matrice([[int(i==j) for j in xrange(self.n)] for i in xrange(self.n)])
        A = self.copy()
        while b:
            if b & 1:
                result *= A
            A *= A
            b >>= 1
        return result

N = 10**12
M = Matrice(M)
I = Matrice(I)
A = M**(N-1)*I
print sum(A[i][0] for i in xrange(6))%P
