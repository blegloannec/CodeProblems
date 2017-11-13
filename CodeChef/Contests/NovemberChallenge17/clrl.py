#!/usr/bin/env python3

def check(A,R):
    inf,sup = 1,10**9
    for a in A:
        if a>R:
            if a>sup:
                return False
            sup = a
        else:
            if a<inf:
                return False
            inf = a
    return True

def main():
    T = int(input())
    for _ in range(T):
        N,R = map(int,input().split())
        A = list(map(int,input().split()))
        print('YES' if check(A,R) else 'NO')

main()
