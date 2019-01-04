#!/usr/bin/env python3

# http://oeis.org/A054639

def queneau_perm(N):
    P = []
    a,b = N-1,0
    while a>b:
        P += [a,b]
        a -= 1
        b += 1
    if a==b:
        P.append(a)
    return P

def perm(P,X):
    return [X[P[i]] for i in range(len(X))]

def main():
    N = int(input())
    Q = queneau_perm(N) 
    A = list(range(1,N+1))
    A0 = A[:]
    L = []
    for _ in range(N):
        A = perm(Q,A)
        L.append(A)
        # Actually the problem is WRONG:
        # while the statement says "exactly N iterations"
        # the answers only expect N to be a multiple of the order
        #if A==A0:
        #    break
    if len(L)==N and A==A0:
        for X in L:
            print(','.join(map(str,X)))
    else:
        print('IMPOSSIBLE')

main()
