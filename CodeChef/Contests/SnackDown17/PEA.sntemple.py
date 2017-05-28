#!/usr/bin/env python3

def temple(H):
    A = [1]*len(H)
    # A[i] = plus grand escalier croissant se terminant en i
    for i in range(1,len(H)):
        A[i] = min(H[i],A[i-1]+1)
    B = [1]*len(H)
    # B[i] = plus grand escalier decroissant commencant en i
    for i in range(len(H)-2,-1,-1):
        B[i] = min(H[i],B[i+1]+1)
    # h = taille du plus grand temple possible
    h = max(min(A[i],B[i]) for i in range(len(H)))
    # un temple de taille h utilise h^2 blocs, on elimine le reste
    return sum(H)-h*h

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        H = list(map(int,input().split()))
        print(temple(H))

main()
