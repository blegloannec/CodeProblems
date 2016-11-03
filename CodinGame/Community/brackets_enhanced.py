#!/usr/bin/env python3

P = {'(':0,')':0,'[':1,']':1,'{':3,'}':3,'<':4,'>':4}

n = int(input())
for i in range(n):
    expression = input()
    S = []
    for c in expression:
        if c in P:
            if S and S[-1]==P[c]:
                S.pop()
            else:
                S.append(P[c])
    print('false' if S else 'true')
