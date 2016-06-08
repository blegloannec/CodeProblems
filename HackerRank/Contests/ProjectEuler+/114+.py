#!/usr/bin/env python

import sys

# on fixe m = 3 pour le calcul (generalisation facile ensuite)
# pour n>3, f(n) = f(n-1) + f(n-4) + ... + f(0)
# avec la convention f(0) = 2
# posons S(n) = sum( f(k), k=0..n )
# f(n) = S(n-1) - S(n-2) + S(n-4)
# S(n) = f(n) + S(n-1) = 2*S(n-1) - S(n-2) + S(n-4)
# relation lineaire acceptable
# et f(n) = S(n) - S(n-1)
# Valeurs initiales (0..3)
# f 2 1 1 2
# S 2 3 4 6

# tout cela se generalise (trivial) a m qcq en :
# S(n) = 2*S(n-1) - S(n-2) + S(n-m-1)

P = 1000000007

# matrix multiplication has to be fast for testcase 14
# but numpy not allowed
def matmult(A,B):
    pB = zip(*B)
    return [[sum(ea*eb for ea,eb in zip(a,b))%P for b in pB] for a in A]

def expo(A,b):
    result = [[int(i==j) for j in xrange(len(A))] for i in xrange(len(A))]
    while b:
        if b & 1:
            result = matmult(result,A)
        A = matmult(A,A)
        b >>= 1
    return result

def main():
    n,m = map(int,sys.stdin.readline().split())
    if n<=m:
        print 2 if n==m else 1
        return
    # Cas m = 3
    #A = Matrice([[2,-1,0,1],[1,0,0,0],[0,1,0,0],[0,0,1,0]])
    #I = Matrice([[6],[4],[3],[2]])
    M = [[0 for _ in xrange(m+1)] for _ in xrange(m+1)]
    M[0][0] = 2
    M[0][1] = -1
    M[0][m] += 1 # += to deal with m=1 (testcase 8)
    for i in xrange(1,m+1):
        M[i][i-1] = 1
    Init = [[m-i+2] for i in xrange(m+1)]
    Init[0][0] += 1
    B = expo(M,n-m)
    BI = matmult(B,Init)
    print (BI[0][0] - BI[1][0])%P

main()
