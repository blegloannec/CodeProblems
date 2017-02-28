#!/usr/bin/env python3

def genM(h,w):
    n = h*w
    M = [[0]*n for _ in range(n)]
    for x in range(h):
        for y in range(w):
            for (vx,vy) in [(x-1,y),(x,y),(x+1,y),(x,y-1),(x,y+1)]:
                if 0<=vx<h and 0<=vy<w:
                    M[vx*w+vy][x*w+y] = 1
    return M

def line_swap(M,i,j):
    for k in range(len(M)):
        M[i][k],M[j][k] = M[j][k],M[i][k]
        
def pivot(M,j):
    for i in range(j,len(M)):
        if M[i][j]!=0:
            return i
    return None

def line_diff(a,M,i,j):
    for k in range(len(M)):
        M[j][k] -= a*M[i][k]
        M[j][k] %= 2

def inverse(M0):
    M = [L[:] for L in M0]
    n = len(M)
    Inv = [[int(i==j) for j in range(n)] for i in range(n)]
    for i in range(n):
        j0 = pivot(M,i)
        assert(j0!=None)
        if j0>i:
            line_swap(M,i,j0)
            line_swap(Inv,i,j0)
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
            y[i] %= 2
    return y

def main():
    n = int(input())
    M = genM(n,n)
    Minv = inverse(M)
    InD = {'.':1,'*':0}
    X0 = []
    for _ in range(n):
        X0 += map((lambda x: InD[x]),input())
    S = mv_prod(Minv,X0)
    OutD = ['.','X']
    for i in range(n):
        print(''.join(map((lambda x: OutD[x]),S[i*n:(i+1)*n])))

main()
