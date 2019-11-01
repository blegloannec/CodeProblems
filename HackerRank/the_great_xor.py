#!/usr/bin/env python3

# X = *****0**** for any 0 of X
# A = 000001**** change 0 to 1 and set the remaining left part to whatever

Q = int(input())
for _ in range(Q):
    X = int(input())
    print((1<<(X.bit_length()))-1 - X)
