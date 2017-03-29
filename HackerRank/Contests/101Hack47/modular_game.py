#!/usr/bin/env python3

def main():
    n,p,q = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    S = [0]*n
    for a in A:
        for b in B:
            # 0 est envoye sur la derniere case
            S[(-(a+b))%n - 1] += 1
    print(S.index(min(S))+1)

main()
