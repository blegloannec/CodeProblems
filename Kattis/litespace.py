#!/usr/bin/env python3

def run(P):
    S = []
    i = 0
    while i<len(P):
        if P[i:i+2]=='SS':
            i += 2
            neg = (P[i]=='T')
            i += 1
            n = 0
            while P[i]!='N':
                n = (n<<1) | (P[i]=='T')
                i += 1
            if neg:
                n = -n
            S.append(n)
            i += 1
        elif P[i:i+3]=='SNS':
            if len(S)>0:
                S.append(S[-1])
            else:
                print('Invalid copy operation')
            i += 3
        elif P[i:i+3]=='SNT':
            if len(S)>=2:
                S[-1],S[-2] = S[-2],S[-1]
            else:
                print('Invalid swap operation')
            i += 3
        elif P[i:i+3]=='SNN':
            if S:
                S.pop()
            else:
                print('Invalid remove operation')
            i += 3
        elif P[i:i+4]=='TSSS':
            if len(S)>=2:
                u = S.pop()
                v = S.pop()
                S.append(u+v)
            else:
                print('Invalid addition operation')
            i += 4
        elif P[i:i+4]=='TSST':
            if len(S)>=2:
                u = S.pop()
                v = S.pop()
                S.append(v-u)
            else:
                print('Invalid subtraction operation')
            i += 4
        elif P[i:i+4]=='TSSN':
            if len(S)>=2:
                u = S.pop()
                v = S.pop()
                S.append(u*v)
            else:
                print('Invalid multiplication operation')
            i += 4
        elif P[i:i+4]=='TSTS':
            if len(S)>=2:
                if S[-1]!=0:
                    u = S.pop()
                    v = S.pop()
                    # /!\ For negative quotients, the required integer division
                    #     is not the math euclidean division (that Python does)
                    #     but the expected behavior is to round towards 0.
                    q,r = divmod(v,u)
                    if q<0 and r!=0:
                        q += 1
                    S.append(q)
                else:
                    print('Division by zero')
            else:
                print('Invalid division operation')
            i += 4
        elif P[i:i+4]=='TNST':
            if len(S)>0:
                print(S.pop())
            else:
                print('Invalid print operation')
            i += 4
        else:
            assert False

run(input())
