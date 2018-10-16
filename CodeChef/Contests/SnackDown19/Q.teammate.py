#!/usr/bin/env python3

# simple optimal greedy choice: pair 2 of the strongest players

from itertools import groupby

P = 10**9+7
NMAX = 10**5+2
Fact2 = [1]*NMAX
for n in range(2,NMAX):
    Fact2[n] = (n*Fact2[n-2]) % P

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = sorted(map(int,input().split()))
        S = [(x,len(list(g))) for x,g in groupby(S)]
        res = 1
        while S:
            x,c = S.pop()
            if c==1:
                y,d = S.pop()
                if d>1:
                    res = (res*d) % P
                    S.append((y,d-1))
            elif c>2:
                if c%2==0:
                    res = (res*Fact2[c-1]) % P
                else:
                    res = (res*Fact2[c]) % P
                    S.append((x,1))
        print(res)

main()
