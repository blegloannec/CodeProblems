#!/usr/bin/env python3

# approach probably slightly better (same complexity though)
# than the editorial's

def main():
    n = int(input())
    A = list(map(int,input().split()))
    for i in range(1,n):
        A[i] += A[i-1]
    T = A[-1]
    S = set(A)
    R = []
    for a in A:
        if T%a==0 and all(k*a in S for k in range(2,T//a+1)):
            R.append(a)
    print(*R)

main()
