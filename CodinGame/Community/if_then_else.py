#!/usr/bin/env python3

N = int(input())
Stk = [0, '(']
for _ in range(N):
    line = input()
    if line == 'if':
        Stk.append('(')
    elif line[0] == 'e':
        c = 1
        while Stk[-1] != '(':
            c *= Stk[-1]
            Stk.pop()
        Stk.pop()  # '('
        if line == 'else':
            Stk += (c, '(')
        else:  # end(if)?
            Stk.append(c + Stk.pop())
print(Stk.pop())
