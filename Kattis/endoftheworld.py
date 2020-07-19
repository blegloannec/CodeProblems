#!/usr/bin/env python3

def hanoi_idx(n, a=0, b=1):
    if n<0:
        return 0
    p = S[n]
    c = 3-a-b
    assert p!=c
    if p==a:
        # nth disk still in a
        # so we're still moving (n-1)th tower from a to c
        return hanoi_idx(n-1, a, c)
    else:
        # nth disk in b
        # so (n-1)th has already been moved from a to c
        # and we're currently moving it from c to b
        return (1<<n) + hanoi_idx(n-1, c, b)

def main():
    global S
    while True:
        S = input()
        if S=='X':
            break
        S = [ord(c)-ord('A') for c in S]
        res = (1<<len(S))-1 - hanoi_idx(len(S)-1)
        print(res)

main()
