#!/usr/bin/env python3

# Linear time Horn-SAT solver through unit-propagation
# https://en.wikipedia.org/wiki/Horn-satisfiability
# NB: Horn-SAT is of the two main classes of SAT problems to be in P
#     (along with 2-SAT).

from collections import defaultdict

def horn_sat_solver(V, Conj):
    C = len(Conj)
    Var2Clause = defaultdict(list)
    Unit = []
    for i in range(C):
        if len(Conj[i])==0:
            return None
        for x in Conj[i]:
            Var2Clause[x].append(i)
        if len(Conj[i])==1:
            Unit.append(i)
    Active = [True]*C
    Sol = [None]*(V+1)
    while Unit:
        i = Unit.pop()
        if len(Conj[i])==0:
            return None
        Active[i] = False
        x = Conj[i].pop()
        v = abs(x)
        if Sol[v] is None:
            Sol[v] = x
            for j in Var2Clause[x]:
                Active[j] = False
            for j in Var2Clause[-x]:
                if Active[j]:
                    Conj[j].remove(-x)
                    if len(Conj[j])==1:
                        Unit.append(j)
        elif Sol[v]!=x:
            return None
    for v in range(1,V+1):
        if Sol[v] is None:
            Sol[v] = -v
    return Sol[1:]

if __name__=='__main__':
    _,_,V,C = input().split()
    V,C = int(V),int(C)
    Conj = [set(map(int,input().split()[:-1])) for _ in range(C)]
    Sol = horn_sat_solver(V, Conj)
    if Sol is None:
        print('s UNSATISFIABLE')
    else:
        print('s SATISFIABLE')
        print('v', *Sol, '0')
