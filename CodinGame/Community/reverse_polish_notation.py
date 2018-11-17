#!/usr/bin/env python3

from operator import *

OP = {'ADD':add, 'SUB':sub, 'MUL':mul, 'DIV':floordiv, 'MOD':mod}

def simu(P):
    S = []
    try:
        for I in P:
            if I in OP:
                b,a = S.pop(),S.pop()
                S.append(OP[I](a,b))
            elif I=='POP':
                S.pop()
            elif I=='DUP':
                S.append(S[-1])
            elif I=='SWP':
                S[-1],S[-2] = S[-2],S[-1]
            elif I=='ROL':
                S.pop()
                S[-3],S[-2],S[-1] = S[-2],S[-1],S[-3]
            else:
                S.append(int(I))
    except:
        S.append('ERROR')
    return S

N = int(input())
print(*simu(input().split()))
