#!/usr/bin/env python3

def main():
    T = int(input())
    for _ in range(T):
        s = input()
        a = b = p = 0
        last = None
        for c in s:
            if c=='.':
                p += 1
            else:
                if c=='A':
                    a += 1 + (p if c==last else 0)
                else:
                    b += 1 + (p if c==last else 0)
                last = c
                p = 0
        print(a,b)

main()
