#!/usr/bin/env python3

import sys, re
from collections import Counter

Forb = {"and", "array", "echo", "else", "elseif", "if", "for", "foreach", "function", "or", "return", "while"}

S = sys.stdin.read()
S = re.sub(r'//.*?\n', '', S)
S = re.sub(r'/\*.*?\*/', '', S, flags=re.DOTALL)
S = re.sub(r'(["\']).*?\1', '', S, flags=re.DOTALL)

Excl = set(mo.group(2) for mo in re.finditer(r'(function|new)\s+([\w_]+)\(', S))
Cnt = Counter(mo.group(1) for mo in re.finditer(r'(?<!\$)([\w_]+)\(', S)  \
              if mo.group(1).lower() not in Forb                          \
              and mo.group(1) not in Excl)
if Cnt:
    for it in sorted(Cnt.items()):
        print(*it)
else:
    print('NONE')
