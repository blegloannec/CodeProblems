#!/usr/bin/env python

import sys

# la solution est simplement le nb d'inversions

# compte les inversions d'une permutation
# en O(n log n) par tri fusion modifie
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
    for _ in xrange(T):
        N = int(sys.stdin.readline())
        A = map(int,sys.stdin.readline().split())
        print merge_sort_inv(A,0,N-1)

main()
