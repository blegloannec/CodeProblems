#!/usr/bin/env python3

NMAX = 1001

def precomp():
    F = [None,[0]]
    for n in range(2,NMAX):
        F.append([0,1])
        u1,u0 = 1,1
        while (u1,u0)!=(1,0):
            F[n].append(u1)
            u1,u0 = (u1+u0)%n,u1
        F[n].pop()
    return F

def main():
    F = precomp()
    N = int(input())
    for _ in range(N):
        a,b,n = map(int,input().split())
        print(F[n][pow(a,b,len(F[n]))])

main()
