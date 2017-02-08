#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

/*
  Tentatives d'approches de type analyse numerique (Newton, etc)
  restees sans success ici...
  Comme 10000 = 50*200, on peut aussi conjecturer que la solution est
  "proche" de 50 fois la solution de l'enonce (ce qui est +/- vrai et
  donne une bonne idee de la taille des nombres de la solution).
  Au pire, il y avait la borne exp(k/n)-1 < pi soit k < n*ln(pi+1) ~ 14211.
  On procede par approche une plus combinatoire facon "meet in the middle".
  runs in 17s with -O3
*/

struct triple {
  double x;
  int a,b;
  triple(double x, int a, int b) : x(x), a(a), b(b) {}
  bool operator <(const triple &T) const {
    return (x<T.x)||(x==T.x && a<T.a)||(x==T.x && a==T.a && b<T.b);
  }
};

const double n = 10000.;
const int K = 12000; // borne

double f(double x) {
  return exp(x/n)-1.;
}

int main() {
  vector<triple> L;
  // on pre-calcule les sommes des paires
  for (int a=1; a<K; ++a)
    for (int b=a; b<K; ++b) {
      double x = f(a)+f(b);
      if (x<M_PI) L.push_back(triple(x,a,b));
    }
  // on trie
  sort(L.begin(),L.end());
  // exploration en O(n) pour le meet in the middle
  // (initialement en O(n*log(n)) par recherche dicho
  //  du second couple optimal pour chaque couple)
  double emin = 1.;
  int i=0,j=L.size()-1,i0=0,j0=0;
  while (i<=j) {
    double e = L[i].x+L[j].x-M_PI;
    while (i<=j && e>0) {
      --j;
      e = L[i].x+L[j].x-M_PI;
    }
    // plus grand j pour lequel L[i]+L[j] < pi
    e = -e;
    if (L[i].b<=L[j].a && e<emin) {
      emin = e;
      i0 = i; j0 = j;
    }
    // plus petit j pour lequel L[i]+L[j] > pi
    e = L[i].x+L[j+1].x-M_PI;
    if (L[i].b<=L[j+1].a && e<emin) {
      emin = e;
      i0 = i; j0 = j+1;
    }
    ++i;
  }
  cout << L[i0].a << ' ' << L[i0].b << ' ' << L[j0].a << ' ' << L[j0].b << endl;
  cout << L[i0].a*L[i0].a + L[i0].b*L[i0].b + L[j0].a*L[j0].a + L[j0].b*L[j0].b << endl;
  return 0;
}
