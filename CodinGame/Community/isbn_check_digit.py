#!/usr/bin/env python3

def num(c):
    return 10 if c=='X' else int(c)

def valid10(isbn):
    return 'X' not in isbn[:-1] and sum(num(c)*(10-i) for i,c in enumerate(isbn))%11==0

def valid13(isbn):
    return 'X' not in isbn and sum(num(c)*(1+2*(i%2)) for i,c in enumerate(isbn))%10==0

def valid(isbn):
    return (len(isbn)==10 and valid10(isbn)) or (len(isbn)==13 and valid13(isbn))

def main():
    N = int(input())
    Inval = []
    for _ in range(N):
        isbn = input()
        if not valid(isbn):
            Inval.append(isbn)
    print(len(Inval),'invalid:')
    for isbn in Inval:
        print(isbn)

main()
