# le developpement est soit periodique soit fini
# il est fini ssi n divise une puissance de 10
# i.e. n = 2^k * 5^l (auquel cas n | 10^max(k,l))
# sinon 1/n est ultimement periodique :
# pour la fraction p/q avec p<q, on considere
# la DE 10*p = a*q + r et on recommence avec
# la fraction r/q, jusqu'a retomber sur un r deja
# rencontre, alors on boucle...
     
def dev_fini(n):
    while n%2==0:
        n /= 2
    while n%5==0:
        n /= 5
    return n==1

def period(n):
    t = [-1 for i in range(n)]
    r = 1
    i = 0
    while t[r]<0:
        t[r] = i
        i += 1
        r = (10*r)%n
    return i-t[r]

def main():
    pmax = 0
    nmax = 1000
    for n in range(2,nmax):
        if not dev_fini(n):
            p = period(n)
            if p>pmax:
                d = n
                pmax = p
    print d

main()
