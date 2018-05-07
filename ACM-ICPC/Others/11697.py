#!/usr/bin/env python3

# modified from Kattis/itsasecret

Alpha = 'ABCDEFGHIJKLMNOPRSTUVWXYZ'  # no Q

class Playfair:
    def __init__(self, key):
        K = self.str_form(key) + Alpha
        self.KT = [[0]*5 for _ in range(5)]
        self.CP = {}
        for c in K:
            if c not in self.CP:
                i,j = divmod(len(self.CP),5)
                self.KT[i][j] = c
                self.CP[c] = (i,j)

    def str_form(self, S):
        return S.upper().replace(' ','')
        
    def encrypt(self, S):
        S = self.str_form(S)
        D = []
        i = 0
        while i<len(S):
            if i==len(S)-1 or S[i]==S[i+1]:
                D.append(S[i]+'X')
                i += 1
            else:
                D.append(S[i:i+2])
                i += 2
        C = []
        for d in D:
            i1,j1 = self.CP[d[0]]
            i2,j2 = self.CP[d[1]]
            if i1!=i2 and j1!=j2:
                C.append(self.KT[i1][j2]+self.KT[i2][j1])
            elif i1==i2:
                C.append(self.KT[i1][(j1+1)%5]+self.KT[i2][(j2+1)%5])
            else:  # j1==j2
                C.append(self.KT[(i1+1)%5][j1]+self.KT[(i2+1)%5][j2])
        return ''.join(C)

def main():
    n = int(input())
    for _ in range(n):
        P = Playfair(input())
        print(P.encrypt(input()))

main()
