#!/usr/bin/env python

import hashlib

def md5(s):
    m = hashlib.md5()
    m.update(s)
    return m.hexdigest()

I = 'cxdnnyjw'

# Part One
def password(s):
    i = 0
    P = []
    for _ in xrange(8):
        h = md5(s+str(i))
        while h[:5]!='00000':
            i += 1
            h = md5(s+str(i))
        P.append(h[5])
        i += 1
    return ''.join(P)

print password(I)


# Part Two
def password2(s):
    i = 0
    P = [None for _ in xrange(8)]
    c = 0
    while c<8:
        h = md5(s+str(i))
        while h[:5]!='00000':
            i += 1
            h = md5(s+str(i))
        if ord('0')<=ord(h[5])<=ord('7') and P[int(h[5])]==None:
            P[int(h[5])] = h[6]
            c += 1
        i += 1
    return ''.join(P)

print password2(I)
