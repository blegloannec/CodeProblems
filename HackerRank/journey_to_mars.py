#!/usr/bin/env python3

# first and last K digits of 2^(N-1)

from decimal import *

T = int(input())
for _ in range(T):
    N,K = map(int,input().split())
    Flog = (N-1) * Decimal(2).log10()
    Flog -= Flog.to_integral(rounding=ROUND_FLOOR)
    F = (Decimal(10)**(Flog+K-1)).to_integral(rounding=ROUND_FLOOR)
    L = pow(2,N-1,10**K)
    print(F+L)
