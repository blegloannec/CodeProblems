#!/bin/env python3

def find(x):
    if T[x]<0:
        return x
    T[x] = find(T[x])
    return T[x]

def union(x,y):
    x0,y0 = find(x),find(y)
    T[y0] = x0
    Size[x0] += Size[y0]

def main():
    global T,Size
    q = int(input())
    for _ in range(q):
        n,m = map(int,input().split())
        T = [-1]*n
        Size = [1]*n
        Extra = 0
        for _ in range(m):
            u,v = map(int,input().split())
            u -= 1
            v -= 1
            if find(u)!=find(v):
                # edge that connects 2 components (increase friends)
                union(u,v)
            else:
                # edge within a component (no improvement)
                Extra += 1
        # sort components by decreasing size
        C = sorted((Size[u] for u in range(n) if find(u)==u), reverse=True)
        # for each component from the largest to the smallest
        #   add useful edges (n-1 edges forming a spanning tree for a
        #   component of size n) in an order that increase the size of
        #   the component by 1 at each step
        res = A = 0  # global sum  &  sum of friends at the current step
        for c in C:
            #for i in range(1,c):
            #    res += A + i*(i+1)
            res += (c-1)*A + (c-1)*c*(2*c-1)//6 + (c-1)*c//2
            A += c*(c-1)
        # add extra edges (after having maximized A)
        res += A*Extra
        print(res)

main()
