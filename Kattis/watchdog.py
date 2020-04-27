#!/usr/bin/env python3

def leash(S, P):
    for x in range(S+1):
        for y in range(S+1):
            d2 = 0
            for u,v in P:
                if x==u and y==v:
                    d2 = float('inf')
                    break
                d2 = max(d2, (x-u)**2 + (y-v)**2)
            if d2 <= min(x, S-x, y, S-y)**2:
                return (x,y)
    return None

def main():
    N = int(input())
    for _ in range(N):
        S, H = map(int, input().split())
        P = [tuple(map(int, input().split())) for _ in range(H)]
        pos = leash(S, P)
        if pos is None:
            print('poodle')
        else:
            print(*pos)

main()
