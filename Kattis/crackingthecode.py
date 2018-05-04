#!/usr/bin/env python3

A = ord('a')
def num(c):
    return ord(c)-A

def match(M,D,C):
    if len(M)!=len(D):
        return False
    U = [False]*26
    for i in range(len(M)):
        c,d = num(M[i]),num(D[i])
        if C[c]==None:
            if U[d]:
                return False
            C[c] = d
            U[d] = True
        elif C[c]!=d:
            return False
    return True

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        M = [input() for _ in range(n)]
        D = input()
        X = input()
        # looking for acceptable matchings
        PC = []
        for m in M:
            C = [None]*26
            if match(m,D,C):
                PC.append(C)
        if len(PC)==0:
            print('IMPOSSIBLE')
        else:
            # "intersecting" acceptable matchings
            IC = [None]*26
            for i in range(26):
                if all(PC[0][i]==PC[k][i] for k in range(1,len(PC))):
                    IC[i] = PC[0][i]
            # TRICKY corner case: only one letter missing in IC ~> completing
            Ui = [i for i in range(26) if IC[i]==None]
            if len(Ui)==1:
                IC[Ui[0]] = sum(range(26))-sum(IC[i] for i in range(26) if IC[i]!=None)
            # decrypting
            Y = ['?']*len(X)
            for i in range(len(X)):
                d = IC[num(X[i])]
                if d!=None:
                    Y[i] = chr(d+A)
            Y = ''.join(Y)
            print(Y)

main()
