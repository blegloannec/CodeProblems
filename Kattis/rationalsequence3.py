#!/usr/bin/env python3

def frac_idx(i):
    b = i.bit_length()
    l = 0 if b<2 else 1<<(b-2)
    p = q = 1
    while l:
        if i&l:
            p += q
        else:
            q += p
        l >>= 1
    return (p,q)

def main():
    T = int(input())
    for _ in range(T):
        k,i = map(int, input().split())
        p,q = frac_idx(i)
        print(f'{k} {p}/{q}')

main()
