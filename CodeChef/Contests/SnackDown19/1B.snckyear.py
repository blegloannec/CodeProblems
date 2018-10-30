#!/usr/bin/env python3

Y = {2010, 2015, 2016, 2017, 2019}

T = int(input())
for _ in range(T):
    N = int(input())
    print(('' if N in Y else 'NOT ')+'HOSTED')
