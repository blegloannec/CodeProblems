#!/usr/bin/env python3

def solve(E, R):
    if eval(E)==R:
        return E
    for i in range(len(E)):
        for j in range(i+3, len(E)+1):
            F = E[:i]+'('+E[i:j]+')'+E[j:]
            try:
                if eval(F)==R:
                    return F
            except (SyntaxError, TypeError):
                pass

N = int(input())
for _ in range(N):
    E,R = input().split('=')
    E = solve(E, int(R))
    print(f'{E}={R}')
