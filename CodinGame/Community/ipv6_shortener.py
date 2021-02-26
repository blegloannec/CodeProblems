#!/usr/bin/env python3

# 0. using a convenient module
#import ipaddress
#print(ipaddress.IPv6Address(input()))

# 1. handmade solution
ip = [x[:-1].lstrip('0')+x[-1] for x in input().split(':')]
lmax = rmax = i = 0
while i < len(ip):
    l = i
    while i < len(ip) and ip[i] == '0':
        i += 1
    if i-l > rmax-lmax:
        lmax,rmax = l,i
    i += 1
if rmax-lmax > 1:
    ip = ':'.join(ip[:lmax]) + '::' + ':'.join(ip[rmax:])
else:
    ip = ':'.join(ip)
print(ip)
