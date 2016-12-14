#!/usr/bin/env python

def looknsay(s):
    t  = []
    i = 0
    while i<len(s):
        c = 1
        while i+c<len(s) and s[i+c]==s[i]:
            c += 1
        t.append(str(c))
        t.append(s[i])
        i = i+c
    return ''.join(t)

# Conway proved that ultimately each term of the sequence
# can be split into elements that evolve independently
# http://www.se16.info/js/lands2.htm
# http://www.lifl.fr/~jdelahay/pls/032.pdf
# Starting from '1', the first term that seems to follow that
# rule is step 7 = 1113213211 = Hf Sn

E = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U']

D = {'Ru': (43, '132211331222113112211', ['Eu', 'Ca', 'Tc']), 'Re': (74, '111312211312113221133211322112211213322113', ['Ge', 'Ca', 'W']), 'Ra': (87, '132113', ['Fr']), 'Rb': (36, '1321122112', ['Kr']), 'Rn': (85, '311311222113', ['Ho', 'At']), 'Rh': (44, '311311222113111221131221', ['Ho', 'Ru']), 'Be': (3, '111312211312113221133211322112211213322112', ['Ge', 'Ca', 'Li']), 'Ba': (55, '311311', ['Cs']), 'Bi': (82, '3113322113', ['Pm', 'Pb']), 'Br': (34, '3113112211322112', ['Se']), 'H': (0, '22', ['H']), 'P': (14, '311311222112', ['Ho', 'Si']), 'Os': (75, '1321132122211322212221121123222113', ['Re']), 'Hg': (79, '31121123222113', ['Au']), 'Ge': (31, '31131122211311122113222', ['Ho', 'Ga']), 'Gd': (63, '13221133112', ['Eu', 'Ca', 'Co']), 'Ga': (30, '13221133122211332', ['Eu', 'Ca', 'Ac', 'H', 'Ca', 'Zn']), 'Pr': (58, '31131112', ['Ce']), 'Pt': (77, '111312212221121123222113', ['Ir']), 'C': (5, '3113112211322112211213322112', ['B']), 'Pb': (81, '123222113', ['Tl']), 'Pa': (90, '13', ['Th']), 'Pd': (45, '111312211312113211', ['Rh']), 'Cd': (47, '3113112211', ['Ag']), 'Po': (83, '1113222113', ['Bi']), 'Pm': (60, '132', ['Nd']), 'Ho': (66, '1321132', ['Dy']), 'Hf': (71, '11132', ['Lu']), 'K': (18, '1112', ['Ar']), 'He': (1, '13112221133211322112211213322112', ['Hf', 'Pa', 'H', 'Ca', 'Li']), 'Mg': (11, '3113322112', ['Pm', 'Na']), 'Mo': (41, '13211322211312113211', ['Nb']), 'Mn': (24, '111311222112', ['Cr', 'Si']), 'O': (7, '132112211213322112', ['N']), 'S': (15, '1113122112', ['P']), 'W': (73, '312211322212221121123222113', ['Ta']), 'Zn': (29, '312', ['Cu']), 'Eu': (62, '1113222', ['Sm']), 'Zr': (39, '12322211331222113112211', ['Y', 'H', 'Ca', 'Tc']), 'Er': (67, '311311222', ['Ho', 'Pm']), 'Ni': (27, '11133112', ['Zn', 'Co']), 'Na': (10, '123222112', ['Ne']), 'Nb': (40, '1113122113322113111221131221', ['Er', 'Zr']), 'Nd': (59, '111312', ['Pr']), 'Ne': (9, '111213322112', ['F']), 'Fr': (86, '1113122113', ['Rn']), 'Fe': (25, '13122112', ['Mn']), 'B': (4, '1321132122211322212221121123222112', ['Be']), 'F': (8, '31121123222112', ['O']), 'Sr': (37, '3112112', ['Rb']), 'N': (6, '111312212221121123222112', ['C']), 'Kr': (35, '11131221222112', ['Br']), 'Si': (13, '1322112', ['Al']), 'Sn': (49, '13211', ['In']), 'Sm': (61, '311332', ['Pm', 'Ca', 'Zn']), 'V': (22, '13211312', ['Ti']), 'Sc': (20, '3113112221133112', ['Ho', 'Pa', 'H', 'Ca', 'Co']), 'Sb': (50, '3112221', ['Pm', 'Sn']), 'Se': (33, '13211321222113222112', ['As']), 'Co': (26, '32112', ['Fe']), 'Cl': (16, '132112', ['S']), 'Ca': (19, '12', ['K']), 'Ce': (57, '1321133112', ['La', 'H', 'Ca', 'Co']), 'Xe': (53, '11131221131211', ['I']), 'Lu': (70, '311312', ['Yb']), 'Cs': (54, '13211321', ['Xe']), 'Cr': (23, '31132', ['V']), 'Cu': (28, '131112', ['Ni']), 'La': (56, '11131', ['Ba']), 'Li': (2, '312211322212221121123222112', ['He']), 'Tl': (80, '111213322113', ['Hg']), 'Tm': (68, '11131221133112', ['Er', 'Ca', 'Co']), 'Th': (89, '1113', ['Ac']), 'Ti': (21, '11131221131112', ['Sc']), 'Te': (51, '1322113312211', ['Eu', 'Ca', 'Sb']), 'Tb': (64, '3113112221131112', ['Ho', 'Gd']), 'Tc': (42, '311322113212221', ['Mo']), 'Ta': (72, '13112221133211322112211213322113', ['Hf', 'Pa', 'H', 'Ca', 'W']), 'Yb': (69, '1321131112', ['Tm']), 'Dy': (65, '111312211312', ['Tb']), 'I': (52, '311311222113111221', ['Ho', 'Te']), 'U': (91, '3', ['Pa']), 'Y': (38, '1112133', ['Sr', 'U']), 'Ac': (88, '3113', ['Ra']), 'Ag': (46, '132113212221', ['Pd']), 'Ir': (76, '3113112211322112211213322113', ['Os']), 'Al': (12, '1113222112', ['Mg']), 'As': (32, '11131221131211322113322112', ['Ge', 'Na']), 'Ar': (17, '3112', ['Cl']), 'Au': (78, '132112211213322113', ['Pt']), 'At': (84, '1322113', ['Po']), 'In': (48, '11131221', ['Cd'])}

