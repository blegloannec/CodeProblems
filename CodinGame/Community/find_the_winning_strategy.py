#!/usr/bin/env python3

def move(P):
    X = 0
    for xp,xb in P:
        X ^= xb-xp-1
    assert X!=0
    for i,(xp,xb) in enumerate(P):
        x = xb-xp-1
        Xi = X^x
        if x>Xi:
            return (i,xp+x-Xi)
        # Variant (easier to see/prove)
        #if (x&X).bit_length()==X.bit_length():
        #    return (i,xp+x-(x^X))

if __name__=='__main__':
    rows = int(input())
    columns = int(input())
    while True:    
        P = [tuple(map(int,input().split())) for _ in range(rows)]
        print(*move(P))
