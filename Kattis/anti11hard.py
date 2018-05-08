#!/usr/bin/env python3

# fonction prefixe de KMP
def prefs(B):
    P = [-1]*(len(B)+1)
    k = -1
    for i in range(1,len(B)+1):
        while k>=0 and B[i-1]!=B[k]:
            k = P[k]
        k += 1
        P[i] = k
    return P

# construit la matrice de l'automate deterministe reconnaissant
# les mots ne contenant pas S
Alpha = ['0','1']
def kmp_automaton(S):
    P = prefs(S)
    M = [[0]*len(S) for _ in range(len(S))]
    for i in range(len(S)):
        for a in Alpha:
            k = i
            while k>=0 and S[k]!=a:
                k = P[k]
            k += 1
            # transition i -a-> k
            if k<len(S):
                # si k n'est pas l'etat associe au mot complet
                # on comptabilise la transition
                M[i][k] += 1
    return M

P = 10**9+7
class Matrice:
    def __init__(self,M):
        self.M = M
        self.m = len(M)
        self.n = len(M[0])

    def __getitem__(self,i):
        return self.M[i]
        
    def __mul__(self,A):
        #assert(self.n==A.m)
        C = Matrice([[0]*A.n for _ in range(self.m)])
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

def count_words(S,n):
    M = Matrice(kmp_automaton(S))**n
    return sum(M[0][i] for i in range(len(S)))%P

def main():
    T = int(input())
    for _ in range(T):
        n,S = input().split()
        n = int(n)
        print(count_words(S,n))

main()
