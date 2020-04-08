#!/usr/bin/env python3

S = 5

def tie(a,b):
    for i in range(S):
        for j in range(S):
            I = Cards[a][i] & Cards[b][j]
            if I:
                for x in I:
                    U = Cards[a][i] | Cards[b][j]
                    U.remove(x)
                    if all(not Cards[c][k]<=U  \
                           for c in range(N)   \
                           if c!=a and c!=b    \
                           for k in range(S)):
                        return True
    return False

def main():
    global N, Cards
    N = int(input())
    Cards = []
    for i in range(N):
        if i>0:
            input()
        Cards.append([set(map(int,input().split())) for _ in range(S)])
    for a in range(N):
        for b in range(a+1,N):
            if tie(a,b):
                print(a+1,b+1)
                return
    print('no ties')

main()
