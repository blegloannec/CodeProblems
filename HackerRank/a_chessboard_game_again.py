#!/usr/bin/env python3

from functools import lru_cache

def mex(X):
    x = 0
    while x in X:
        x += 1
    return x

S = 15

@lru_cache(maxsize=None)
def grundy(x,y):
    if x==y==0:
        return 0
    X = []
    for vx,vy in ((x-2,y+1),(x-2,y-1),(x+1,y-2),(x-1,y-2)):
        if 0<=vx<S and 0<=vy<S:
            X.append(grundy(vx,vy))
    return mex(X)

def main():
    T = int(input())
    for _ in range(T):
        K = int(input())
        G = 0
        for _ in range(K):
            x,y = map(int,input().split())
            G ^= grundy(x-1,y-1)
        print('First' if G!=0 else 'Second')

main()
