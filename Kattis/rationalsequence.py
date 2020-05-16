#!/usr/bin/env python3

def next_frac(p,q):
    if q==1:
        return (1,p+1)
    l,p = divmod(p,q)
    q -= p
    p += q
    q += l*p
    return (p,q)

def main():
    T = int(input())
    for _ in range(T):
        k,pq = input().split()
        p,q = map(int, pq.split('/'))
        a,b = next_frac(p,q)
        print(f'{k} {a}/{b}')

main()
