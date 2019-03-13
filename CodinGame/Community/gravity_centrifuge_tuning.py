#!/usr/bin/env python3

# non-consecutive digits Fibonacci base
# see also https://en.wikipedia.org/wiki/Zeckendorf%27s_theorem (& PE 297)

def fibo(n):
    u0,u1 = 1,2
    U = [1]
    while u1<=n:
        U.append(u1)
        u1,u0 = u1+u0,u1
    return U

# greedy zeckendorf decomp
def zeck(n):
    L = fibo(n)
    i = len(L)-1
    D = []
    while n>0:
        if L[i]<=n:
            D.append(i)
            n -= L[i]
        i -= 1
    return D

if __name__=='__main__':
    N = int(input())
    if N==0:
        print(0)
    else:
        B = zeck(N)
        Stream = [0]*(B[0]//3+1)
        for b in B:
            q,r = divmod(b,3)
            Stream[q] |= 1<<r
        print(''.join(map(str,reversed(Stream))))
