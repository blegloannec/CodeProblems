#include <iostream>
using namespace std;

/*
  https://oeis.org/A000041

  P(n) = nb de partitions de n

  Methode 1 : selon le nb k de composantes
  P(n,k) = nb de partitions de n en k composantes exactement
  P(n,k) = P(n-1,k-1)+P(n-k,k)
  (derniere composante valant 1
   + toutes les composantes >=2 donc equivalent a
     partition de n-k en retirant 1 a chaque composante)
  P(n) = sum(P(n,k), k=1..n)
  ou encore
  P'(n,k) = nb de partitions de n en <=k composantes
  P'(n,k) = P'(n,k-1) + P'(n-k,k)
  (partitions en <k composantes
   + exactement k composantes donc en retirant 1 a toutes les composantes
     on se ramene aux partitions en <=k composantes de n-k)
  (c'est le meme raisonnement que pour P(.,.) mais en autorisant
   des composantes de taille 0)
  P(n) = P'(n,n)

  Methode 2 : selon la valeur max m des composantes
  Q(n,m) = nb de partitions de n en composantes <=m
  Q(n,m) = Q(n,m-1) + Q(n-m,m)
  (toutes composantes <m + au moins une composante valant m)
  P(n) = Q(n,n)

  Solution ci-dessous : calculer les Q(.,m) successifs pour des m croissants.

  NB : P(n,k) = Q(n,k) car ils verifient la meme relation de recurrence, mais
  cela peut se voir directement par la dualite sur les partitions d'entiers
  (transposition du diagramme de Young).

  NB a posteriori : le pre-calcul est ici en O(N^2), on peut en fait le faire
  en O(N*sqrt(N)) avec la formule d'Euler pour les partitions (via la fonction
  generatrice). Voir PE+ 78 d'HackerRank pour cette solution...
*/

const int M = 100000;
int Q[M];

int main() {
  for (int n=0; n<M; ++n) Q[n] = 1;
  for (int m=2; m<M; ++m) {
    if (Q[m-1]==0) {
      cout << m-1 << endl;
      break;
    }
    for (int n=m; n<M; ++n) Q[n] = (Q[n]+Q[n-m])%1000000;
  }
  return 0;
}
