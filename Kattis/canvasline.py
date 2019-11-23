#!/usr/bin/env python3

def main():
    N = int(input())
    LR = [tuple(map(int,input().split())) for _ in range(N)]  # sorted
    P = int(input())
    X = list(map(int,input().split()))  # sorted
    SX = set(X)
    i = 0
    O = []
    for l,r in LR:
        p = 0
        while i<P and X[i]<r:
            if X[i]>=l:
                p += 1
            i += 1
        if i<P and X[i]==r:
            p += 1
        if p>2:
            print('impossible')
            return
        elif p==2:
            if O and O[-1]==l:
                O[-1] -= 2 if O[-1]-1 in SX else 1
        elif p==1:
            if not (O and O[-1]==l):
                O.append(r-1 if i<P and X[i]==r else r)
        else:
            if not (O and O[-1]==l):
                O.append(r-2)
            O.append(r)
    print(len(O))
    print(*O)

main()
