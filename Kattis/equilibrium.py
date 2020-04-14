#!/usr/bin/env python3

import sys

def eq_tree(E, Ref, i=0, d=0):
    if E[i]!='[':
        n = 0
        while i<len(E) and '0'<=E[i]<='9':
            n = 10*n + ord(E[i])-ord('0')
            i += 1
        ref = n<<d
        Ref[ref] = Ref.get(ref,0) + 1
    else:
        #assert E[i]=='['
        i = eq_tree(E, Ref, i+1, d+1)
        #assert E[i]==','
        i = eq_tree(E, Ref, i+1, d+1)
        #assert E[i]==']'
        i += 1
    return i

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        E = sys.stdin.readline().strip()
        Ref = {}
        eq_tree(E, Ref)
        size = sum(Ref.values())
        max_ref = max(Ref.values())
        print(size - max_ref)

main()
