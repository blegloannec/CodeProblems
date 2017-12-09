#!/usr/bin/env python3

I = input()

def parse(I):
    L = G = score = 0
    garbage = escape = False
    for c in I:
        if escape:
            escape = False
        elif garbage:
            if c=='>':
                garbage = False
            elif c=='!':
                escape = True
            else:
                G += 1
        elif c=='<':
            garbage = True
        elif c=='{':
            L += 1
        elif c=='}':
            score += L
            L -= 1
    return score,G

print(*parse(I))  # Part 1 & 2
