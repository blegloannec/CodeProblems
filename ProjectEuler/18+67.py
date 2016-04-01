#!/usr/bin/python

def zero(n):
    return [[0 for j in range(n)] for i in range(n)]

def make_table(path):
    f = open(path,'r')
    ll = [map(int,l.split(' ')) for l in f.readlines()]
    n = len(ll)
    M = zero(n)
    for i in range(n):
        for j in range(i+1):
            M[i-j][j] = ll[i][j]
    return M
        
def traite(M):
    N = len(M)
    for i in range(1,N):
        M[0][i] += M[0][i-1]
        M[i][0] += M[i-1][0]
    for i in range(1,N):
        for j in range(1,N):
            M[i][j] += max(M[i-1][j],M[i][j-1])
    # Pas optimal, on peut stopper a la diagonale
    print M[N-1][N-1]

def main():
    M18 = make_table('input/18_triangle.txt')
    traite(M18)
    M67 = make_table('input/67_triangle.txt')
    traite(M67)
    

main()
