#!/usr/bin/env python3

from itertools import permutations

# lazy solution using python itertools
# could have used Heap's algo instead

def fact(n):
    return 1 if n<=1 else n*fact(n-1)

n = int(input())
print(fact(n))
for P in permutations(range(1,n+1)):
    print(' '.join(map(str,P)))
