import csv

Mass = {}
with open('periodic_table.csv') as csvfile:
    periodic_table_reader = csv.reader(csvfile, delimiter=',')
    for e,m in periodic_table_reader:
        Mass[e] = float(m)

def molecular_mass(chemical_formula):
    mass = 0
    s = len(chemical_formula)
    i = 0
    while i<s:
        assert 'A'<=chemical_formula[i]<='Z'
        e = chemical_formula[i]
        i += 1
        if i<s and 'a'<=chemical_formula[i]<='z':
            e += chemical_formula[i]
            i += 1
        assert e in Mass
        c = 0
        while i<s and '0'<=chemical_formula[i]<='9':
            c = 10*c + ord(chemical_formula[i]) - ord('0')
            i += 1
        if c==0:
            c = 1
        mass += c*Mass[e]
    return mass

if __name__=='__main__':
    for M in ('Pa', 'OCS', 'C4H4AsH', 'C20H25N3O'):
        print(M, molecular_mass(M))
