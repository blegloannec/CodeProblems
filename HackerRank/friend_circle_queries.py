#!/usr/bin/env python3

# pretty straigthforward union-find

Tarj = []
Size = []
MaxSize = 0

def find(x):
    if Tarj[x]<0:
        return x
    Tarj[x] = find(Tarj[x])
    return Tarj[x]

def union(x,y):
    global MaxSize
    x0, y0 = find(x), find(y)
    if x0!=y0:
        Tarj[y0] = x0
        Size[x0] += Size[y0]
        MaxSize = max(MaxSize, Size[x0])

if __name__ == '__main__':
    Q = int(input())
    Num = {}
    for _ in range(Q):
        x,y = map(int,input().split())
        for u in (x,y):
            if u not in Num:
                Num[u] = len(Num)
                Tarj.append(-1)
                Size.append(1)
        union(Num[x], Num[y])
        print(MaxSize)
