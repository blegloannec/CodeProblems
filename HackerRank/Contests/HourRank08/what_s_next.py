#!/usr/bin/env python

import sys

# The next integer B we are looking for is actually the next permutation
# of A (as a bit string) in the lex order if A is not maximal.
# Case 1 (particular): A is lex-max, ie is decreasing, ie of the form:
# 11..1 (n=1) or 1..10..0 (n=2)
# then B requires 1 more bit (to 0) and is of the form:
# 101..1 = {1,1,A[0]-1} or 10..01..1 = {1,A[1]+1,A[0]-1}
# (the first case is covered by the second considering A[1]=0)
# Case 2 (general): A is not lex-max, n>=3 and is of the form
# ..0..01..1 = {..,A[-2],A[-1]}  (n odd)
# or ..0..01..10..0 = {..,A[-3],A[-2],A[-1]}  (n even)
# then B is of the form
# 0..0101..1 = {..,A[-2]-1,1,1,A[-1]-1}
# or 0..010..01..1 = {..,A[-3]-1,1,A[-1]+1,A[-2]-1}
# (the first case is covered by the second considering A[-1]=0)

def main():
    T = int(sys.stdin.readline())
    for t in xrange(T):
        n = int(sys.stdin.readline())
        A = map(int,sys.stdin.readline().split())
        if n%2==1:
            A.append(0)
        if n<=2:
            B = [1,A[1]+1,A[0]-1]
            if B[-1]==0:
                B.pop()
        else:
            B = A[:]
            if A[-3]>1:
                B.append(0)
                B[-3] = 1
                B[-4] = A[-3]-1
            else:
                B.pop()
                B[-3] += 1
            B[-1] = A[-2]-1
            B[-2] = A[-1]+1
            if B[-1]==0:
                B.pop()
        print len(B)
        print ' '.join(map(str,B))


main()
