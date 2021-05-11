#!/usr/bin/env python3

import sys, re

def validate(code):
    L = '({['
    R = ')}]'
    B = []
    b = False
    for c in code:
        if c in R:
            if B and B[-1]==L[R.index(c)]:
                B.pop()
            else:
                return 'Invalid'
        elif c in L:
            B.append(c)
            b = True
    return 'Invalid' if B else 'Valid' if b else 'No brackets'

code = sys.stdin.read().replace(r'\\', '').replace(r'\"','')
code = re.sub(r'".*?"', '', code)
print(validate(code))
