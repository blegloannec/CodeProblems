#!/usr/bin/env python3

import sys

def simu(Y,C,E,S,F,A): # en O(Y)
    A = A[:] # copie locale
    i0 = 0 # indice tournant de l'age 0
    for _ in range(Y):
        i0 = (i0-1)%len(A)
        S -= A[i0]
        F += A[(i0+20)%len(A)]-A[(i0+E//2+1)%len(A)]
        A[i0] = F//10
        S += A[i0]
        if S>C:
            return False
    return S>=200

def main():
    Y = int(sys.stdin.readline())
    C = int(sys.stdin.readline())
    N = int(sys.stdin.readline())
    A = {}
    for _ in range(N):
        a,n = map(int,sys.stdin.readline().split())
        A[a] = n
    E = max(A)
    B = [0]*(E+1)
    for a in A:
        B[a] = A[a]
    S = sum(B)
    F = sum(B[20:E//2+1])
    L,R = None,None
    while R==None:
        if simu(Y,C,E,S,F,B):
            if L==None:
                L = E
        else:
            if L!=None:
                R = E-1
                break
        E += 1
        B.append(0)
        if E%2==0:
            F += B[E//2]
    print(L,R)

main()
