#!/usr/bin/env python3

I = input()

# Part 1
D = ord('a')-ord('A')
def react(I):
    P = []
    for c in I:
        if P and abs(ord(c)-ord(P[-1]))==D:
            P.pop()
        else:
            P.append(c)
    return len(P)

print(react(I))


# Part 2
print(min(react(I.replace(chr(ord('A')+c),'').replace(chr(ord('a')+c),'')) for c in range(26)))
