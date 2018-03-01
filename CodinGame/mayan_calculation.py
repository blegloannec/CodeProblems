#!/usr/bin/env python3

from operator import add,sub,mul,floordiv

B = 20
O = {'+':add, '-':sub, '*':mul, '/':floordiv}

def read_digits():
    global L,H,R,D
    L,H = map(int,input().split())
    I = [input() for _ in range(H)]
    R = []
    D = {}
    for i in range(B):
        d = '\n'.join(I[j][i*L:(i+1)*L] for j in range(H))
        R.append(d)
        D[d] = i

def read_mayan():
    s = int(input())
    x = 0
    for _ in range(s//H):
        d = '\n'.join(input() for _ in range(H))
        x = B*x+D[d]
    return x

def print_mayan(n):
    n,d = divmod(n,B)
    S = [R[d]]
    while n:
        n,d = divmod(n,B)
        S.append(R[d])
    print('\n'.join(reversed(S)))

def main():
    read_digits()
    x = read_mayan()
    y = read_mayan()
    o = input()
    print_mayan(O[o](x,y))

main()
