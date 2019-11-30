#!/usr/bin/env python3

from functools import lru_cache

S = 15

@lru_cache(maxsize=None)
def win(x,y):
    for vx,vy in ((x-2,y+1),(x-2,y-1),(x+1,y-2),(x-1,y-2)):
        if 0<=vx<S and 0<=vy<S:
            if not win(vx,vy):
                return True
    return False

def main():
    T = int(input())
    for _ in range(T):
        x,y = map(int,input().split())
        print('First' if win(x-1,y-1) else 'Second')

main()
