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

# N(m,n) = nb pavages avec blocs de couleur de taille m (fixee)
# N(m,n) = N(m,n-1) + N(m,n-m)
# (dernier bloc 1 + dernier bloc m)
# et N(m,n) = 1 pour 0<=n<m
# pour m=2, c'est fibonacci

def expo(A,n):
    if n==1:
        return A
    elif n%2==0:
        return expo(A*A,n/2)
    else:
        return A*expo(A*A,(n-1)/2)

R = Matrice([[0,1],[1,1]])
G = Matrice([[0,1,0],[0,0,1],[1,0,1]])
B = Matrice([[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,1]])
def F(n):
    # full black are forbidden
    return (expo(R,n).M[1][1] + expo(G,n).M[2][2] + expo(B,n).M[3][3] - 3)%P

def main():
    T = int(sys.stdin.readline())
    for t in xrange(T):
        n = int(sys.stdin.readline())
        print F(n)

main()
