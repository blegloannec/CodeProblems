#!/usr/bin/env python3

from functools import lru_cache

normalize = lambda T: tuple(sorted(t for t in T if t>0))

@lru_cache(maxsize=None)
def win(T, S):
    if S==0:
        return 0.
    if len(T)==0:
        return 1.
    p = 0.
    d = len(T)+2  # dice options: trees + max tree + raven
    T = list(T)
    for i in range(len(T)):
        T[i] -= 1
        coeff = 2 if i==len(T)-1 else 1  # max tree / other tree
        p += coeff * win(normalize(T), S)/d
        T[i] += 1
    p += win(normalize(T), S-1)/d
    return p

def main():
    R,G,B,Y,S = map(int, input().split())
    T = normalize((R,G,B,Y))
    print(win(T,S))

main()
