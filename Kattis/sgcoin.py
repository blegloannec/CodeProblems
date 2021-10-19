#!/usr/bin/env python3

def H(previousHash, transaction, token):
    v = previousHash
    for c in transaction:
        v = (v*31 + ord(c)) % 1000000007
    return (v*7 + token) % 1000000007

def gen_token(previousHash, transaction, targetHash):
    v = previousHash
    for c in transaction:
        v = (v*31 + ord(c)) % 1000000007
    return (targetHash - v*7) % 1000000007

def main():
    h0 = int(input())
    # parameters chosen for sample check (h0 = 140000000)
    s1 = 'charlie-pays-to-eve-9-sg-coins'
    h1 = 930000000
    tok1 = gen_token(h0, s1, h1)
    s2 = 'icpc-sg-2018-at-nus'
    h2 = 730000000
    tok2 = gen_token(h1, s2, h2)
    print(s1, tok1)
    print(s2, tok2)

main()
