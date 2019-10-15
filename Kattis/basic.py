#!/usr/bin/env python3

import re

def parse_int(I):
    re_base = lambda b: '^[%s]+$' % '0123456789abcdef'[:b]
    M = re.match(r'^([0-9a-f#]+)#([0-9a-f]+)#$', I)
    if M:
        base = parse_int(M.group(1))
        J = M.group(2)
        if base is not None and 2<=base<=16 and re.match(re_base(base), J):
            return int(J, base)
    elif re.match(re_base(10), I):
        return int(I)
    return None

def main():
    N = int(input())
    for _ in range(N):
        I = input()
        print('no' if parse_int(I) is None else 'yes')

main()
