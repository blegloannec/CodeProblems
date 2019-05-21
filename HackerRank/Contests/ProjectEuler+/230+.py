#!/usr/bin/env python3

if __name__=='__main__':
    Q = int(input())
    for _ in range(Q):
        A,B,N = input().split()
        N = int(N)
        if N<=len(A):
            k = 0
        else:
            F = [len(A),len(B)]
            while F[-1]<N:
                F.append(F[-2]+F[-1])
            k = len(F)-1
            while k>1:
                if N>F[k-2]:
                    N -= F[k-2]
                    k -= 1
                else:
                    k -= 2
        print((A,B)[k][N-1])
