#!/usr/bin/env python3

# pb 10040 on UVa, 2201 on Archive

# Duval's algorithm (1988) to generate Lyndon words of size <=n in lex order
# https://en.wikipedia.org/wiki/Lyndon_word
def lyndon(n):
    w = [0]*n
    l = 1
    yield '0'
    while True:
        for i in range(l,n):
            w[i] = w[i%l]
        l = n
        while l>0 and w[l-1]==1:
            l -= 1
        if l==0:
            break
        w[l-1] = 1
        yield ''.join(map(str,w[:l]))

# the lex-min De Bruijn cycle of order n is the concatenation of lex-ordered
# Lyndon words of size <=n whose size divides n
# https://oeis.org/A166315
# we modify the previous algorithm to efficiently generate that cycle
def lyndon_de_bruijn(n):
    w = [0]*n
    l = 1
    db = [0]    
    while True:
        for i in range(l,n):
            w[i] = w[i%l]
        l = n
        while l>0 and w[l-1]==1:
            l -= 1
        if l==0:
            break
        w[l-1] = 1
        if n%l==0:
            db += w[:l]
    return db

def main():
    DB = [lyndon_de_bruijn(n) for n in range(22)]
    T = int(input())
    for _ in range(T):
        n,k = map(int,input().split())
        res = 0
        for i in range(k,k+n):
            res = (res<<1) | DB[n][i%len(DB[n])]
        print(res)

main()
