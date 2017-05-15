#!/usr/bin/env python3

from math import sqrt

# maximize h such that there exists a>=1 such that
# h * (a + a+h-1) / 2 = n
# 2a+h-1 >= h+1 > h
# hence h < sqrt(2n)

n = 2*int(input())
h = int(sqrt(n))
while n%h!=0 or (n//h-h)%2==0:
    h -= 1

a = ((n//h-h)+1)//2
print('\n'.join('*'*i for i in range(a,a+h)))
