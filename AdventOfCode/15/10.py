#!/usr/bin/env python

def looknsay(s):
    res = []
    i = 0
    while i<len(s):
        c = s[i]
        n = 1
        while i+n<len(s) and s[i+n]==c:
            n += 1
        res.append(str(n))
        res.append(c)
        i += n
    return ''.join(res)

def main():
    s = '1113222113'
    for i in range(50):
        s = looknsay(s)
        if i==39:
            print len(s)
    print len(s)

main()
