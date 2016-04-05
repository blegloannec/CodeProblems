#include <iostream>
using namespace std;

/*
  https://oeis.org/A000041

  Methode 1 : selon le nb k de composantes
  P(n,k) = nb de partitions de n en k morceaux
  P(n,k) = P(n-1,k-1)+P(n-k,k)
  (derniere partition valant 1
   + toutes les partitions >=2 donc equivalent a
     partition de n-k en retirant 1 a chaque composante)
  P(n) = sum(P(n,k), k=1..n)

  Methode 2 : selon la valeur max m des composantes
  Q(n,m) = nb de partitions de n en morceaux <=m
  Q(n,m) = sum(Q(n-k,k), k=1..m)
  (Q(n-k,k) est le nb de partitions de n en morceaux <=k avec
   au moins 1 morceau de valeur k)
  P(n) = Q(n,n)

  Mais dans ce cas :
  Q(n,m) = Q(n,m-1)+Q(n-m,m)
  Calculons les Q(.,m) successifs pour des m croissants
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
