#!/usr/bin/env python3

def minimize(DigCnt):
        if DigCnt[0]==sum(DigCnt):
            return 0 if DigCnt[0]==1 else -1
        S = ''.join(str(i)*DigCnt[i] for i in range(1,10))
        return int(S[0] + '0'*DigCnt[0] + S[1:])

def minA_minB(Dig, Emax=18):
    if len(Dig)==1 or (len(Dig)>2 and max(Dig)==0):
        return -1,-1
    A = [0]*10
    for c in Dig:
        A[c] += 1
    if A[0]>=Emax and A[1]>0 and (sum(A[1:])>1 or A[0]==Emax+1):
        A[0] -= Emax
        A[1] -= 1
        B = [Emax,1] + [0]*8
    else:
        B = [0]*10
        SizeA, SizeB = sum(A), 0
        c = 9
        while SizeA>1 and SizeB<Emax:
            k = min(A[c], SizeA-1, Emax-SizeB)
            A[c]  -= k
            SizeA -= k
            B[c]  += k
            SizeB += k
            c -= 1
        if 1<SizeA==A[0]:
            c = next(c for c in range(1,10) if B[c]>0)
            A[0] -= 1
            B[0] += 1
            B[c] -= 1
            A[c] += 1
    a, b = minimize(A), minimize(B)
    if a>10**Emax or a<0 or b<0:
        return -1,-1
    return a,b

print(*minA_minB(list(map(int,input()))))
