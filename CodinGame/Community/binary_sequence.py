#!/usr/bin/env python3

def get_bit(i):
    if i == 0:
        return 0
    i -= 1
    k = 1
    while k<<(k-1) <= i:
        i -= k<<(k-1)
        k += 1
    q, r = divmod(i, k)
    n = (1<<(k-1)) | q
    b = (n>>(k-1-r)) & 1
    return b

N = int(input())
for _ in range(N):
        print(get_bit(int(input(), 2)))
