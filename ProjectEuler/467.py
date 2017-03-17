#!/usr/bin/env python3

from math import sqrt

# let #LCSub be the size of the longest common subsequence
# between 2 strings A,B and #SCSup the size of the shortest
# common supersequence
# then we guess #SCSup(A,B) = #A + #B - #LCSub(A,B)
# so that we should expect an analog O(n^2) DP algo
# (otherwise we would solve the other pb more efficiently)

def digits_sum(n,b=10):
    s = 0
    while n>0:
        s += n%b
        n //= b
    return s

def digit_root(n):
    return n if n<10 else digit_root(digits_sum(n))

def sieve(N):
    P = [True]*N
    for i in range(2,int(sqrt(N))+1):
        if P[i]:
            for k in range(2*i,N,i):
                P[k] = False
    return P

# DP for SCSup (analog to LCSub)
def super(A,B):
    # we reverse for lex-min stuff
    A,B = A[::-1],B[::-1]
    LA,LB = len(A),len(B)
    SCS = [[0]*(LB+1) for _ in range(LA+1)]
    for j in range(LB+1):
        SCS[0][j] = j
    for i in range(LA+1):
        SCS[i][0] = i
    for i in range(1,LA+1):
        for j in range(1,LB+1):
            if A[i-1]==B[j-1]:
                SCS[i][j] = 1+SCS[i-1][j-1]
            else:
                SCS[i][j] = 1+min(SCS[i-1][j],SCS[i][j-1])
    # building the lex-smallest solution
    Sup = []
    i,j = LA,LB
    while i>0 or j>0:
        if i==0:
            Sup.append(B[j-1])
            j -= 1
        elif j==0:
            Sup.append(A[i-1])
            i -= 1
        elif A[i-1]==B[j-1]:
            Sup.append(A[i-1])
            i -= 1
            j -= 1
        elif SCS[i-1][j]==SCS[i][j-1]:
            # we have to pick the lex-smallest here
            if A[i-1]<B[j-1]:
                Sup.append(A[i-1])
                i -= 1
            else:
                Sup.append(B[j-1])
                j -= 1
        elif SCS[i][j]==1+SCS[i-1][j]:
            Sup.append(A[i-1])
            i -= 1
        else:
            Sup.append(B[j-1])
            j -= 1
    return Sup

def main():
    M = 10**9+7
    N = 10000
    P = sieve(20*N)
    PD,CD = [],[]
    i = 2
    while len(PD)<N or len(CD)<N:
        if P[i]:
            if len(PD)<N:
                PD.append(digit_root(i))
        elif len(CD)<N:
            CD.append(digit_root(i))
        i += 1
    res = 0
    for x in super(PD,CD):
        res = (10*res+x)%M
    print(res)

main()
