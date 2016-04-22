#include <iostream>
using namespace std;

/*
  https://oeis.org/A000041

  P(n) = nb de partitions de n

  Methode 1 : selon le nb k de composantes
  P(n,k) = nb de partitions de n en k morceaux
  P(n,k) = P(n-1,k-1)+P(n-k,k)
  (derniere composante valant 1
   + toutes les composantes >=2 donc equivalent a
     partition de n-k en retirant 1 a chaque composante)
  P(n) = sum(P(n,k), k=1..n)

  Methode 2 : selon la valeur max m des composantes
  Q(n,m) = nb de partitions de n en morceaux <=m
  Q(n,m) = sum(Q(n-k,k), k=1..m)
  (Q(n-k,k) est le nb de partitions de n en morceaux <=k avec
   au moins 1 morceau de valeur k)
  P(n) = Q(n,n)

  Mais on peut aussi revisiter la methode 2 ainsi :
  Q(n,m) = Q(n,m-1)+Q(n-m,m)
  (toutes composantes <m + au moins une composante valant m)
  SOLUTION : Calculons les Q(.,m) successifs pour des m croissants !

  NB: dans le meme esprit on pourrait revisiter la methode 1 ainsi
  P'(n,k) = nb de partitions de n en <=k morceaux
  P'(n,k) = P'(n,k-1)+P(n,k)
  P(n) = P'(n,n)
  SOLUTION BIS : calculer les P(.,k) et P'(.,k) successifs pour des k croissants
  mais c'est un peu moins simple (maintenir 2 tableaux au lieu d'un seul)...

  NB a posteriori: le pre-calcul est ici en O(N^2), on peut en fait le faire
  en O(N*sqrt(N)) avec la formule d'Euler pour les partitions (via la fonction
  generatrice). Voir PE+ 78 d'HackerRank pour cette solution...
*/

const int M = 100000;
int Q[M];

int main() {
  for (int n=0; n<M; ++n) Q[n] = 1;
  for (int m=2; m<M; ++m) {
    //cout << m-1 << " " << Q[m-1] << endl;
    if (Q[m-1]==0) {
      cout << m-1 << endl;
      break;
    }
    for (int n=m; n<M; ++n) Q[n] = (Q[n]+Q[n-m])%1000000;
  }
  return 0;
}
