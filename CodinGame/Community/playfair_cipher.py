#!/usr/bin/env python3

class Playfair:
    def __init__(self, key_table):
        self.KT = key_table
        self.CP = {}
        for i in range(5):
            for j in range(5):
                self.CP[self.KT[i][j]] = (i,j)

    def str_form(self, S):
        S = S.upper()
        S = ''.join(c for c in S if c in self.CP)
        return S

    def encrypt(self, S):
        S = self.str_form(S)
        if len(S)%2!=0:
            return None
        C = []
        for i in range(0,len(S),2):
            i1,j1 = self.CP[S[i]]
            i2,j2 = self.CP[S[i+1]]
            if i1!=i2 and j1!=j2:
                C.append(self.KT[i1][j2]+self.KT[i2][j1])
            elif i1==i2:
                C.append(self.KT[i1][(j1+1)%5]+self.KT[i2][(j2+1)%5])
            else:  # j1==j2
                C.append(self.KT[(i1+1)%5][j1]+self.KT[(i2+1)%5][j2])
        return ''.join(C)

    def decrypt(self, S):
        S = self.str_form(S)
        if len(S)%2!=0:
            return None
        C = []
        for i in range(0,len(S),2):
            i1,j1 = self.CP[S[i]]
            i2,j2 = self.CP[S[i+1]]
            if i1!=i2 and j1!=j2:
                C.append(self.KT[i1][j2]+self.KT[i2][j1])
            elif i1==i2:
                C.append(self.KT[i1][(j1-1)%5]+self.KT[i2][(j2-1)%5])
            else:  # j1==j2
                C.append(self.KT[(i1-1)%5][j1]+self.KT[(i2-1)%5][j2])
        return ''.join(C)

def main():
    KT = [input().split() for _ in range(5)]
    P = Playfair(KT)
    A = input()
    N = int(input())
    for _ in range(N):
        M = input()
        M = P.encrypt(M) if A[0]=='E' else P.decrypt(M)
        print('DUD' if M is None else M)

main()
