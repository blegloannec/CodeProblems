#!/usr/bin/env python3

from math import gcd

lcm = lambda a,b: a*b//gcd(a,b)

photobooth = lambda w,h: lambda x,y: (x//2+(x%2)*(w//2), y//2+(y%2)*(h//2))

# period of a permutation = LCM of the sizes of its cycles
def permutation_period(P):
    per = 1
    Seen = [False]*len(P)
    for i in range(len(P)):
        if not Seen[i]:
            c = 0
            while not Seen[i]:
                Seen[i] = True
                c += 1
                i = P[i]
            per = lcm(per,c)
    return per

# O(w*h) approach (expected)
def solution2d(w,h):
    F = photobooth(w,h)
    idx = lambda x,y: x*h+y
    P = [idx(*F(*divmod(i,h))) for i in range(w*h)]
    return permutation_period(P)

# O(w+h) approach noticing both dimensions are independent
def solution1d(w,h):
    F = photobooth(w,h)
    Px = [F(x,0)[0] for x in range(w)]
    Py = [F(0,y)[1] for y in range(h)]
    return lcm(permutation_period(Px), permutation_period(Py))

# There is also a "formula" for the period of the 1d-permutations
# (period on one dimension w = multiplicative order of 2 mod w-1)
# - ad-hoc proof (in French):
#   https://fr.wikipedia.org/wiki/Transformation_du_clich%C3%A9_Photomaton
# - or notice the 1d-perm. is the inverse of a classic cards "faro shuffle":
#   https://en.wikipedia.org/wiki/Faro_shuffle
def solution_formula(w,h):
    l = 1
    for d in (w-1, h-1):
        if d>1:
            # multiplicative order of 2 mod d (odd), computed "naively"
            k, p = 2, 1
            while k!=1:
                k = (2*k)%d
                p += 1
            l = lcm(l,p)
    return l

def main():
    T = int(input())
    for _ in range(T):
        w,h = map(int,input().split())
        print(solution2d(w,h))
        #print(solution1d(w,h))
        #print(solution_formula(w,h))

main()
