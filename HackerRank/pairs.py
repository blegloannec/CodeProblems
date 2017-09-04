#!/usr/bin/env python3

# NB : pas de doublons dans le tableau d'entree

# Methode 1 : tri et on fait avancer 2 pointeurs, O(n log n)
def methode1(): 
    N,K = map(int,input().split())
    A = sorted(map(int,input().split()))
    res = 0
    i,j = 0,1
    while i<N-1:
        while j<N and A[j]-A[i]<K:
            j += 1
        if j<N and A[j]-A[i]==K:
            res += 1
        i += 1
    print(res)

#methode1()

# Methode 2 : table de hashage, O(n)
def methode2():
    N,K = map(int,input().split())
    A = set(map(int,input().split()))
    res = 0
    for a in A:
        if a+K in A:
            res += 1
    print(res)

methode2()
