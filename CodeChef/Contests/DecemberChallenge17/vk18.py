#!/usr/bin/env python3

NMAX = 10**6

def val(n):
    S = [0,0]
    while n:
        d = n%10
        S[d%2] += d
        n //= 10
    return abs(S[0]-S[1])

def main():
    R = [0]
    P = [0]
    S = [0]
    for i in range(1,NMAX+1):
        R.append(val(2*i-1))
        P.append(P[-1]+R[-1])
        R.append(val(2*i))
        P.append(P[-1]+R[-1])
        S.append(S[-1]+R[-1]+2*(P[-2]-P[-1-i]))
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(S[N])

main()
