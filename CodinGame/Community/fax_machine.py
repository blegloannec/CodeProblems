#!/usr/bin/env python3

W = int(input())
H = int(input())
O = ''.join('* '[i&1]*int(l) for i,l in enumerate(input().split()))
print('\n'.join(f'|{O[i:i+W]}|' for i in range(0,H*W,W)))
