#!/usr/bin/env python3

# interactive problem!

import sys
input = sys.stdin.readline

def send_recv(d):
    sys.stdout.write(d+'\n')
    sys.stdout.flush()
    return input().strip()

Dirs = (('up',-1,0,'down'),('down',1,0,'up'),('left',0,-1,'right'),('right',0,1,'left'))
Seen = [[False]*210 for _ in range(210)]
def dfs(x=105,y=105):
    Seen[x][y] = True
    for d,dx,dy,invd in Dirs:
        vx,vy = x+dx,y+dy
        if not Seen[vx][vy]:
            ans = send_recv(d)
            if ans=='solved':
                sys.exit()
            elif ans=='ok':
                dfs(vx,vy)
                assert send_recv(invd)=='ok'
            elif ans=='wrong':
                sys.exit(1)

def main():
    dfs()
    assert send_recv('no way out')=='solved'

main()
