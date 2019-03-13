#!/usr/bin/env python3

def decode_stream(S):
    count = drive = 0
    Momentum = [1,1]
    for c in S:
        b = ord(c)-ord('0')
        for _ in range(3):
            if b&1:
                count += Momentum[drive]
            Momentum[drive^1] += Momentum[drive]
            drive ^= 1
            b >>= 1
    return count

def tumble(G):
    H,W = len(G),len(G[0])
    C = [sum(int(G[i][j]=='#') for i in range(H)) for j in range(W)]
    C = [sum(int(C[j]>=i) for j in range(W)) for i in range(H,0,-1)]
    W,H = H,W
    return [''.join('#' if C[j]>=i else '.' for j in range(W)) for i in range(H,0,-1)]

if __name__=='__main__':
    W,H = map(int,input().split())
    S = input()
    G = [input() for _ in range(H)]
    t = decode_stream(S)
    # Of course t could be huge and we only need it kinda-modulo-4 (cf. below)
    # hence decode_stream() could be optimized to only manipulate small numbers
    # and return the actually usefull result, yet this is good enough here...
    if t>4:
        t = 4 + t%4
    for _ in range(t):
        G = tumble(G)
    print('\n'.join(G))
