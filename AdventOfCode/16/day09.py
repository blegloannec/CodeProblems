#!/usr/bin/env python

import sys

# handmade (not using RE) marker parsing
def marker(s,i,L):
    if s[i]!='(':
        return None
    i += 1
    x = 0
    while i<L and ord('0')<=ord(s[i])<=ord('9'):
        x = 10*x + ord(s[i])-ord('0')
        i += 1
    if i==L or s[i]!='x':
        return None
    i += 1
    y = 0
    while i<L and ord('0')<=ord(s[i])<=ord('9'):
        y = 10*y + ord(s[i])-ord('0')
        i += 1
    if i==L or s[i]!=')':
        return None
    i += 1
    return (x,y,i)

# Part One
def dec_len(F,I0,L):
    res = 0
    i = I0
    while i<L:
        O = marker(F,i,L)
        if O!=None:
            x,y,j = O
            res += y*x
            i = j+x
        else:
            res += 1
            i += 1
    return res

# Part Two
def rec_dec_len(F,I0,L):
    res = 0
    i = I0
    while i<L:
        O = marker(F,i,L)
        if O!=None:
            x,y,j = O
            res += y*rec_dec_len(F,j,j+x)
            i = j+x
        else:
            res += 1
            i += 1
    return res

# MAIN
F = sys.stdin.readline().strip()
print dec_len(F,0,len(F))
print rec_dec_len(F,0,len(F))
