#!/usr/bin/env python3

# la borne de 5000 est TRES TRES large pour du 10 x 10 max
# il faut moins de 2m+10 etapes pour vider une ligne

# ******.  ==>  ......*
def solve_line(l,n):
    S = []
    for i in range(n-2,0,-2):
        S.append((l,i,l,i+2))
    if n%2==0:
        S.append((l,1,l,2))
    for i in range(2+n%2,n,2):
        S.append((l,i+2,l,i+1))
        S.append((l,i,l,i+2))
    return S

# ***  ==>  **.
# ..*       ...
def transition(l,n):
    return [(l,n-1,l+1,n-1),(l+1,n,l+1,n-2),(l,n,l+1,n),(l+1,n-2,l+1,n-1),(l+1,n,l+1,n-2),(l+1,n-2,l+1,n-1),(l+1,n-1,l,n-1)]

# deplacer le trou en bas a droite
def move_hole(n,m,i,j):
    S = []
    while i<n:
        S.append((i+1,j,i,j))
        i += 1
    while j<m:
        S.append((i,j+1,i,j))
        j += 1
    return S

# resolution
def solve(n,m,i0,j0):
    S = move_hole(n,m,i0,j0)
    for i in range(n,0,-1):
        S += solve_line(i,m)
        if i>1:
            S += transition(i-1,m)
    return S

# position initiale du trou
def hole(G):
    for i in range(len(G)):
        for j in range(len(G[i])):
            if G[i][j]=='.':
                return (i+1,j+1)

def main():
    T = int(input())
    for _ in range(T):
        n,m = map(int,input().split())  # lines, columns
        G = [input() for _ in range(n)]
        if n<=2 and m<=2:
            # les cas particuliers...
            if n==m:
                print(-1)
            else:
                print(0)
        else:
            i0,j0 = hole(G)
            transpo = False
            if n>m:
                transpo = True
                n,m = m,n
                i0,j0 = j0,i0
            S = solve(n,m,i0,j0)
            print(len(S))
            for (a,b,c,d) in S:
                if transpo:
                    print(b,a,d,c)
                else:
                    print(a,b,c,d)

main()
