#!/usr/bin/env python3

import sys
input = sys.stdin.readline

def main():
    N,M = map(int, input().split())
    Ideg = [0]*N
    Odeg = [0]*N
    for _ in range(M):
        a,b = map(int, input().split())
        a -= 1
        b -= 1
        Ideg[b] += 1
        Odeg[a] += 1
    first = last = None
    for u in range(N):
        if Ideg[u]+1==Odeg[u]:
            if first is None:
                first = u+1
            else:
                print('no')
                return
        elif Ideg[u]==Odeg[u]+1:
            if last is None:
                last = u+1
            else:
                print('no')
                return
        elif Ideg[u]!=Odeg[u]:
            print('no')
            return
    if first is last is None:
        print('anywhere')
    elif first is not None and last is not None:
        print(first,last)
    else:
        print('no')

main()
