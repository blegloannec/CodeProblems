#!/usr/bin/env python3

def ip_str(x):
    return '.'.join(str((x>>(8*i))&255) for i in range(3,-1,-1))

ip,mask = input().split('/')
ip = sum(x<<(8*i) for i,x in enumerate(map(int,reversed(ip.split('.')))))
mask = int(mask)
mask = ((1<<mask)-1)<<(32-mask)

print(ip_str(ip&mask))
print(ip_str(ip|~mask))
