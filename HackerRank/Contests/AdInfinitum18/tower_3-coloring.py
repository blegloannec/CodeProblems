#!/usr/bin/env python3

# le nb de coloriages est 3^(3^n)

P = 10**9+7
phiP = P-1
n = int(input())
print(pow(3,pow(3,n,phiP),P))
