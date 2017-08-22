#!/usr/bin/env python3

# DP for SCSup (analog to LCSub)
def SCS(A,B):
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
    # building the solution
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
        elif SCS[i][j]==1+SCS[i-1][j]:
            Sup.append(A[i-1])
            i -= 1
        else:
            # NB: equality also falls here
            Sup.append(B[j-1])
            j -= 1
    return ''.join(reversed(Sup))

S = input()
T = input()
print(SCS(S,T))
