#!/usr/bin/env python3

# Attention : on n'a pas le droit de vider une boite
# donc une boite incorrecte de rang pair contenant 1
# ne peut que recevoir (et pas donner)

def boxes(n,X):
    n1 = 0  # boites incorrectes ne pouvant que recevoir 1
    ni = 0  # boites incorrectes pouvant donner/recevoir 1
    e = 0   # excedent que l'on peut repartir
    for i in range(n):
        if i%2==0 and X[i]==1:
            n1 += 1
        else:
            ie = int(i%2!=X[i]%2)
            e += X[i]-ie-(2-i%2)
            ni += ie
    # on transfere des ni vers les n1
    if ni>=n1:
        ni -= n1
        return -1 if ni%2==1 else n1+ni//2
    else:
        n1 -= ni
        return -1 if n1%2==1 or e<n1 else ni+n1
        
def main():
    q = int(input())
    for _ in range(q):
        n = int(input())
        X = list(map(int,input().split()))
        print(boxes(n,X))

main()
