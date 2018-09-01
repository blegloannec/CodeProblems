#!/usr/bin/env python

import sys

# so boooooooring...

def borders(i,j,n,m):
    res = 4
    if i==0:
        res -= 1
    if i==n-1:
        res -= 1
    if j==0:
        res -= 1
    if j==m-1:
        res -= 1
    return res

def comp(n,m,p):
    p1 = 1.-p
    P = [[0 for _ in xrange(3)] for _ in xrange(3)]
    for i in xrange(min(3,n)):
        for j in xrange(min(3,m)):
            b = borders(i,j,n,m)
            # proba de composante de taille 1 en (i,j)
            P[i][j] = p1**b
            V = filter((lambda (vx,vy): 0<=vx<n and 0<=vy<m), [(i-1,j),(i+1,j),(i,j-1),(i,j+1)])
            assert(len(V)==b)
            # proba de composante 2 en (i,j), divisee par 2 (car le voisin
            # contribuera aussi)
            for (vx,vy) in V:
                P[i][j] += (p * p1**(b-1) * p1**(borders(vx,vy,n,m)-1)) / 2.
            # proba que (i,j) soit le "centre" d'une composante de taille 3
            # (non divisee par 3 car les 2 voisins ne contribueront pas)
            for iv0 in xrange(len(V)):
                vx0,vy0 = V[iv0]
                for iv1 in xrange(iv0+1,len(V)):
                    vx1,vy1 = V[iv1]
                    P[i][j] += p**2 * p1**(b-2) * p1**(borders(vx0,vy0,n,m)-1) * p1**(borders(vx1,vy1,n,m)-1)
    return P

def fullcomp(n,m,p):
    P = [[0 for _ in xrange(m)] for _ in xrange(n)]
    for i in xrange(n):
        for j in xrange(m):
            b = borders(i,j,n,m)
            P[i][j] = (1-p)**b
            V = filter((lambda (vx,vy): 0<=vx<n and 0<=vy<m), [(i-1,j),(i+1,j),(i,j-1),(i,j+1)])
            assert(len(V)==b)
            for (vx,vy) in V:
                P[i][j] += (p * (1-p)**(b-1) * (1-p)**(borders(vx,vy,n,m)-1)) / 2.
            for iv0 in xrange(len(V)):
                vx0,vy0 = V[iv0]
                for iv1 in xrange(iv0+1,len(V)):
                    vx1,vy1 = V[iv1]
                    P[i][j] += p**2 * (1-p)**(b-2) * (1-p)**(borders(vx0,vy0,n,m)-1) * (1-p)**(borders(vx1,vy1,n,m)-1)
    return P

def main():
    q = int(sys.stdin.readline())
    for _ in xrange(q):
        n,m,p = sys.stdin.readline().split()
        n,m,p = int(n),int(m),float(p)
        n,m = min(n,m),max(n,m) # n <= m
        E = 0.
        if m<5:
            P = fullcomp(n,m,p)
            for i in xrange(n):
                for j in xrange(m):
                    E += P[i][j]
        elif n==1:
            P = comp(n,5,p)
            E = 2*P[0][0]+2*P[0][1]+(m-4)*P[0][2]
        elif n==2:
            P = comp(n,5,p)
            E = 4*P[0][0]+4*P[0][1]+2*(m-4)*P[0][2]
        elif n==3:
            P = comp(n,5,p)
            E = 4*P[0][0]+4*P[0][1]+2*P[1][0]+2*(m-4)*P[0][2]+(m-4)*P[1][2]+2*P[1][1]
        elif n==4:
            P = comp(n,5,p)
            E = 4*P[0][0]+8*P[0][1]+2*(m-4)*P[0][2]+2*(m-4)*P[1][2]+4*P[1][1]
        else:
            P = comp(5,5,p)
            inter = (n-4)*(m-4)
            bords = 2 * (n-4 + m-4)
            E = P[0][0]*4 + P[0][1]*8 + P[1][1]*4 + P[0][2]*bords + P[1][2]*bords + P[2][2]*inter
        print E/(n*m)
        

main()
