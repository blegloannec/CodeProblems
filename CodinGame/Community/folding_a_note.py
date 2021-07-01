#!/usr/bin/env python3

import numpy as np

N = int(input())
A = np.array([[[c] for c in input()] for _ in range(N)])
while N>1:
    N >>= 1
    A = np.concatenate((A[:,:N-1:-1,::-1], A[:,:N,:]), axis=2)
    A = np.concatenate((A[:N-1:-1,:,::-1], A[:N,:,:]), axis=2)
    if N>1:
        N >>= 1
        A = np.concatenate((A[:,N-1::-1,::-1], A[:,N:,:]), axis=2)
        A = np.concatenate((A[N-1::-1,:,::-1], A[N:,:,:]), axis=2)
print(''.join(A[0,0]))
