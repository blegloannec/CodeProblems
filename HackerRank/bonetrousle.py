#!/usr/bin/env python3

# Thm: N can be decomposed as a sum of B distinct positive integers <= K
#      iff B(B+1)/2 <= N <= B(2K-B+1)/2

def decomp(N,K,B):
    if not ((B*(B+1))//2 <= N <= (B*(2*K-B+1))//2):
        return [-1]
    Sol = []
    while B:
        n = min(K, N-((B-1)*B)//2)
        Sol.append(n)
        N -= n
        K = n-1
        B -= 1
    return Sol

if __name__=='__main__':
    T = int(input())
    for _ in range(T):
        N,K,B = map(int,input().split())
        print(*decomp(N,K,B))
