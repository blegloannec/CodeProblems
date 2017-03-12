#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

typedef unsigned long long ll;

/*
  on calcule la sequence des "fractures", i.e. des indices
  auxquels la sequence change de valeur (pour passer a la
  valeur courante + 1)
  pour 10^6 on ne peut pas tout stocker, donc on ne stocke
  que le "debut" qui sera suffisant pour tout enumerer

  runs in < 4min with -O3
  must have missed something here...
*/

int main() {
  ll N = 1000000;
  vector<int> G = {0,1,2};
  ll L = 4, S = 1, iS = 2;
  ll iS3 = iS*iS*iS;
  int i0 = 2, i = 3;
  while (iS<N) {
    if (G.size()<100000000) // inutile de stocker au dela
      G.push_back(L);
    while (iS<N && iS3<L) {
      S += i-1;
      ++iS;
      iS3 = iS*iS*iS;
    }
    //assert(i0+1<(int)G.size()); // sinon augmenter la borne de taille
    if (G[i0+1]==i) ++i0;
    L += i0;
    ++i;
  }
  cout << S << endl;
  return 0;
}
