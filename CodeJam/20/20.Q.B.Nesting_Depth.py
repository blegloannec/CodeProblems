#!/usr/bin/env python3

def main():
    T = int(input())
    for t in range(1,T+1):
        S = input() + '0'
        O = []
        o = 0
        for c in S:
            n = ord(c)-ord('0')
            if o>n:
                O.append(')'*(o-n))
            elif o<n:
                O.append('('*(n-o))
            o = n
            O.append(c)
        O.pop()
        O = ''.join(O)
        print('Case #{}: {}'.format(t,O))

main()
