#!/usr/bin/env python2

memo = {}
def game(n,i):
    #assert H[i]<=n
    if (n,i) not in memo:
        res = 1
        for j in xrange(i,len(Div)):
            d = Div[j]
            if d*d>n:
                break
            q,r = divmod(n,d)
            if r==0 and Div[j+1]<=q:
                b = 1 + game(q, j+1)
                if b<res:
                    break
                else:
                    res = b
        memo[n,i] = res
    return memo[n,i]

def main():
    global Div
    N = int(input())
    Div = [1]
    n = N
    while n&1==0:
        n >>= 1
        Div.append(Div[-1]<<1)
    p = 3
    while n>1 and p*p<=n:
        if n%p==0:
            L = len(Div)
            q = p
            while n%p==0:
                for i in xrange(L):
                    Div.append(q * Div[i])
                n //= p
                q *= p
        p += 2
    if n>1:
        for i in xrange(len(Div)):
            Div.append(n*Div[i])
    Div.sort()
    print(game(N,1))

main()
