#!/usr/bin/env python3

a = ord('a')
num = lambda c: ord(c)-a
let = lambda i: chr(i+a)

def main():
    k,l = map(int,input().split())
    M = [num(c) for c in reversed(input())]
    C = [num(c) for c in reversed(input())]
    for i in range(l):
        M.append((C[i]-M[i])%26)
    M = ''.join(let(i) for i in reversed(M))
    K,M = M[:k],M[k:]
    print(M)

main()
