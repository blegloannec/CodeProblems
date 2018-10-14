#!/usr/bin/env python3

def sum_div_range(n):
    return sum(d*(n//d) for d in range(1,n+1))

n = int(input())
print(sum_div_range(n))
