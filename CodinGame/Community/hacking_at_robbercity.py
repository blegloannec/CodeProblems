#!/usr/bin/env python3

X = bytes.fromhex(input())  # M ^ A
Y = bytes.fromhex(input())  # M ^ A ^ B
Z = bytes.fromhex(input())  # M ^ B

M = bytes(x^y^z for x,y,z in zip(X,Y,Z))
print(M.decode())
