# on fait joujou avec Julia, la taille de la matrice
# etant assez grande (61), on a un overflow en Int128 avec un simple
# produit de matrice, donc on bricole une arithmetique modulaire
# attention le code suivant est "cool", mais lent
# a cause de l'utilisation de type/operateurs custom

# Contrairement au pb de PE, on compte ici les combinaisons.
# Soit Tout la liste (avec multiplicite) des points qu'il est possible
# de marquer avec une flechette (60 valeurs).
# Soit Double la liste des points qu'il est possible de marquer en
# faisant un double.
# Sans terminer necessairement par un double :
# C(n) le nb de combinaisons verifie clairement la relation de
# recurrence C(n) = sum( C(n-x), x in Tout ) de profondeur 60
# S(n) = S(n-1) + C(n) verifie alors une RRL de degre 61
# Avec la contrainte de double final :
# C'(n) = sum( C(n-x), x in Double ) verifie une RRL de degre 60
# S'(n) = S'(n-1) + C'(n) verifie une relation de RRL de degre 61
# Apres calcul, avec l'aide de Sage, la table M0 plus bas contient
# les coeffs de cette recurrence.

# pour definir de nouvelles methodes de base
importall Base

# modulo
P = 10^9+9

# definition d'un type d'entier modulo
type IntMod
  n::Int64

  function IntMod(n)
    new(n)
  end
end

# definition des operateurs pour ce type
+(a::IntMod,b::IntMod) = IntMod((a.n+b.n)%P)
-(a::IntMod,b::IntMod) = IntMod((a.n-b.n+P)%P)
*(a::IntMod,b::IntMod) = IntMod((a.n*b.n)%P)
zero(a::IntMod) = IntMod(0)
zero(a::Type{IntMod}) = IntMod(0)
one(a::Type{IntMod}) = IntMod(1)
convert(a::Type{IntMod},b::Int64) = IntMod(b)
show(io::IO, a::IntMod) = show(io,a.n)

# matrice du pb
M0 = [2 1 0 0 P-1 2 P-2 1 0 0 P-1 2 P-2 1 0 0 P-1 2 P-2 1 P-1 0 P-1 2 P-1 0 0 0 P-1 2 P-2 1 0 0 P-1 2 P-2 1 0 0 P-1 1 P-1 0 1 P-1 0 1 P-1 1 0 P-1 0 1 P-1 0 1 P-1 0 1 P-1]
M = zeros(IntMod,61,61)
for i = 1:61
  M[1,i] = M0[i]
  if i>1
    M[i,i-1] = 1
  end
end
Init = IntMod[234966370 ; 153505823 ; 651805486 ; 345894890 ; 984356873 ; 298478575 ; 757386272 ; 161731070 ; 290714545 ; 887947027 ; 992076992 ; 684113732 ; 17057502 ; 45336236 ; 543862818 ; 182185808 ; 386816425 ; 476646378 ; 408396218 ; 221770928 ; 93719952 ; 473239815 ; 497506602 ; 352454411 ; 969647274 ; 646036526 ; 841312877 ; 802659834 ; 358399823 ; 361638274 ; 489532034 ; 67542656 ; 888031543 ; 929716878 ; 294214816 ; 451830141 ; 436559373 ; 597857519 ; 248812332 ; 103549006 ; 43094346 ; 17934695 ; 7463955 ; 3106286 ; 1292762 ; 538006 ; 223909 ; 93180 ; 38783 ; 16137 ; 6718 ; 2794 ; 1164 ; 483 ; 202 ; 83 ; 35 ; 14 ; 6 ; 2 ; 1]

# MAIN
N = parse(Int64,readline(STDIN))-1
if N<=61
  println(Init[62-N])
else
  X = M^(N-61)*Init
  println(X[1])
end
