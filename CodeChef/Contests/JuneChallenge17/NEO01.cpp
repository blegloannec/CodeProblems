#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/*
  Les positifs iront necessairement tous ensemble. On essaye de facon gloutonne
  d'y ajouter les negatifs les plus grands possibles (i.e. dans l'ordre
  decroissant) tant que c'est benefique a l'ensemble. Des que ca ne l'est
  plus on s'arrete et on traite tous les negatifs restant comme des singletons.
*/

typedef long long ll;

ll feast(vector<ll> &A) {
  sort(A.begin(),A.end());
  ll s0 = 0, n0 = 0;
  for (int i=A.size()-1; i>=0; --i) {
    if (A[i]>=0 || (n0+1)*(s0+A[i])>=n0*s0+A[i]) {
      s0 += A[i];
      ++n0;
    }
    else {
      ll res = n0*s0;
      for (int j=i; j>=0; --j) res += A[j];
      return res;
    }
  }
  return n0*s0;
}

int main() {
  int T,N;
  cin >> T;
  for (int t=0; t<T; ++t) {
    cin >> N;
    vector<ll> A(N);
    for (int i=0; i<N; ++i) cin >> A[i];
    cout << feast(A) << endl;
  }
  return 0;
}
