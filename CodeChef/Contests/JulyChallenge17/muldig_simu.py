#!/usr/bin/env python3

B = 7
M = [0]*10**5
for i in range(B):
    M[i] = i
M[B] = 4
M[B+1] = 4
M[B+2] = 5
M[B+3] = 6

def main():
    F = [list(map(int,input().split())) for i in range(B)]
    K = int(input())
    for _ in range(K):
        a,b,c = map(int,input().split())
        if a<0:
            print(M[:30])
        else:
            M[c] = F[M[a]][M[b]]
    print(M[:30])


main()
