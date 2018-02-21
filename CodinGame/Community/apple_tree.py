#!/usr/bin/env python3

def inter(i,j):
    return (A[i][0]-A[j][0])**2 + (A[i][1]-A[j][1])**2 < (A[i][3]+A[j][3])**2

def main():
    global A
    N,i0 = map(int,input().split())
    A = [tuple(map(int,input().split())) for _ in range(N)]
    a0 = A[i0]
    A.sort(key=(lambda x: x[2]))
    i0 = A.index(a0)
    F = [i0]
    for i in range(i0-1,-1,-1):
        if any(inter(i,j) for j in F):
            F.append(i)
    print(N-len(F))

main()
