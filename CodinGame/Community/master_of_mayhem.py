#!/usr/bin/env python3

import re

REport = lambda: re.fullmatch(r'(.+)\'s (\w+) is (?:a |an |")(.+?)"?', input()).groups()

Cyb = {input() for _ in range(int(input()))}
May = {}
for _ in range(int(input())):
    _,a,v = REport()
    May[a] = v
for _ in range(int(input())):
    name,a,v = REport()
    if a=='catchphrase':
        if 'word' in May and May['word'] not in v:
            Cyb.discard(name)
    elif a in May and May[a]!=v:
        Cyb.discard(name)
print('MISSING' if len(Cyb)==0 else Cyb.pop() if len(Cyb)==1 else 'INDETERMINATE')
