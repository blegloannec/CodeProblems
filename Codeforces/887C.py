#!/usr/bin/env python3

# RECYCLAGE (cf. PE 599)
#       |20 21|
#       |23 22|
#       -------
#       |16 17|
#       |19 18|
# -------------------
# |12 13| 0  1| 4  5|
# |15 14| 3  2| 7  6|
# -------------------
#       | 8  9|
#       |11 10|

S = 24
class Permutation:
    def __init__(self,C=None):
        if isinstance(C,list):
            assert(len(C)==S)
            self.P = C
        else:
            self.P = list(range(S))
            if isinstance(C,tuple):
                for i in range(len(C)):
                    self.P[C[i]] = C[(i+1)%len(C)]
        self.P = tuple(self.P)

    def __getitem__(self,i):
        return self.P[i]
        
    def __mul__(self,A):
        res = [0]*S
        for i in range(S):
            res[i] = self[A[i]]
        return Permutation(res)

    def __hash__(self):
        return hash(self.P)

    def __eq__(self,A):
        return self.P==A.P

    def decomp(self):
        D = []
        seen = [False]*S
        for i0 in range(S):
            if not seen[i0]:
                seen[i0] = True
                C = [i0]
                i = self[i0]
                while i!=i0:
                    seen[i] = True
                    C.append(i)
                    i = self[i]
                D.append(C)
        return D

Gen = []
# rotation de la face centrale du patron
# 0 -> 1 -> 2 -> 3 -> 0
# 4 -> 9 -> 14 -> 19 -> 4
# 7 -> 8 -> 13 -> 18 -> 7
Gen.append(Permutation((0,1,2,3))*Permutation((4,9,14,19))*Permutation((7,8,13,18)))

# (4,5,6,7)(1,17,21,9)(2,18,22,10)
Gen.append(Permutation((4,5,6,7))*Permutation((1,17,21,9))*Permutation((2,18,22,10)))

# (8,9,10,11)(15,3,7,21)(14,2,6,20)
Gen.append(Permutation((8,9,10,11))*Permutation((15,3,7,21))*Permutation((14,2,6,20)))

# (12,13,14,15)(20,16,0,8)(23,19,3,11)
Gen.append(Permutation((12,13,14,15))*Permutation((20,16,0,8))*Permutation((23,19,3,11)))

# (16,17,18,19)(13,23,5,1)(12,22,4,0)
Gen.append(Permutation((16,17,18,19))*Permutation((13,23,5,1))*Permutation((12,22,4,0)))

# (20,21,22,23)(12,11,6,17)(15,10,5,16)
Gen.append(Permutation((20,21,22,23))*Permutation((12,11,6,17))*Permutation((15,10,5,16)))

def solved(C,P):
    for i in range(0,24,4):
        if any(C[P[i+k]]!=C[P[i]] for k in range(1,4)):
            return False
    return True

def main():
    C = list(map(int,input().split()))
    # re-numerotation
    R = Permutation([5,7,6,4,9,11,10,8,13,15,14,12,1,3,2,0,17,19,18,16,21,23,22,20])
    for i in range(len(Gen)):  # rotations inverses
        Gen.append(Gen[i]*Gen[i]*Gen[i])
    print('YES' if any(solved(C,R*g) for g in Gen) else 'NO')

main()
