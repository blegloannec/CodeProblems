#!/usr/bin/env python3

from operator import *

OP = {'ADD':add, 'SUB':sub, 'MUL':mul, 'DIV':floordiv, 'MOD':mod}

def run(Func, S, fname='_MAIN_'):
    Prog = Func[fname]
    i = 0
    while i<len(Prog):
        I = Prog[i]
        if isinstance(I, int):
            S.append(I)
        elif isinstance(I, tuple):         # IF / ELS
            if I[0]=='ELS' or S.pop()==0:  # jump case
                i = I[1]
                continue
        elif I in OP:
            b,a = S.pop(),S.pop()
            S.append(OP[I](a,b))
        elif I=='POP':
            S.pop()
        elif I=='DUP':
            S.append(S[-1])
        elif I=='SWP':
            S[-1],S[-2] = S[-2],S[-1]
        elif I=='ROT':
            S[-3],S[-2],S[-1] = S[-2],S[-1],S[-3]
        elif I=='OVR':
            S.append(S[-2])
        elif I=='POS':
            S.append(int(S.pop()>=0))
        elif I=='NOT':
            S.append(int(S.pop()==0))
        elif I=='OUT':
            print(S.pop())
        else:
            assert I in Func
            run(Func, S, I)
        i += 1

def parse_func(Prog, Func, i=0):
    assert Prog[i]=='DEF'
    fname = Prog[i+1]
    i += 2
    Body = []
    Cond = []
    while Prog[i]!='END':
        I = Prog[i]
        if I=='DEF':
            i = parse_func(Prog, Func, i)
            continue
        elif I=='IF':
            Cond.append(len(Body))
        elif I=='ELS':
            Cond.append(len(Body))
        elif I=='FI':
            ifi = Cond.pop()
            if Body[ifi]=='ELS':
                ifi, eli = Cond.pop(), ifi
                Body[ifi] = ('IF', eli+1)
                Body[eli] = ('ELS', len(Body))
            else:
                Body[ifi] = ('IF', len(Body))
            i += 1
            continue  # we do not keep the FI token
        else:
            try:
                I = int(I)
            except ValueError:
                pass
        Body.append(I)
        i += 1
    assert fname not in Func
    Func[fname] = Body
    return i+1

def main():
    N = int(input())
    Prog = ['DEF', '_MAIN_']
    for _ in range(N):
        Prog += input().split()
    Prog.append('END')
    Func = {}
    parse_func(Prog, Func)
    run(Func, [])

main()
