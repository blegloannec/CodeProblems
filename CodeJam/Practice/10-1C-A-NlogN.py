#!/usr/bin/env python

import sys

# compte les inversions d'une permutation
def inversions(A):
    return merge_sort_inv(A,0,len(A)-1)[0]

def merge_sort_inv(A,i,j):
    if j-i<=0:
        return (0,A[i:j+1])
    m = (i+j)/2
    n1,B1 = merge_sort_inv(A,i,m)
    n2,B2 = merge_sort_inv(A,m+1,j)
    B = []
    i1,i2 = 0,0
    inv = n1+n2
    for _ in xrange(j-i+1):
        if i1<len(B1) and (i2>=len(B2) or B1[i1]<=B2[i2]):
            B.append(B1[i1])
            i1 += 1
        else:
            B.append(B2[i2])
            i2 += 1
            # inversions avec tout le reste de B1
            inv += len(B1)-i1
    return (inv,B)

def main():
    T = int(sys.stdin.readline())
    for t in xrange(1,T+1):
        N = int(sys.stdin.readline())
        P = []
        for _ in xrange(N):
            a,b = map(int,sys.stdin.readline().split())
            P.append((a,b))
        P.sort() # tri selon a
        Q = map((lambda x: x[1]),P) # on garde les b
        print 'Case #%d: %d' % (t,inversions(Q))

main()
