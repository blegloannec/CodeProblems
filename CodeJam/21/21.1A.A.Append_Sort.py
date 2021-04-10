#!/usr/bin/env python3

def comp(a, b):
    ib = int(b)
    if int(a)<ib:
        return b
    if len(a)==len(b):
        return b+'0'
    #assert len(b)<len(a)
    ia0 = int(a[:len(b)])
    if ia0<ib:
        return b+'0'*(len(a)-len(b))
    if ia0>ib:
        return b+'0'*(len(a)-len(b)+1)
    a1 = a[len(b):]
    if all(c=='9' for c in a1):
        return b+'0'*(len(a)-len(b)+1)
    b1 = str(int(a1)+1).zfill(len(a1))
    return b+b1

def main():
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        X = input().split()
        y = X[0]
        res = 0
        for i in range(1, N):   
            y = comp(y, X[i])
            res += len(y)-len(X[i])
        print(f'Case #{t}: {res}')

main()
