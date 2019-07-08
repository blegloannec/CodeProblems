#!/usr/bin/env python3

T = ('prime','second','third','fourth','fifth','sixth','seventh','octave')
Q = (('diminished','minor','major','augmented'), ('diminished','perfect','augmented'))
F = (0,2,3,5,7,8,10,12)
Pitch = lambda A: ord(A[0])-ord('A')
Alter = lambda A: 0 if len(A)==1 else 1 if A[1]=='+' else -1
Ref = ((None,    2,    1, None, None,    1,    1, None),
       (   1, None, None,    1,    1, None, None,    1))

def interval(A, B):
    pa, pb = Pitch(A), Pitch(B)
    fa, fb = F[pa]+Alter(A), F[pb]+Alter(B)
    if fa>=fb:
        pb += 7
        fb += 12
    t = pb-pa
    qc = 0 if Ref[0][t] is not None else 1
    q = Ref[qc][t] + fb-fa-F[t]
    return '{} {}'.format(Q[qc][q],T[t])

if __name__=='__main__':
    N = int(input())
    for _ in range(N):
        A,B = input().split()
        print(interval(A,B))
