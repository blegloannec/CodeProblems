#!/usr/bin/env python3

# size 2n   -> 1pq1      with p = [01]^(n-1) and q the mirror of p
# size 2n+1 -> 1p[01]q1  idem

def pal_bin(M):
    Start = ('0','1','11','101','111')
    if M<len(Start):
        return Start[M]
    M -= len(Start)
    k = 1
    odd = 0
    while M >= (odd+1) * 2**k:
        M -= (odd+1) * 2**k
        odd ^= 1
        if odd==0:
            k += 1
    form = '{:0%db}' % k
    if odd==0:
        p = form.format(M)
        mid = ''
    else:
        m,r = divmod(M,2)
        p = form.format(m)
        mid = str(r)
    return '1' + p + mid + p[::-1] + '1'

M = int(input())
print(int(pal_bin(M),2))
