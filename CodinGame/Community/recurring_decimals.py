#!/usr/bin/env python3

def main():
    r = 1
    q = int(input())
    seen = {}
    D = []
    while r not in seen:
        seen[r] = len(D)
        a,r = divmod(10*r,q)
        D.append(a)
    t = seen[r]
    pre = ''.join(map(str,D[:t]))
    per = ''.join(map(str,D[t:]))
    if per=='0':
        print('0.%s' % pre)
    else:
        print('0.%s(%s)' % (pre,per))

main()
