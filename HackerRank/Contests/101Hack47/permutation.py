#!/usr/bin/env python3

def test(S):
    Seen = set()
    for s in S:
        if s in Seen:
            return False
        Seen.add(s)
    return True

def main():
    m = int(input())
    S = list(map(int,input().split()))
    print('YES' if test(S) else 'NO')

main()
