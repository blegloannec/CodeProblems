#!/usr/bin/env python3

S = 5
class Permutation:
    def __init__(self, C=None):
        if isinstance(C, list):
            assert len(C)==S
            self.P = C
        else:
            self.P = list(range(S))
            if isinstance(C, tuple):
                for i in range(len(C)):
                    self.P[C[i]] = C[(i+1)%len(C)]

    def __getitem__(self, i):
        return self.P[i]

    def __mul__(self, A):
        res = [0]*S
        for i in range(S):
            res[i] = self[A[i]]
        return Permutation(res)

    def decomp(self):
        C = []
        Seen = [False]*S
        for i in range(S):
            if not Seen[i]:
                Seen[i] = True
                c = [i]
                j = self[i]
                while j!=i:
                    Seen[j] = True
                    c.append(j)
                    j = self[j]
                if len(c)>1:
                    C.append(tuple(c))
        return C


def main():
    I = input()[1:-1].split(')(')
    I = [Permutation(tuple(int(i)-1 for i in c.split())) for c in I if c]
    P = Permutation()
    for Q in I:
        P *= Q
    C = P.decomp()
    print(''.join(f'({" ".join(str(i+1) for i in c)})' for c in C) if C else '()')

main()
