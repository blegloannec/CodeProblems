#!/usr/bin/env python3

ROW = '87654321'
COL = 'abcdefgh'

O = 'KQRBN'
compW = lambda w: ((5 if len(w)==2 else O.index(w[0])), int(w[-1]), w[-2])
compB = lambda w: ((5 if len(w)==2 else O.index(w[0])),-int(w[-1]), w[-2])

def main():
    G = [input()[2::4] for _ in range(16)][1::2]
    W = []
    B = []
    for i,L in enumerate(G):
        for j,p in enumerate(L):
            if   'A'<=p<='Z':
                W.append(('' if p=='P' else p) + COL[j] + ROW[i])
            elif 'a'<=p<='z':
                B.append(('' if p=='p' else p.upper()) + COL[j] + ROW[i])
    W.sort(key=compW)
    B.sort(key=compB)
    print('White:', ','.join(W))
    print('Black:', ','.join(B))

main()
