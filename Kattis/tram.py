#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# let's rotate everything by 45° so that the y = x line becomes
# the horizontal axis: (x,y)  ->  z = (y-x)/√2
#                  y = x + a  ->  z = b := a/√2
# minimize f(b) = ∑ (zᵢ-b)² = ∑ zᵢ² - 2zᵢb + b²
#          f'(b) = 2 ∑ b-zᵢ = 2 (nb - ∑ zᵢ)
# f'(b) = 0  <=>  b = ∑ zᵢ / n
# i.e. a = √2 ∑ (yᵢ-xᵢ)/√2 / n = ∑ (yᵢ-xᵢ) / n

def main():
    N = int(input())
    a = 0.
    for _ in range(N):
        x,y = map(int,input().split())
        a += y-x
    a /= N
    print(a)

main()
