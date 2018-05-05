#!/usr/bin/env python3

from fractions import *

def lcm(a,b):
    return a*b//gcd(a,b)

def parse_mol(S):
    n = len(S)
    M = {}
    i = 0
    while i<n:
        A = S[i]
        i += 1
        if i<n and 'a'<=S[i]<='z':
            A += S[i]
            i += 1
        m = 0
        while i<n and '0'<=S[i]<='9':
            m = 10*m + ord(S[i])-ord('0')
            i += 1
        if m==0:
            m = 1
        M[A] = m
    return M

def solve(S):
    # Gaussian elimination
    h,w = len(S),len(S[0])
    assert(h>=w-1)
    for i in range(w-1):
        j = next(j for j in range(i,h) if S[j][i]!=0)
        if j>i:
            S[i],S[j] = S[j],S[i]
        for j in range(i+1,h):
            if S[j][i]!=0:
                a = S[j][i]/S[i][i]
                for k in range(i,w):
                    S[j][k] -= a*S[i][k]
    # backwards solution extraction
    B = [Fraction(1)]*w
    for i in range(w-2,-1,-1):
        B[i] = -sum(S[i][j]*B[j] for j in range(i+1,w))/S[i][i]
    # smallest integer solution
    l = 1
    for b in B:
        l = lcm(l,b.denominator)
    for i in range(w):
        B[i] = B[i].numerator*l//B[i].denominator
    return B

def main():
    # parsing input
    L,R = input().split(' -> ')
    L = L.split(' + ')
    LM = list(map(parse_mol,L))
    R = R.split(' + ')
    RM = list(map(parse_mol,R))
    A = set()
    for M in LM+RM:
        for a in M:
            A.add(a)
    A = list(A)
    NumA = {A[i]:i for i in range(len(A))}
    # building the system
    S = [[Fraction(0)]*(len(L)+len(R)) for _ in range(len(A))]
    for i in range(len(L)):
        for a in LM[i]:
            S[NumA[a]][i] = Fraction(LM[i][a])
    for i in range(len(R)):
        for a in RM[i]:
            S[NumA[a]][len(L)+i] = Fraction(-RM[i][a])
    B = solve(S)
    # printing solution
    SolL = ' + '.join([(str(B[i]) if B[i]>1 else '')+L[i] for i in range(len(L))])
    SolR = ' + '.join([(str(B[len(L)+i]) if B[len(L)+i]>1 else '')+R[i] for i in range(len(R))])
    Sol = SolL+' -> '+SolR
    print(Sol)

main()
