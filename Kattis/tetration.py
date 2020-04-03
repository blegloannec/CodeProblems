#!/usr/bin/env python3

# x = a^(a^(a^...)), a^x = x, a = x^(1/x)

x = float(input())
a = x**(1./x)
print(a)
