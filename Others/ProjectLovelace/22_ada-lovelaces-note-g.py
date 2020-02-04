from fractions import Fraction

def bernoulli(n):
    Binom = [1,1]
    B = [Fraction(1),Fraction(-1,2)]
    for n in range(2,n+1):
        Binom = [1] + [Binom[k-1]+Binom[k] for k in range(1,n)] + [1]
        B.append(-sum(Binom[k] * B[k] * Fraction(1,n+1-k) for k in range(n)))
    return B[n].numerator, B[n].denominator