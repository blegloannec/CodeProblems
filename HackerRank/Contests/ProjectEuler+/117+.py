#!/usr/bin/env python

import sys

P = 1000000007

class Matrice:
    def __init__(self,M):
        self.M = M
        self.m = len(M)
        self.n = len(M[0])
    def __mul__(self,A):
        assert(self.n==A.m)
        C = Matrice([[0 for _ in xrange(A.n)] for _ in xrange(self.m)])
        for i in xrange(self.m):
            for j in xrange(A.n):
                for k in xrange(self.n):
                    C.M[i][j] = (C.M[i][j]+self.M[i][k]*A.M[k][j])%P
        return C

# N(n) = nb pavages avec blocs de taille 1 à 4
# N(n) = N(n-1) + N(n-2) + N(n-3) + N(n-4)

def expo(A,n):
    if n==1:
        return A
    elif n%2==0:
        return expo(A*A,n/2)
    else:
        return A*expo(A*A,(n-1)/2)

M = Matrice([[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,1,1,1]])
def main():
    T = int(sys.stdin.readline())
    for t in xrange(T):
        n = int(sys.stdin.readline())
        print expo(M,n).M[3][3]

main()
