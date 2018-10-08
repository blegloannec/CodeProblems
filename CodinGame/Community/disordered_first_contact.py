#!/usr/bin/env python3

def encode_perm(n):
    P = []
    l = 1
    i = 0
    while i<n:
        if l%2==1:
            P += list(range(i,min(i+l,n)))
        else:
            P = list(range(i,min(i+l,n)))+P
        i += l
        l += 1
    return P

def compose(A,B):
    return [A[b] for b in B]

def inverse(P):
    I = [0]*len(P)
    for i in range(len(P)):
        I[P[i]] = i
    return I

def main():
    N = int(input())
    M = input()
    P0 = encode_perm(len(M))
    if N>0:
        P0 = inverse(P0)
    else:
        N = -N
    P = list(range(len(M)))
    for _ in range(N):  # could be done through fast exp if N was large
        P = compose(P,P0)
    C = ''.join(M[p] for p in P)
    print(C)

main()
