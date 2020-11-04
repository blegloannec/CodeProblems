#!/usr/bin/env python3

from itertools import combinations

def test(Sentences, Lies):
    for seq, lie in Sentences:
        if sum(int(Lies[i]) for i in seq)&1 != lie:
            return False
    return True

def main():
    N = int(input())
    L = int(input())
    Sentences = []
    for _ in range(N):
        s = input()
        lie = s[-1]=='L'
        seq = tuple(map(int, s[:-2].split('>')))
        Sentences.append((seq, lie))
    for Liars in combinations(range(N), L):
        Lies = [False]*N
        for i in Liars:
            Lies[i] = True
        if test(Sentences, Lies):
            print(*Liars)
            break

main()
