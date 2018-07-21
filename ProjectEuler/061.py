#!/usr/bin/env python

from collections import defaultdict

Nums = [[n*(n+1)/2 for n in range(45,141)],
        [n*n for n in range(32,100)],
        [n*(3*n-1)/2 for n in range(26,82)],
        [n*(2*n-1) for n in range(23,71)],
        [n*(5*n-3)/2 for n in range(21,64)],
        [n*(3*n-2) for n in range(19,59)]]

def split(n):
    return (n/100,n%100)

# recursive generator using Heap's algo, quite ugly
# better in python 3: syntax "yield from <recursive call>"
def heap(n,A):
    if n==1:
        yield A
    else:
        for i in xrange(n-1):
            for B in heap(n-1,A):
                yield B
            if n%2==0:
                A[i],A[n-1] = A[n-1],A[i]
            else:
                A[0],A[n-1] = A[n-1],A[0]
        for B in heap(n-1,A):
            yield B
         
def main():
    global Nums
    Nums = map((lambda l: map(split,l)), Nums)
    Nums2 = [defaultdict(list) for _ in xrange(6)]
    for i in xrange(1,6):
        for x,y in Nums[i]:
            Nums2[i][x].append(y)
    for i in xrange(len(Nums[0])):
        a0,a1 = Nums[0][i]
        for P in heap(5,range(1,6)):
            for b1 in Nums2[P[0]][a1]:
                for c1 in Nums2[P[1]][b1]:
                    for d1 in Nums2[P[2]][c1]:
                        for e1 in Nums2[P[3]][d1]:
                            for f1 in Nums2[P[4]][e1]:
                                if f1==a0:
                                    print 101*(a0+a1+b1+c1+d1+e1)
                                    return

main()
