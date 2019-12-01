#!/usr/bin/env python3

def parse(i=0):
    if E[i]=='R':
        return R[ord(E[i+1])-ord('1')], i+2
    assert E[i]=='('
    X = []
    while E[i]!=')':
        assert E[i] in '(-|'
        op = E[i]
        x,i = parse(i+1)
        X.append(x)
    assert op!='(' # kinda correct for ((...)) or (Rx), but should not happen
    r = sum(X) if op=='-' else 1./sum(1./x for x in X)
    return r, i+1

def main():
    global E,R
    N = int(input())
    R = list(map(float,input().split()))
    E = input()
    print(parse()[0])

main()
