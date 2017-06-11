#!/usr/bin/env python3

a = int(input())
if a%2==1:
    # a^2 impair
    # a^2 = 2k+1 = (k+1)^2 - k^2
    k = (a*a-1)//2
    print(a,k,k+1)
else:
    k = a//2
    # (m^2-n^2)^2 + (2mn)^2 = (m^2+n^2)^2
    # a = 2*k*1
    print(a,k*k-1,k*k+1)
