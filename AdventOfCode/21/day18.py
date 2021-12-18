#!/usr/bin/env python3

# Going lazy on this one...

import sys
from copy import *

def is_leaf(n):
    return isinstance(n, int)

def is_pair(n):
    return isinstance(n, list)

def child_idx(u, v):
    return 0 if v is u[0] else 1

 # moves value v from u in direction d
 # (similar to finding pred/succ in a BST)
def move_incr(u, path, d, v):
    for p in reversed(path):
        if u is p[d]:
            u = p
        else:
            if is_pair(p[d]):
                u = p[d]
                while is_pair(u[d^1]):
                    u = u[d^1]
                u[d^1] += v
            else:
                p[d] += v
            break

def explode(n, path):
    a,b = n
    move_incr(n, path, 0, a)
    move_incr(n, path, 1, b)
    path[-1][child_idx(path[-1], n)] = 0

def split(n, path):
    m = n//2
    path[-1][child_idx(path[-1], n)] = [m, n-m]

def reduce_explode(n, path):
    if is_pair(n):
        if len(path)>=4 and is_leaf(n[0]) and is_leaf(n[1]):
            explode(n, path)
            return True
        path.append(n)
        if reduce_explode(n[0], path) or \
           reduce_explode(n[1], path):
            return True
        path.pop()
    return False

def reduce_split(n, path):
    if is_pair(n):
        path.append(n)
        if reduce_split(n[0], path) or \
           reduce_split(n[1], path):
            return True
        path.pop()
    elif n>=10:
        split(n, path)
        return True
    return False

def reduce(n):
    while reduce_explode(n, []) or reduce_split(n, []):
        pass

def add(n1, n2):
    s = [deepcopy(n1), deepcopy(n2)]
    reduce(s)
    return s

def magnitude(n):
    if is_pair(n):
        return 3*magnitude(n[0]) + 2*magnitude(n[1])
    return n


# Input
I = [eval(L) for L in sys.stdin.readlines()]

# Part 1
s = deepcopy(I[0])
for n in I[1:]:
    s = add(s,n)
print(magnitude(s))

# Part 2
smax = 0
for i in range(len(I)):
    for j in range(len(I)):
        if i!=j:
            s = add(I[i],I[j])
            smax = max(smax, magnitude(s))
print(smax)
