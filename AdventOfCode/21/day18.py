#!/usr/bin/env python3

# Going lazy on this one...

import sys
from copy import deepcopy

def is_leaf(n):
    return isinstance(n, int)

def is_pair(n):
    return isinstance(n, list)

def child_idx(parent, child):
    return 0 if child is parent[0] else 1

 # moves value x from node u in direction d
 # (similar to finding pred/succ in a BST)
def move_incr(u, path, d, x):
    for p in reversed(path):
        if u is p[d]:
            u = p
        else:
            r = d^1
            if is_pair(p[d]):
                u = p[d]
                while is_pair(u[r]):
                    u = u[r]
                u[r] += x
            else:
                p[d] += x
            break

def explode(n, path):
    move_incr(n, path, 0, n[0])
    move_incr(n, path, 1, n[1])
    path[-1][child_idx(path[-1], n)] = 0

def split(n, parent):
    m = n//2
    parent[child_idx(parent, n)] = [m, n-m]

def reduce_explode(n, path):
    if is_pair(n):
        if len(path)>=4 and is_leaf(n[0]) and is_leaf(n[1]):
            explode(n, path)
            return True
        path.append(n)
        if reduce_explode(n[0], path) or reduce_explode(n[1], path):
            return True
        path.pop()
    return False

def reduce_split(n, parent=None):
    if is_pair(n):
        if reduce_split(n[0], n) or reduce_split(n[1], n):
            return True
    elif n>=10:
        split(n, parent)
        return True
    return False

def reduce(n):
    while reduce_explode(n, []) or reduce_split(n):
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
s = I[0]
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
