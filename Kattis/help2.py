#!/usr/bin/env python3

import sys

is_word = lambda w: w[0]!='<'

def find(Repr, x):
    if x not in Repr:
        return x
    Repr[x] = find(Repr, Repr[x])
    return Repr[x]

def union(Repr, Word, a, b):
    a0 = find(Repr, a)
    b0 = find(Repr, b)
    if a0!=b0:
        Repr[b0] = a0
        if b0 in Word:
            if a0 not in Word:
                Word[a0] = Word[b0]
            elif Word[a0]!=Word[b0]:
                return False
    return True

def match_both(A, B):
    if len(A)!=len(B):
        return '-'
    Repr, Word = {}, {}
    for a,b in zip(A,B):
        a0, b0 = 'A'+a, 'B'+b
        if is_word(a): Word[a0] = a
        if is_word(b): Word[b0] = b
        if not union(Repr, Word, a0, b0):
            return '-'
    return ' '.join(Word.get(find(Repr,'A'+a),'x') for a in A)

def main():
    N = int(sys.stdin.readline())
    for _ in range(N):
        A = sys.stdin.readline().split()
        B = sys.stdin.readline().split()
        sys.stdout.write('%s\n' % match_both(A,B))

main()
