#!/usr/bin/env python3

# a = bh/2

b,a = map(int,input().split())
h = (2*a+b-1)//b
print(h)
