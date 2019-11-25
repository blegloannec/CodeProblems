#!/usr/bin/env python3

def precomp(N=100001):
    Pi = [1]*N
    Pi[0] = Pi[1] = 0
    for p in range(2,N):
        if Pi[p]==1:
            for k in range(2*p,N,p):
                Pi[k] = 0
    for i in range(3,N):
        Pi[i] += Pi[i-1]
    return Pi

def main():
    Pi = precomp()
    G = int(input())
    for _ in range(G):
        N = int(input())
        print('Alice' if Pi[N]%2==1 else 'Bob')

main()
