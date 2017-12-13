#!/usr/bin/env python3

H = ['+--+   +--+   +--+   +--+   +--+   +--+   +--+ ',
     '|      |  o   |  o   |  o   |  o   |  o   |  o ',
     '|      |      |  |   | /|   | /|\  | /|\  | /|\\',
     '|\     |\     |\     |\     |\     |\/    |\/ \\']

def hangman(e):
    for j in range(4):
        print(H[j][7*e:7*e+5].strip())

w = input()
ws = set(c.lower() for c in w)
L = input().split()

e = 0
found = set()
if ' ' in ws:
    found.add(' ')
for c in L:
    if c in ws and c not in found:
        found.add(c)
    else:
        e += 1
        if e==6:
            break
hangman(e)
print(''.join(c if c.lower() in found else '_' for c in w))
