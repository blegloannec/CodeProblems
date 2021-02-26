#!/usr/bin/env python3

# Variation of Josephus problem for k = 2
# https://en.wikipedia.org/wiki/Josephus_problem
# NB: can be derived from https://oeis.org/A006257
#     but is exactly      https://oeis.org/A152423

# f1/2(n) = nb (between 1 and n) of the remaining card
#           starting by eliminating the 1st/2nd card
# at each step we throw away half the cards (the odd/even
# ones for f1/f2 respectively)
# this could be factorized furthermore, but we keep it
# as is for readability of the cases
def f1(n):
    if n==1: return 1
    n,o = divmod(n,2)
    return 2*f2(n) if o else 2*f1(n)

def f2(n):
    if n==1: return 1
    n,o = divmod(n,2)
    return 2*f1(n+1)-1 if o else 2*f2(n)-1

n = int(input())
print(f1(n))
