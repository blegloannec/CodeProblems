# Handmade solution

# 6531031914842725

# il faut former une chaine de taille 16, et non 17, 10 doit etre
# a l'exterieur

# pour demarrer par le plus grand nombre possible,
# mettre les 5 plus grands nombres 6-10 a l'exterieur
# comme on commencera par le plus petit (6), on les place
# dans l'ordre 6 10 9 8 7 sur les points exterieurs

# on place le plus grand des 5 nb restants 1-5 a cote de 6
# et on essaye de completer progressivement les 4 cases restantes
# en essayant les nombres 4-1 sur la troisieme case de la ligne
# 6,5,? ce qui fixe a chaque fois la somme, et permet de completer
# de facon deterministe les 4 cases restantes

# on trouve une solution pour la valeur 3 (somme 14) :
# 6,5,3 ; 10,3,1 ; 9,1,4 ; 8,4,2 ; 7,2,5
