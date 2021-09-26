#!/usr/bin/env python3

# interactive problem!

def main():
    R = int(input())
    l,r = 1,R
    for d in range(1,86):
        m = (l+r)//2
        print(d*m)
        ans = input()
        if ans=='less':
            r = m-1
        elif ans=='more':
            l = m+1
        else:
            break

main()
