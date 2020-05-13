#!/usr/bin/env python3

def sat(Form):  # backtracking on clauses
    if len(Form)==0:
        return True
    for x0,v0 in Form[0]:
        NewForm = []
        nonempty = True
        for i in range(1,len(Form)):
            C = []
            satisfied = False
            for x,v in Form[i]:
                if x==x0:
                    if v==v0:
                        satisfied = True
                        break
                else:
                    C.append((x,v))
            if not satisfied:
                if C:
                    NewForm.append(C)
                else:  # empty clause
                    nonempty = False
                    break
        if nonempty and sat(NewForm):
            return True
    return False

def main():
    T = int(input())
    for _ in range(T):
        N,M = map(int, input().split())
        Form = []
        for _ in range(M):
            C = []
            for x in input().split(' v '):
                val = x[0]!='~'
                var = int(x[2-val:])-1
                C.append((var,val))
            Form.append(C)
        Form.sort(key=len)
        print('satisfiable' if sat(Form) else 'unsatisfiable')

main()
