#!/usr/bin/env python3

import numpy as np

Name = ('O(log n)', 'O(n)', 'O(n log n)', 'O(n^2)', 'O(n^2 log n)', 'O(n^3)', 'O(2^n)', 'O(1)')
Funs = ((lambda n: np.log(n)), (lambda n: n), (lambda n: n * np.log(n)), (lambda n: n**2),
        (lambda n: (n**2) * np.log(n)), (lambda n: n**3))

def main():
    N = int(input())
    XY = np.array([tuple(map(int, input().split())) for _ in range(N)])
    X, Y = XY[:,0], XY[:,1]

    # coeff. of variation (normalized std. dev.), also scipy.stats.variation
    variation = np.std(Y)/np.mean(Y)
    if variation < 0.1:
        print(Name[-1])
    else:
        CC = [np.corrcoef(Y, f(X))[0,1] for f in Funs]
        CC.append(np.corrcoef(np.log(Y), X*np.log(2.))[0,1])
        print(Name[np.argmax(CC)])

main()
