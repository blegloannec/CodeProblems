#!/usr/bin/env python3

# on ne verifie pas que les 0 et 1 sont en alternance (message
# "compresse") et apparemment ce n'est pas necessaire...

def decode(M):
    if len(M)%2!=0:
        return 'INVALID'
    D = []
    for i in range(0,len(M),2):
        if M[i]>2:
            return 'INVALID'
        b = 2-M[i]
        for _ in range(M[i+1]):
            D.append(b)
    if len(D)%7!=0:
        return 'INVALID'
    R = []
    for i in range(0,len(D),7):
        c = 0
        for j in range(7):
            c |= D[i+j]<<(6-j)
        R.append(chr(c))
    return ''.join(R)

print(decode(list(map(len,input().split()))))
