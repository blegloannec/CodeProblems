#!/usr/bin/env python3

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int,input().split()))
        B = list(map(int,input().split()))
        AB = sorted(((a+b,i) for i,a,b in zip(range(N),A,B)), reverse=True)
        SA = sum(A[AB[i][1]] for i in range(0,N,2))
        SB = sum(B[AB[i][1]] for i in range(1,N,2))
        print('Tie' if SA==SB else 'First' if SA>SB else 'Second')

main()
