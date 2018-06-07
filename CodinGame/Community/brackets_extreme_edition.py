#!/usr/bin/env python3

def valid(E):
    D = {')':'(',']':'[','}':'{'}
    S = []
    for c in E:
        if c in ['(','[','{']:
            S.append(c)
        elif c in D:
            if len(S)==0 or S[-1]!=D[c]:
                return False
            S.pop()
    return len(S)==0

print(str(valid(input())).lower())
