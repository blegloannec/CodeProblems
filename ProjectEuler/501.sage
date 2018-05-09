# si n = Prod_i pi^ai decomposition primale
# alors #div(n) = Prod_i ai+1
# donc n a exactement 8 diviseurs ssi il est de la forme
# n = p^7 ou n = pq^3 ou n = pqr avec p,q,r premiers distincts

# on utilise ici le denombrement rapide prime_pi() de Sage (~45s)
# https://en.wikipedia.org/wiki/Meissel%E2%80%93Lehmer_algorithm
# http://acganesh.com/blog/2016/12/23/prime-counting

# voir aussi http://images.math.cnrs.fr/Nombres-a-huit-diviseurs.html

memo = {}
def memo_prime_pi(n):
    if n not in memo:
        memo[n] = prime_pi(n)
    return memo[n]

def prime_pi_range(l,r):
    return 0 if r<=l else memo_prime_pi(r) - memo_prime_pi(l-1)

def f_p7(n):
    return memo_prime_pi(n^(1/7))

def f_pq3(n):
    return sum(memo_prime_pi(int(n/q^3)) for q in prime_range(int(n^(1/3))+1)) - memo_prime_pi(int(n^(1/4)))

def f_pqr(n):
    res = 0
    for p in prime_range(int(n^(1/3))+1):
        for q in prime_range(p+1,int((n/p)^(1/2))+1):
            res += prime_pi_range(q+1,int(n/(p*q)))
    return res

def f(n):
    return f_p7(n) + f_pq3(n) + f_pqr(n)

print(f(10^12))
