#!/usr/bin/env python3

def prime(n):
    if n<=2:
        return n==2
    if n&1==0:
        return False
    d = 3
    while d*d<=n:
        if n%d==0:
            return False
        d += 2
    return True

# generating superprimes in increasing order
# turns out there are no superprime of size 9
# hence it stops at only 83 superprimes in total
# also it is https://oeis.org/A024770
def gen_superprimes():
    SP = [2,3,5,7]
    i = 0
    while i<len(SP):  # and SP[i]<10**8:
        for d in range(1,10,2):
            q = 10*SP[i] + d
            if prime(q):
                SP.append(q)
        i += 1
    return SP

def grids(h, w):
    if h==0:
        yield []
    else:
        for G in grids(h-1, w):
            for p in SP[w]:
                G.append(p)
                if all(''.join(G[i][j] for i in range(h)) in SP[h] for j in range(w)):
                    yield G
                G.pop()

def main():
    global SP
    SP = [[] for _ in range(9)]
    for p in map(str, gen_superprimes()):
        SP[len(p)].append(p)
    n,m = map(int, input().split())
    print(sum(1 for G in grids(n,m)))

main()
