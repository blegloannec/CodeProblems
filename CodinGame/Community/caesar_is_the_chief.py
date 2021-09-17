#!/usr/bin/env python3

def main():
    A = ord('A')
    ciph = input().split()
    for k in range(26):
        M = [''.join(chr((ord(c)-A+k)%26+A) for c in w) for w in ciph]
        if 'CHIEF' in M:
            print(*M)
            return
    print('WRONG MESSAGE')

main()
