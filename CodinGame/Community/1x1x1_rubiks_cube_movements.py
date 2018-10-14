#!/usr/bin/env python3

# yet another problem that is so "simplified" that it
# has no relation with it's title...

#    U5
# L4 F0 R1
#    D2
#    B3

Num = {'F':0,'R':1,'D':2,'B':3,'L':4,'U':5}
Face = 'FRDBLU'

def compose(A,B):
    return [A[B[i]] for i in range(6)]

R = {"x'": [2,1,3,5,4,0],
     "y'": [1,3,2,4,0,5],
     "z'": [0,5,1,3,2,4]}
for d in ["x'","y'","z'"]:
    R[d[0]] = compose(R[d],compose(R[d],R[d]))

def main():
    S = input().split()
    P = list(range(6))
    for r in S:
        P = compose(R[r],P)
    for _ in range(2):
        print(Face[P[Num[input()]]])

main()
