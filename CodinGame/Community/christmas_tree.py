#!/usr/bin/env python3

# ∑(k=0..h-1) ik+1 = i(h-1)h/2 + h
# ∑ ik+1 = n  <=>  i(h-1)h + 2h - 2n = 0
#             <=>  ih² + (2-i)h - 2n = 0
# Δ = (2-i)² + 8in

def formula(n, i):
    d = ((2-i)**2 + 8*i*(n-1))**0.5
    h = int((i-2+d)/(2*i))
    return n - i*(h-1)*h//2

def dicho(n, i):
    hl, hr = 0, 1<<60
    while hl < hr:
        h = (hl+hr+1)//2
        if i*(h-1)*h//2+h <= n-1:
            hl = h
        else:
            hr = h-1
    return n - i*(hl-1)*hl//2

if __name__=='__main__':
    n = int(input())
    i = int(input())
    print(formula(n,i))
    #print(dicho(n,i))
