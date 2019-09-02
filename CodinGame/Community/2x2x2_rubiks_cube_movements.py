#!/usr/bin/env python3

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


Col = ["F"]*4+["R"]*4+["D"]*4+["L"]*4+["U"]*4+["B"]*4

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

R = {}
# rotation de la face centrale du patron
# 0 -> 1 -> 2 -> 3 -> 0
# 4 -> 9 -> 14 -> 19 -> 4
# 7 -> 8 -> 13 -> 18 -> 7
R["F'"] = Permutation((0,1,2,3))*Permutation((4,9,14,19))*Permutation((7,8,13,18))
R["F"] = R["F'"]*R["F'"]*R["F'"]

# (4,5,6,7)(1,17,21,9)(2,18,22,10)
R["R'"] = Permutation((4,5,6,7))*Permutation((1,17,21,9))*Permutation((2,18,22,10))
R["R"] = R["R'"]*R["R'"]*R["R'"]

# (8,9,10,11)(15,3,7,21)(14,2,6,20)
R["D'"] = Permutation((8,9,10,11))*Permutation((15,3,7,21))*Permutation((14,2,6,20))
R["D"] = R["D'"]*R["D'"]*R["D'"]

# (12,13,14,15)(20,16,0,8)(23,19,3,11)
R["L'"] = Permutation((12,13,14,15))*Permutation((20,16,0,8))*Permutation((23,19,3,11))
R["L"] = R["L'"]*R["L'"]*R["L'"]

# (16,17,18,19)(13,23,5,1)(12,22,4,0)
R["U'"] = Permutation((16,17,18,19))*Permutation((13,23,5,1))*Permutation((12,22,4,0))
R["U"] = R["U'"]*R["U'"]*R["U'"]

# (20,21,22,23)(12,11,6,17)(15,10,5,16)
R["B'"] = Permutation((20,21,22,23))*Permutation((12,11,6,17))*Permutation((15,10,5,16))
R["B"] = R["B'"]*R["B'"]*R["B'"]

def main():
    P = Permutation()
    M = input()
    N = len(M)
    i = 0
    while i<N:
        m = M[i]
        i += 1
        if m==".":
            continue
        if i<N and M[i]=="'":
            m += "'"
            i += 1
        c = 1
        if i<N and "0"<=M[i]<="9":
            c = int(M[i])
            i += 1
        for _ in range(c):
            P = P*R[m]
    print(Col[P[0]]+Col[P[1]])
    print(Col[P[3]]+Col[P[2]])

main()
