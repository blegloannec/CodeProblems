#!/usr/bin/env python3

from itertools import product

def main():
    T = int(input())
    for t in range(1,T+1):
        N,L = map(int,input().split())
        W = set(input() for _ in range(N))
        C = [set() for _ in range(L)]
        for w in W:
            for i in range(L):
                C[i].add(w[i])
        P = 1
        for i in range(L):
            P *= len(C[i])
        if P<=N:
            w = '-'
        else:
            for X in product(*C):
                w = ''.join(X)
                if w not in W:
                    break
        print('Case #%d: %s' % (t,w))

main()
