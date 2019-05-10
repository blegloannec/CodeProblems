#!/usr/bin/env python3

# https://en.wikipedia.org/wiki/Constructible_polygon

F = [3, 5, 17, 257, 65537]  # Fermat primes

def gen_prod(i=0, x=1):
    if i==len(F):
        yield x
    else:
        yield from gen_prod(i+1, x)
        yield from gen_prod(i+1, x*F[i])

if __name__=='__main__':
    a,b = map(int,input().split())
    count = 0
    for x in gen_prod():
        while x<=b:
            if x>=a:
                count += 1
            x <<= 1
    print(count)
