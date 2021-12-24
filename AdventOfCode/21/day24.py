#!/usr/bin/env python3

from functools import lru_cache

# Analyzing the program inputs/input24, we realize it is structured
# as 14 blocks of the form:
#  - read w as input
#  - execute f(X,Y,Z, w,z) below
#    for some parameters X,Y,Z depending on the block
#    and hardcoded in the list below (probably the only variable
#    part of the different provided inputs),
#    x and y are only used as local variables,
#    while the only persistent variable is z (initially z = 0)

# z can be seen as a base 26 number that either:
#  - gets a new digit appended   (when Z=1  and x!=w)
#  - remains the same            (when Z=1  and x =w)
#  - gets its last digit changed (when Z=26 and x!=w)
#  - get divided by 26           (when Z=26 and x =w)

XYZ = ((10,2,1),(15,16,1),(14,9,1),(15,0,1),(-8,1,26),(10,12,1),(-16,6,26),(-4,6,26),(11,3,1),(-3,5,26),(12,9,1),(-7,3,26),(-15,2,26),(-7,3,26))

def f(X,Y,Z, w,z):
    x = z%26 + X
    z //= Z
    if x!=w:
        z = 26*z + w+Y
    return z

# As we want z = 0 in the end, the number of remaining potential
# divisions by 26 gives an upper bound on the value of z at each step.

DIV = [0]*(len(XYZ)+1)
for i in range(len(XYZ)-1,-1,-1):
    DIV[i] = DIV[i+1] + (XYZ[i][2]==26)
ZMAX = [26**d for d in DIV]


# Part 1
# Memoized backtracking to find the highest sequence of w inputs
# that leads to z = 0.
# NB: A deeper analysis/understanding might lead to a smarter approach,
#     but this is good/fast enough...
W = []

@lru_cache(maxsize=None)
def search_max(i=0, z=0):
    if i==len(XYZ):
        return z==0
    if z>=ZMAX[i]:
        return False
    X,Y,Z = XYZ[i]
    for w in range(9,0,-1):
        W.append(w)
        z1 = f(X,Y,Z, w,z)
        if search_max(i+1, z1):
            return True
        W.pop()
    return False

assert search_max()
print(*W, sep='')


# Part 2
# Exact same as part 1 but with a reversed range on w.
W = []

@lru_cache(maxsize=None)
def search_min(i=0, z=0):
    if i==len(XYZ):
        return z==0
    if z>=ZMAX[i]:
        return False
    X,Y,Z = XYZ[i]
    for w in range(1,10):
        W.append(w)
        z1 = f(X,Y,Z, w,z)
        if search_min(i+1, z1):
            return True
        W.pop()
    return False

assert search_min()
print(*W, sep='')
