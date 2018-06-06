#!/usr/bin/env python3

# NB: comme on minimise la difference, alors a signe fixe,
# minimiser un des scores en cas d'egalite est equivalent
# a minimiser l'autre

# algo en O(N), vraisemblablement similaire au O(N^2) du
# corrige mais en pre-calculant les suffixes
def min_diff(A,B): # pour A <= B
    N = len(A)
    # pre-calcul des suffixes
    SA,SB = [0]*(N+1),[0]*(N+1)
    for i in range(N-1,-1,-1):
        # maximises avec des 9 pour A
        SA[i] = SA[i+1] + (9 if A[i]==None else A[i])*10**(N-1-i)
        # minimises avec des 0 pour B
        SB[i] = SB[i+1] + (0 if B[i]==None else B[i])*10**(N-1-i)
    currA,currB = 0,0
    Dmin,imin,Amin = float('inf'),0,float('inf')
    for i in range(N):
        if A[i]!=None and B[i]!=None:
            if A[i]!=B[i]: # premiere difference explicite
                currA += SA[i]
                currB += SB[i]
                tryD = currB-currA
                if 0<=tryD<Dmin or (tryD==Dmin and currA<Amin):
                    Dmin,imin,Amin = tryD,i,currA
                # FIN
                return Dmin,imin,Amin
            # sinon A[i] == B[i] et on continue
            currA += A[i]*10**(N-1-i)
            currB += B[i]*10**(N-1-i)
        elif A[i]==B[i]==None:
            # on considere une difference de 1 avec 0/1
            tryA = currA + SA[i+1]
            tryB = currB + 10**(N-1-i) + SB[i+1]
            tryD = tryB-tryA
            if 0<=tryD<Dmin or (tryD==Dmin and tryA<Amin):
                Dmin,imin,Amin = tryD,i,tryA
            # on continue en egalisant avec 0/0
            # donc currA et currB ne changent pas
        elif A[i]==None:
            # on considere une difference de 1
            if B[i]!=0:
                tryA = currA + (B[i]-1)*10**(N-1-i) + SA[i+1]
                tryB = currB + B[i]*10**(N-1-i) + SB[i+1]
                tryD = tryB-tryA
                if 0<=tryD<Dmin or (tryD==Dmin and tryA<Amin):
                    Dmin,imin,Amin = tryD,i,tryA
            # on continue en egalisant
            currA += B[i]*10**(N-1-i)
            currB += B[i]*10**(N-1-i)
        elif B[i]==None:
            # on considere une difference de 1
            if A[i]!=9:
                tryA = currA + A[i]*10**(N-1-i) + SA[i+1]
                tryB = currB + (A[i]+1)*10**(N-1-i) + SB[i+1]
                tryD = tryB-tryA
                if 0<=tryD<Dmin or (tryD==Dmin and tryA<Amin):
                    Dmin,imin,Amin = tryD,i,tryA
            # on continue en egalisant
            currA += A[i]*10**(N-1-i)
            currB += A[i]*10**(N-1-i)
    tryD = currB-currA
    if 0<=tryD<Dmin or (tryD==Dmin and currA<Amin):
        Dmin,imin,Amin = tryD,N,currA
    return Dmin,imin,Amin

def build_sol(A,B,d):
    N = len(A)
    for i in range(len(A)):
        if i<d:
            if A[i]==B[i]==None:
                A[i] = B[i] = 0
            elif A[i]==None:
                A[i] = B[i]
            elif B[i]==None:
                B[i] = A[i]
        elif i>d:
            if A[i]==None:
                A[i] = 9
            if B[i]==None:
                B[i] = 0
        else: # i = d
            if A[i]==B[i]==None:
                A[i] = 0
                B[i] = 1
            elif A[i]==None:
                A[i] = B[i]-1
            elif B[i]==None:
                B[i] = A[i]+1

def num(c):
    return None if c=='?' else ord(c)-ord('0')

def main():
    T = int(input())
    for t in range(1,T+1):
        C,J = map((lambda A: list(map(num,A))),input().split())
        D1,i1,Cmin1 = min_diff(C,J)
        Jmin1 = Cmin1+D1
        D2,i2,Jmin2 = min_diff(J,C)
        if D1<D2 or (D1==D2 and Jmin1<=Jmin2):
            build_sol(C,J,i1)
        else:
            build_sol(J,C,i2)
        C = ''.join(map(str,C))
        J = ''.join(map(str,J))
        print('Case #%d: %s %s' % (t,C,J))

main()
