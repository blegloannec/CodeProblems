#!/usr/bin/env python3

# F(i) = F(i-1) + F(i-2)
# S(i) = S(i-1) + F(i)
#      = S(i-1) + F(i-1) + F(i-2)
#      = S(i-1) + S(i-1)-S(i-2) + S(i-2)-S(i-3)
#      = 2*S(i-1) - S(i-3)

# NB (a posteriori):
#   Actually S(n) = F(n+2)-1 (trivial by induction),
#   which allows a simpler computation of S.

class Matrice:
    def __init__(self, M, mod):
        self.M = M
        self.mod = mod
        self.n = len(self.M[0])
    
    def __getitem__(self, i):
        return self.M[i]
    
    def __mul__(self, A):
        C = Matrice([[0]*self.n for _ in range(self.n)], self.mod)
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    C[i][j] = (C[i][j]+self.M[i][k]*A[k][j])%self.mod
        return C
    
    def copy(self):
       return Matrice([self[i].copy() for i in range(self.n)], self.mod)
    
    def __pow__(self,b):
        result = Matrice([[int(i==j) for j in range(self.n)] for i in range(self.n)], self.mod)
        A = self.copy()
        while b:
            if b & 1:
                result *= A
            A *= A
            b >>= 1
        return result

def S(n, mod):
    if n <  1: return 0
    if n == 1: return 1
    # matrix for S
    M = Matrice([[2,0,-1],[1,0,0],[0,1,0]], mod)**(n-2)
    # init. S(2) = 2, S(1) = 1, S(0) = 0
    return (2*M[0][0]+M[0][1]) % mod

def main():
    N = int(input())
    for _ in range(N):
        a,b,d = map(int, input().split())
        s = (S(b,d) - S(a-1,d)) % d
        div = '' if s==0 else 'NOT '
        print(f'F_{a} + ... + F_{b} is {div}divisible by {d}')

main()
