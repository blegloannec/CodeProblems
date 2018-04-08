#!/usr/bin/env python3

import sys

def send(x,y):
    print(x,y)
    sys.stdout.flush()

def recv():
    return tuple(map(int,input().split()))

def case(H,W):
    for i in range(H):
        x = 3*i+2
        for j in range(W):
            y = 3*j+2
            S = set()
            while len(S)<9:
                send(x,y)
                a,b = recv()
                if a==b==0:
                    return True
                S.add((a,b))
    return False

def main():
    T = int(input())
    for _ in range(T):
        A = int(input())
        # 9x3 = 27 for 20, 18x13 = 216 for 200
        H,W = (3,1) if A==20 else (6,4)
        case(H,W)

main()
