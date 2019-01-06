#!/usr/bin/env python3

AlphaChr = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
AlphaOrd = {a:i for i,a in enumerate(AlphaChr)}

B = 53  # prime

# modular inverse
def inv(x):
    return pow(x,B-2,B)

# modular Lagrange interpolation
def lagrange(Pts, x=0):
    y = 0
    for xi,yi in Pts:
        pi = yi
        for xj,_ in Pts:
            if xj!=xi:
                pi = (pi*(x-xj)*inv(xi-xj)) % B
        y = (y+pi) % B
    return y

def reveal(Parts):
    Secret = []
    for i in range(len(Parts[0][1])):
        Pts = [(x,AlphaOrd[s[i]]) for x,s in Parts]
        Secret.append(AlphaChr[lagrange(Pts)])
    return ''.join(Secret)

if __name__=='__main__':
    N = int(input())
    Parts = []
    for _ in range(N):
        a,s = input().split()
        a = int(a)
        Parts.append((a,s))
    print(reveal(Parts))