def count123(s):
    C = [0,0,0]
    for c in s:
        C[ord(c)-ord('1')] += 1
    return C

P = 1<<30 # modulus

class Matrice:
    def __init__(self,M):
        self.M = M
        self.m = len(M)
        self.n = len(M[0])

    def __getitem__(self,i):
        return self.M[i]
        
    def __mul__(self,A):
        assert(self.n==A.m)
        C = Matrice([[0 for _ in xrange(A.n)] for _ in xrange(self.m)])
        for i in xrange(self.m):
            for j in xrange(A.n):
                for k in xrange(self.n):
                    C[i][j] = (C[i][j]+self[i][k]*A[k][j])%P
        return C

    def copy(self):
       return Matrice([self[i][:] for i in xrange(self.m)])
    
    def __pow__(self,b):
        assert(self.m==self.n)
        result = Matrice([[int(i==j) for j in xrange(self.n)] for i in xrange(self.n)])
        A = self.copy()
        while b:
            if b & 1:
                result *= A
            A *= A
            b >>= 1
        return result

def main():
    # transition matrix
    M = [[0 for _ in xrange(92)] for _ in xrange(92)]
    for i in xrange(92):
        for J in D[E[i]][2]:
            j = D[J][0]
            M[j][i] += 1
    M = Matrice(M)
    I = [[0] for _ in xrange(92)]
    I[D['Hf'][0]][0] = 1
    I[D['Sn'][0]][0] = 1
    I = Matrice(I)
    A = M**(10**12-8)*I
    C = [0,0,0]
    for i in xrange(92):
        C0 = count123(D[E[i]][1])
        for j in xrange(3):
            C[j] = (C[j] + C0[j]*A[i][0])%P
    print ','.join(map(str,C))

main()