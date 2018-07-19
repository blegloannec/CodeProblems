#!/usr/bin/env python3

def gen_sub(K):
    used = set()
    G = []
    for c in K:
        if c not in used:
            G.append([c])
            used.add(c)
    col = 0
    for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if c not in used:
            G[col].append(c)
            col = (col+1)%len(G)
            used.add(c)
    G.sort()
    B = ''.join(''.join(Col) for Col in G)
    invSub = {B[i]: chr(i+ord('A')) for i in range(26)}
    invSub[' '] = ' '
    return invSub

def main():
    T = int(input())
    for _ in range(T):
        K = input()
        C = input()
        iSub = gen_sub(K)
        M = ''.join(iSub[c] for c in C)
        print(M)

main()
