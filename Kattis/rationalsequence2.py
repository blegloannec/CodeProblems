#!/usr/bin/env python3

def idx_frac(p,q):
    i = 0
    l = 1
    while p!=q:
        if p<q:
            q -= p
        else:
            p -= q
            i |= l
        l <<= 1
    i |= l
    return i

def main():
    T = int(input())
    for _ in range(T):
        k,pq = input().split()
        p,q = map(int, pq.split('/'))
        i = idx_frac(p,q)
        print(f'{k} {i}')

main()
