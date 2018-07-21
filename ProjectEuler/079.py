#!/usr/bin/env python

data = ['129','160','162','168','180','289','290','316','318','319','362','368','380','389','620','629','680','689','690','710','716','718','719','720','728','729','731','736','760','762','769','790','890']

# No digit is repeated in any of the data
# We make the following guess: it is the same in the solution
# If this is true, then a topological sort solves the problem

N = 10
M = [[False for _ in range(N)] for _ in range(N)]
visited = []
toposort = []

def dfs(u):
    visited[u] = True
    for v in range(N):
        if M[u][v] and not visited[v]:
            dfs(v)
    toposort.append(u)

def main():
    global visited,toposort
    for d in data:
        M[int(d[0])][int(d[1])] = True
        M[int(d[1])][int(d[2])] = True
    sol = ''
    for s in range(N):
        visited = [False for _ in range(N)]
        toposort = []
        dfs(s)
        if len(toposort)>len(sol):
            sol = ''.join(map(str,toposort[::-1]))
    print sol

main()
