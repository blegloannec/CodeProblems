#!/usr/bin/env python3

def score(G):
    s1 = s2 = 0
    for i in range(len(G)):
        for j in range(len(G[i])):
            if (i+j)%2==0:
                if G[i][j]=='R':
                    s1 += 5
                else:
                    s2 += 3
            else:
                if G[i][j]=='G':
                    s1 += 3
                else:
                    s2 += 5
    return min(s1,s2)

def main():
    T = int(input())
    for _ in range(T):
        N,M = map(int,input().split())
        G = [input() for _ in range(N)]
        print(score(G))

main()
