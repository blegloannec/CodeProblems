#!/usr/bin/env python3

def val(n,p):
    v = 0
    while n%p==0:
        v += 1
        n //= p
    return v

def fizzbuzz(n):
    s = str(n)
    c3 = s.count('3') + val(n,3)
    c5 = s.count('5') + val(n,5)
    return s if c3==c5==0 else 'Fizz'*c3+'Buzz'*c5

if __name__=='__main__':
    Rev = {}
    for n in range(1,1001):
        fb_n = fizzbuzz(n)
        if fb_n not in Rev:
            Rev[fb_n] = n
    N = int(input())
    for _ in range(N):
        I = input()
        print(Rev[I] if I in Rev else 'ERROR')
