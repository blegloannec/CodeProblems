#!/usr/bin/env python3

import sys

def expr_eval(Prio, Expr):
    Val = []
    Op = []
    for x in Expr:
        if x=='(':
            Op.append(x)
        elif x in Prio:
            while Op and Prio[Op[-1]]>=Prio[x]:
                o = Op.pop()
                a = Val.pop()
                b = Val.pop()
                Val.append(a+b if o=='+' else a*b)
            if x==')': Op.pop()  # '('
            else:      Op.append(x)
        else:
            Val.append(int(x))
    return Val[0]

Prio1 = {'(': 1, ')': 2, '+': 3, '*': 3}
Prio2 = {'(': 1, ')': 2, '+': 4, '*': 3}

part1 = part2 = 0
for L in sys.stdin.readlines():
    E = ['('] + L.replace('(','( ').replace(')',' )').split() + [')']
    part1 += expr_eval(Prio1, E)
    part2 += expr_eval(Prio2, E)
print(part1)
print(part2)
