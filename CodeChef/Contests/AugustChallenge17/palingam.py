#!/usr/bin/env python3

# Cas 1 : B possede au moins un exemplaire de chaque lettre de A,
#         B gagne a son premier tour en posant la meme lettre que A.

# Dans la suite, A possede des lettres que B n'a pas et commence par poser
# une de ces lettres.

# Cas 2 : A possede au moins 2 exemplaires d'une lettre "a" que B ne possede
#         pas, alors A gagne a son deuxieme tour en formant "aba" pour "b"
#         la lettre differente de "a" posee par B.

# Dans la suite A, possede des lettres que B n'a pas mais en un seul
# exemplaire chacune et commence par poser une de ces lettres.
# Alors cette lettre est unique et doit etre au centre pour former un
# palindrome de taille necessairement impaire. Donc seul A peut desormais
# former un palindrome et B ne gagne qu'en interdisant cette formation.

# Cas 3 : B possede au moins une lettre que A n'a pas,
#         il gagne en interdisant la formation d'un palindrome en posant
#         toujours les exemplaires de cette lettre du meme cote de la lettre
#         initiale de A, brisant ainsi toute symetrie.

# Dans la suite, A possede toutes les lettres de B.

# Cas 4 : A gagne a son deuxieme tour en formant "bab" pour "b" la lettre
#         posee par B a son premier tour.

def num(c):
    return ord(c)-ord('a')

def count(S):
    C = [0]*26
    for c in S:
        C[num(c)] += 1
    return C

def main():
    T = int(input())
    for _ in range(T):
        A = count(input())
        B = count(input())
        winner = 'A'
        # cas 1
        if all(A[i]==0 or B[i]>=1 for i in range(26)):
            winner = 'B'
        # cas 2
        elif any(B[i]==0 and A[i]>=2 for i in range(26)):
            winner = 'A'
        # cas 3
        elif any(A[i]==0 and B[i]>=1 for i in range(26)):
            winner = 'B'
        print(winner)

main()
