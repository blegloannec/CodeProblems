#!/usr/bin/env python

P = 10**9+7

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

def main():
    N = int(raw_input())
    K = int(raw_input())
    H = map(int,raw_input().split())
    S = max(H)
    M = [[int(i+1==j) for j in xrange(S)] for i in xrange(S)]
    for h in H:
        M[-1][S-h] = 1
    M = Matrice(M)
    B = [[0] for _ in xrange(S)]
    B[-1][0] = 1
    B = Matrice(B)
    cnt = (M**N * B)[-1][0]
    print((2*cnt)%P)

main()
