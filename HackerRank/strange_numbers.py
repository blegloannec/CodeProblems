#!/usr/bin/env python3

def gen_strange():
    S = list(range(10))
    for l in range(2,19):
        i = l0 = 0
        while i<len(S) and l0<=l:
            x = S[i]*l
            l0 = len(str(x))
            if l0==l:
                S.append(x)
            i += 1
    return S

if __name__=='__main__':
    S = gen_strange()
    T = int(input())
    for _ in range(T):
        L,R = map(int,input().split())
        print(sum(int(L<=x<=R) for x in S))
