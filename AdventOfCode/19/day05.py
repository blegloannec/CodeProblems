#!/usr/bin/env python3

P = list(map(int,input().split(',')))

def run(P, In):
    P = P[:]  # program copy
    i = 0     # instruction pointer
    i_in = 0  # input pointer
    param = lambda k: P[i+k] if (P[i]//10**(1+k))%10 else P[P[i+k]]
    while True:
        op = P[i] % 100
        if   op==1:  # add
            P[P[i+3]] = param(1) + param(2)
            i += 4
        elif op==2:  # mul
            P[P[i+3]] = param(1) * param(2)
            i += 4
        elif op==3:  # input
            assert i_in < len(In)
            print('input %d' % In[i_in])
            P[P[i+1]] = In[i_in]
            i_in += 1
            i += 2
        elif op==4:  # output
            print(param(1))
            i += 2
        elif op==5:  # jnz
            if param(1)!=0:
                i = param(2)
            else:
                i += 3
        elif op==6:  # jz
            if param(1)==0:
                i = param(2)
            else:
                i += 3
        elif op==7:  # lt
            P[P[i+3]] = 1 if param(1)<param(2) else 0
            i += 4
        elif op==8:  # eq
            P[P[i+3]] = 1 if param(1)==param(2) else 0
            i += 4
        else:
            assert op==99
            break

run(P,[1])
print('='*10)
run(P,[5])
