#!/usr/bin/env python3

def main():
    N = int(input())
    S = input()
    # recursively removing "()" from S
    R = []
    for s in S:
        if s==')' and len(R)>0 and R[-1]=='(':
            R.pop()
        else:
            R.append(s)
    # R = ")" * a  +  "(" * b  with a+b even
    a = R.count(')')
    b = len(R)-a
    if a==b==0:
        res = 0
    elif a==0 or b==0:  # simple reverse one half of R
        res = 1
    else:  # reversing the ")" part leads to the previous case
        res = 2
    print(res)

main()
