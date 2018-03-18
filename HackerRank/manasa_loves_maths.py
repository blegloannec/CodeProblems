#!/usr/bin/env python3

# 8 = 2^3 | 10^k pour k>=3 donc les 3 bons derniers chiffres en base 10
# sont suffisants

def sig(n,k=3):
    s = [0]*10
    while n or k:
        s[n%10] += 1
        n //= 10
        if k:
            k -= 1
    return tuple(s)

S3 = set(sig(n) for n in range(0,1000,8))

def test(N):
    if len(N)<3:
        return int(N)%8==0 or int(N[::-1])%8==0
    sn = sig(int(N))
    return any(all(s[i]<=sn[i] for i in range(10)) for s in S3)

def main():
    T = int(input())
    for _ in range(T):
        N = input()
        print('YES' if test(N) else 'NO')

main()
