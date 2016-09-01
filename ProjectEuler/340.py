#!/usr/bin/env python

# Considerons F definie pour a,b,c
# et G pour ka,kb,kc, avec k>=1
# On A G(kn) = kn-kc = kF(n) si kn>kb (ie n>b)
# et G(kn) = G(ka + G(ka + G(ka + G(ka+kn))))
#          = G(ka + G(ka + G(ka + kF(a+n))))
#          = G(ka + G(ka + kF(a + F(a+n))))
#          = G(ka + kF(a + F(a + F(a+n))))
#          = kF(a + F(a + F(a + F(a+n))))
#          = kF(n)
# si kn<=kb (ie n<=b), et en raisonnant par induction
# mais ca ne nous aide pas ici car gcd(a,b,c) = 1
# et on n'a pas espoir d'une vraie linearite (en decomposant
# a,b,c comme sommes de 2 nombres) a cause des cas croises.

# Si n<=b mais a+n>b, on a F(n) = F(a+F(a+F(2a+n-c)))
# en supposant a>c, comme c'est le cas dans les donnees du pb,
# on a 2a+n-c > a+n > b, donc F(n) = F(a+F(3a+n-2c)) = F(4a+n-3c) = 4a+n-4c
# On sait donc maintenant que F(n) = 4a+n-4c pour b-a < n <= b
# mais alors si n<=b-a mais n+a>b-a, ie b-2a < n <= b-a alors
# F(n) = F(a+F(a+F(a+F(n)))) = F(a+F(a+F(5a+n-4c))) = F(a+F(a+F(5a+n-4c)))
# avec b-a+4(a-c) < 5a+n-4c <= b+4(a-c), d'ou, en supposant 4(a-c) >= a,
# F(n) = F(a+F(6a+n-5c)) = F(7a+n-6c) = 8a+n-7c
# et ainsi de suite, pour b-ka < n <= b-(k-1)a, on aura F(n) = 4ka+n-(4+3(k-1))c
# (en 1 application de F, on passe >b, on fait alors +3a-3c sur les 3 restantes)

M = 10**9

def S(a,b,c):
    s = 0
    k = 1
    while b-(k-1)*a>=0:
        n1 = max(0,b-k*a+1)
        n2 = b-(k-1)*a
        s = (s+(n2-n1+1)*(4*k*a+n1-(4+3*(k-1))*c+4*k*a+n2-(4+3*(k-1))*c)/2)%M
        k += 1
    return s

#print S(50,2000,40)
print S(21**7,7**21,12**7)
