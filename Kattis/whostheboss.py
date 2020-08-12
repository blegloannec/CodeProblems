#!/usr/bin/env python3

import sys
input = sys.stdin.readline

class Employee:
    def __init__(self, i, s, h):
        self.ID = i; self.s = s; self.h = h
        self.boss = None
        self.subo = 0
    def __lt__(self, B):
        return self.s < B.s

def main():
    M,Q = map(int, input().split())
    E = sorted(Employee(*map(int, input().split())) for _ in range(M))
    ID2idx = {e.ID: i for i,e in enumerate(E)}
    # precomp: next >= (for h) element
    S = [E[-1]]
    for i in range(M-2,-1,-1):
        while E[i].h > S[-1].h:
            S.pop()
        E[i].boss = S[-1]
        S.append(E[i])
    # precomp: subtrees sizes computation
    for i in range(M-1):
        E[i].boss.subo += 1 + E[i].subo
    # answering queries
    for _ in range(Q):
        ID = int(input())
        i = ID2idx[ID]
        boss = 0 if E[i].boss is None else E[i].boss.ID
        sys.stdout.write(f'{boss} {E[i].subo}\n')

main()
