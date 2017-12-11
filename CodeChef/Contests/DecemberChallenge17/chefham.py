#!/usr/bin/env python3

from collections import defaultdict

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int,input().split()))
        if N==1:
            print(0)
            print(A[0])
            continue
        C = defaultdict(list)
        for i in range(N):
            C[A[i]].append(i)
        S = []
        D = []
        for v in C:
            if len(C[v])==1:
                S.append(C[v][0])
            else:
                D.append(tuple(C[v]))
        if len(S)==0 and len(D)==1:
            print(0)
            print(' '.join(map(str,A)))
        elif len(S)==1 and len(D)==1:
            print(2)
            A[S[0]],A[D[0][0]] = A[D[0][0]],A[S[0]]
            print(' '.join(map(str,A)))
        else:
            B = [0]*N
            if len(D)==1:
                s1 = S.pop()
                s2 = S.pop()
                d1,d2 = D.pop()
                B[s1],B[s2],B[d1],B[d2] = A[d1],A[d2],A[s1],A[s2]
            elif len(S)==1:
                a = S.pop()
                b,c = D[0]
                B[a] = A[b]
                A[a],A[b] = A[b],A[a]
            print(N)
            for i in range(len(S)):
                a,b = S[i],S[(i+1)%len(S)]
                B[a] = A[b]
            for i in range(len(D)):
                a1,b1 = D[i]
                a2,b2 = D[(i+1)%len(D)]
                B[a1],B[b1] = A[a2],A[b2]
            print(' '.join(map(str,B)))

main()
