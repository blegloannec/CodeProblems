#!/usr/bin/env python3

import sys

S = 10
P = lambda x,y: S*x+y

def genM():
    M = [[0]*(S*S) for _ in range(S*S)]
    for x in range(S):
        for y in range(S):
            for (vx,vy) in [(x-1,y),(x,y),(x+1,y),(x,y-1),(x,y+1)]:
                if 0<=vx<S and 0<=vy<S:
                    M[P(vx,vy)][P(x,y)] = 1
    return M

### Some old matrix inversion code
def size(M):
    return len(M),len(M[0])

def affiche(M):
    h,_ = size(M)
    for i in range(h):
        print(''.join(map(str,M[i])))

def ident(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]

def copy(M):
    h,_ = size(M)
    return [M[i][:] for i in range(h)]

def c_swap(M,i,j):
    h,_ = size(M)
    for k in range(h):
        M[k][i],M[k][j] = M[k][j],M[k][i]

def l_swap(M,i,j):
    w = len(M[0])
    for k in range(w):
        M[i][k],M[j][k] = M[j][k],M[i][k]
        
def first_non_zero(M,j):
    h,_ = size(M)
    for i in range(j,h):
        if M[i][j]!=0:
            return i
    return None

def sline_prod(a,M,i):
    w = len(M[0])
    for j in range(w):
        M[i][j] *= a

def line_diff(a,M,i,j):
    # Mj <- Mj - a*Mi
    _,w = size(M)
    for k in range(w):
        M[j][k] -= a*M[i][k]
        M[j][k] %= 2 # Z/2Z

def inverse(M0):
    M = copy(M0)
    n = len(M)
    assert(n==S*S)
    Inv = ident(n)
    for i in range(n):
        j0 = first_non_zero(M,i)
        assert(j0!=None)
        if j0>i:
            l_swap(M,i,j0)
            l_swap(Inv,i,j0)
        #a = Fraction(1,M[i][i]) # for exact Fraction computation
        #sline_prod(a,M,i)
        #sline_prod(a,I,i)
        for j in range(n):
            if j!=i:
                a = M[j][i]
                line_diff(a,M,i,j)
                line_diff(a,Inv,i,j)
    return Inv

def mv_prod(M,x):
    n = len(x)
    y = [0]*n
    for i in range(n):
        for j in range(n):
            y[i] += M[i][j]*x[j]
            y[i] %= 2 # Z/2Z
    return y

def prod(A,B):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k]*B[k][j]
                C[i][j] %= 2 # Z/2Z
    return C
###

def genV(I):
    V = [0]*(S*S)
    for x in range(S):
        for y in range(S):
            if I[x][y]=='O':
                V[P(x,y)] = 1
    return V

def main():
    M = genM()
    Minv = inverse(M)
    name = sys.stdin.readline()[:-1]
    while name!='end':
        I = []
        for _ in range(S):
            I.append(sys.stdin.readline().strip())
        V = genV(I)
        print(name,sum(mv_prod(Minv,V)))
        name = sys.stdin.readline()[:-1]

main()
