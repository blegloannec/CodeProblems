#!/usr/bin/env python3

from fractions import Fraction
from collections import Counter, defaultdict
from functools import lru_cache

# Let E = proba space of possible solutions from {T,F}^Q that are
#         consistent will all given students scores
#         (i.e. the set of solutions that coincides with
#          A_i at exactly S_i answers, for all 1 <= i <= N)
# Let p_i the proba of answer i being T in solutions of E.
# If each student has given the same answer to questions i and j,
# then obviously p_i = p_j. Hence there are only 2^N values of p_i.
# E.g., for N = 2, pTT, pFF, pTF and  pFT.
# (Formally, f : E -> E that swaps positions i/j, is a well-defined
#  score-preserving bijection.)
# Similarly, if each student as given different answers to questions
# i and j, then p_i = 1-p_j. Indeed, formally, f : E -> E that swaps
# positions i/j and flip answers T/F, is a score-preserving bijection.
# E.g., for N = 2, pTT = 1-pFF and pTF = 1-pFT.
# Computing the expected value over E of the score of each student,
# (which is their score by definition of E), we get N equations, for
# 2^(N-1) unknown.

@lru_cache(maxsize=None)
def binom(n, p):
    if 0<=p<=n:
        return 1 if p==0 else n*binom(n-1,p-1)//p
    return 0

def main():
    T = int(input())
    for t in range(1, T+1):
        N,Q = map(int, input().split())
        A = []
        S = []
        for _ in range(N):
            Aj,Sj = input().split()
            A.append(Aj)
            S.append(int(Sj))
        GA = [''.join(Ai[j] for Ai in A) for j in range(Q)]  # grouped answers
        Cnt = Counter(GA)

        if N==1:
            # #T*pT + #F*(1-pF) = S
            # #T*pT + #F*pT = S
            # pT = S/(#T+#F)
            pT = Fraction(S[0], Q)
            P = {'T': pT, 'F': Fraction(1)-pT}
        elif N==2:
            # #TT*pTT + #FF*(1-pFF) + #TF*pTF + #FT*(1-pFT) = S0
            # #TT*pTT + #FF*(1-pFF) + #TF*(1-pTF) + #FT*pFT = S1

            # #TT*pTT + #FF*pTT + #TF*pTF + #FT*pTF = S0
            # #TT*pTT + #FF*pTT + #TF*(1-pTF) + #FT*(1-pTF) = S1

            # (#TT+#FF)*pTT + (#TF+#FT)*pTF = S0
            # (#TT+#FF)*pTT - (#TF+#FT)*pTF = S1-(#TF+#FT)

            # cTT*pTT + cTF*pTF = S0
            # cTT*pTT - cTF*pTF = S1-cTF

            cTT = Cnt['TT']+Cnt['FF']
            cTF = Cnt['TF']+Cnt['FT']
            if cTT==0:
                pTT = 0  # won't happen
                pTF = Fraction(S[0], cTF)
            elif cTF==0:
                pTT = Fraction(S[0], cTT)
                pTF = 0  # won't happen
            else:
                pTT = Fraction(S[0]+(S[1]-cTF), 2*cTT)
                pTF = Fraction(S[0]-(S[1]-cTF), 2*cTF)
            P = {'TT': pTT, 'FF': Fraction(1)-pTT, 'TF': pTF, 'FT': Fraction(1)-pTF}
        else:
            # For N = 3, we have 3 eq. but 2^(3-1) = 4 unknowns
            # See the official analysis for discussions about that...
            # Here we use a meet-in-the-middle approach that should
            # be close to O(Q²), even though below we actually enumerate
            # all valid quadruples.
            # This could formally be made O(Q²) by precomputing (a,b)-part
            # partial counts instead of storing all (a,b) couples, but this
            # would be slower in practice, so...
            cTTT = Cnt['TTT'] + Cnt['FFF']
            cTTF = Cnt['TTF'] + Cnt['FFT']
            cTFT = Cnt['TFT'] + Cnt['FTF']
            cTFF = Cnt['TFF'] + Cnt['FTT']
            # precomp. left (a,b) part
            DL = defaultdict(list)
            for a in range(cTTT+1):
                for b in range(cTTF+1):
                    L = (a + b, a + b, a + cTTF-b)
                    DL[L].append((a,b))
            # right (c,d) part & meet-in-the-middle
            tot = pTTT = pTTF = pTFT = pTFF = 0
            for c in range(cTFT+1):
                for d in range(cTFF+1):
                    R = (c + d, cTFT-c + cTFF-d, c + cTFF-d)
                    L = tuple(s-r for s,r in zip(S,R))
                    if L in DL:
                        for a,b in DL[L]:
                            tot  += binom(cTTT,a)     * binom(cTTF,b)     * binom(cTFT,c)     * binom(cTFF,d)
                            pTTT += binom(cTTT-1,a-1) * binom(cTTF,b)     * binom(cTFT,c)     * binom(cTFF,d)
                            pTTF += binom(cTTT,a)     * binom(cTTF-1,b-1) * binom(cTFT,c)     * binom(cTFF,d)
                            pTFT += binom(cTTT,a)     * binom(cTTF,b)     * binom(cTFT-1,c-1) * binom(cTFF,d)
                            pTFF += binom(cTTT,a)     * binom(cTTF,b)     * binom(cTFT,c)     * binom(cTFF-1,d-1)
            P = {'TTT': Fraction(pTTT,tot), \
                 'TTF': Fraction(pTTF,tot), \
                 'TFT': Fraction(pTFT,tot), \
                 'TFF': Fraction(pTFF,tot)}
            P['FFF'] = Fraction(1) - P['TTT']
            P['FFT'] = Fraction(1) - P['TTF']
            P['FTF'] = Fraction(1) - P['TFT']
            P['FTT'] = Fraction(1) - P['TFF']

        # Building solution
        Ans = []
        E = Fraction(0)
        for a in GA:
            if P[a]>Fraction(1,2):
                Ans.append('T')
                E += P[a]
            else:
                Ans.append('F')
                E += Fraction(1) - P[a]
        print(f'Case #{t}: {"".join(Ans)} {E.numerator}/{E.denominator}')

main()
