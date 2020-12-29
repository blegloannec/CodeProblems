#!/usr/bin/env python3

import sys
input = sys.stdin.readline
from operator import eq, and_, or_

OP = {'K': and_, 'A': or_, 'C': (lambda p,q: (not p) or q), 'E': eq}

# evaluate a polish notation boolean formula
def evaluate(Form, Vars, ValMask):
    S = []
    # reverse polish is slightly simpler to evaluate than polish
    # (operators are evaluated right away, no need to wait for
    #  their arity be reached in the number of pushed values)
    # so we do it from right to left
    for c in reversed(Form):
        if c=='N':
            S.append(not S.pop())
        elif c in OP:
            p = S.pop()
            q = S.pop()
            S.append(OP[c](q,p))
        else:
            #assert c in Vars
            i = Vars.index(c)
            S.append(((ValMask>>i)&1) == 1)
    #assert len(S)==1
    return S[0]

def main():
    while True:
        L = input().strip()
        if L=='0':
            break
        Vars = ''.join(set(c for c in L if c.islower()))
        tauto = all(evaluate(L, Vars, Val) for Val in range(1<<len(Vars)))
        sys.stdout.write('tautology\n' if tauto else 'not\n')

main()
