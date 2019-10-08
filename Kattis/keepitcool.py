#!/usr/bin/env python3

def main():
    N,M,S,D = map(int,input().split())
    C = list(map(int,input().split()))
    I = sorted(range(S), key=(lambda i: C[i]))
    O = [0]*S
    i = 0
    while N:
        O[I[i]] += min(N, D-C[I[i]])
        N -= O[I[i]]
        i += 1
    cold = sum(C[i] for i in range(S) if O[i]==0)
    if cold>=M:
        print(*O)
    else:
        print('impossible')

main()
