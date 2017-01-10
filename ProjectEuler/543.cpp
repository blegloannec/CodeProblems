#include <iostream>
#include <vector>
using namespace std;

/*
  https://en.wikipedia.org/wiki/Goldbach%27s_conjecture
  https://en.wikipedia.org/wiki/Goldbach%27s_weak_conjecture
  dans les bornes donnes, les conjectures sont vraies (et la weak
  a ete prouvee en 2013).
  donc :
   - tout entier >5 est somme de 3 premiers
   - tout entier pair >2 est somme de 2 premiers
  on en deduit que tout entier >5+2k est somme de 3+k premiers
  reste le cas des entiers impairs x somme de 2 premiers, alors l'un des
  deux doit etre pair, donc 2, et donc il faut x-2 premier.
*/

const int N = 710000000;
const int FI = 45;
vector<bool> P(N,true);
vector<int> F;

void sieve() {
  P[0] = P[1] = false;
  for (int i=2; i*i<N; ++i)
    if (P[i])
      for (int k=2*i; k<N; k+=i)
	P[k] = false;
}

int main() {
  sieve();
  F.push_back(0);
  F.push_back(1);
  for (int i=2; i<FI; ++i)
    F.push_back(F[F.size()-1]+F[F.size()-2]);
  long long S = 1; // pour 2
  long long res = 1; //pour 2
  int fi = 4; // on commence a F = 3
  int i = 3;
  // calcul des k <= 2
  while (fi<FI) {
    if (P[i]) ++S; // k = 1
    if (i%2==0 || P[i-2]) ++S; // k = 2
    if (i==F[fi]) {
      res += S;
      ++fi;
    }
    ++i;
  }
  // calcul des k >= 3, on commence a F = 8
  for (int i=6; i<FI; ++i) {
    long long k = (F[i]-1)/2;
    res += F[i]*(k-1)-(k-2+1)*(k+2+1);
  }
  cout << res << endl;
  return 0;
}
