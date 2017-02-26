#!/usr/bin/env python3

from math import sqrt

# pout M fixe, on cherche tous les couples (a,b)
# tels que a^2-b^2 <= M avec 0 < b < a
# et b = a-2k, ie b de meme parite que a
# a+b = 2l pair
# a^2-b^2 = (a-b)(a+b) = 4kl <= M avec 1<k<l
# donc k < sqrt(M/4)

M = int(input())//4
S = int(sqrt(M))
cpt = sum(M//k-k for k in range(1,S+1))
print(cpt)
