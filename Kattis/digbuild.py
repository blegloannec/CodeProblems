#!/usr/bin/env python3

# states
# 0  000  ->  0 1 2 3 4
# 1  001  ->  0   2 3
# 2  010  ->  0 1   3 4
# 3  100  ->  0 1 2
# 4  101  ->  0   2

P = 10**9+7
class Matrice:
    def __init__(self,M):
        self.M = M
        self.n = len(M)

    def __getitem__(self,i):
        return self.M[i]

    def __mul__(self,A):
        C = Matrice([[0]*A.n for _ in range(self.n)])
        for i in range(self.n):
            for j in range(A.n):
                for k in range(self.n):
                    C[i][j] = (C[i][j]+self[i][k]*A[k][j])%P
        return C

    def copy(self):
       return Matrice([self[i][:] for i in range(self.n)])

    def __pow__(self,b):
        result = Matrice([[int(i==j) for j in range(self.n)] for i in range(self.n)])
        A = self.copy()
        while b:
            if b & 1:
                result *= A
            A *= A
            b >>= 1
        return result


def main():
    M = Matrice([[1,1,1,1,1],
                 [1,0,1,1,0],
                 [1,1,0,1,1],
                 [1,1,1,0,0],
                 [1,0,1,0,0]])
    N = int(input())
    M = M**(N-1)
    print(sum(sum(L)%P for L in M.M) % P)

main()
