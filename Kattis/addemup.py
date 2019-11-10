#!/usr/bin/env python3

DigRev = {'0':'0', '1':'1', '2':'2', '5':'5', '6':'9', '8':'8', '9':'6'}

def reverse(x):
    try:
        return int(''.join(DigRev[c] for c in reversed(str(x))))
    except KeyError:
        return None

def main():
    N,S = map(int,input().split())
    X = list(map(int,input().split()))
    Y = set()
    for x in X:
        rx = reverse(x)
        if S-x in Y or (rx is not None and S-rx in Y):
            print('YES')
            return
        Y.add(x)
        if rx is not None:
            Y.add(rx)
    print('NO')

main()
