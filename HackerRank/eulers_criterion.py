#!/usr/bin/env python3

# https://en.wikipedia.org/wiki/Euler's_criterion

# for p an odd prime, a coprime to p (i.e. not a multiple of p here)
def euler_criterion(a,p):
    return pow(a,(p-1)//2,p)==1

def main():
    T = int(input())
    for _ in range(T):
        A,M = map(int,input().split())
        if A==0 or M==2:
            print('YES')
        else:
            print('YES' if euler_criterion(A,M) else 'NO')

main()
