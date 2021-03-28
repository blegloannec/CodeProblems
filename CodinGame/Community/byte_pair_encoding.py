#!/usr/bin/env python3

N,M = map(int, input().split())
S = ''.join(input() for _ in range(N))
z = ord('Z')
rules = []
while True:
    Cnt = {}
    i = 0
    while i+1<len(S):
        pair = S[i:i+2]
        c,i0 = Cnt.get(pair, (0,-i))
        Cnt[pair] = (c+1,i0)
        i += 1
        if S[i:i+2]==pair: # skip 'a(aa)'
            i += 1
    pair = max(Cnt.keys(), key=Cnt.get)
    if Cnt[pair][0] == 1:
        break
    l = chr(z)
    S = S.replace(pair, l)
    rules.append(f'{l} = {pair}')
    z -= 1
print(S)
print('\n'.join(rules))
