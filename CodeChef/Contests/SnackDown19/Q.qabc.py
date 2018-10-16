#!/usr/bin/env python3

def transform(A,B):
    for i in range(len(A)):
        if i+2>=len(A):
            if A[i]!=B[i]:
                return False
        elif A[i]>B[i]:
            return False
        else:
            k = B[i]-A[i]
            A[i] += k      # (useless btw)
            A[i+1] += 2*k
            A[i+2] += 3*k
    return True

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int,input().split()))
        B = list(map(int,input().split()))
        print('TAK' if transform(A,B) else 'NIE')

main()
