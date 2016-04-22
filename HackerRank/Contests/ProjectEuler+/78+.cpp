#include <iostream>
using namespace std;

const int M = 60001;
long long P[M];

/* calcul en O(m*sqrt(m)) via formule d'Euler pour les partitions */
void precomp() {
  P[0] = 1;
  P[1] = 1;
  for (int n=2; n<M; ++n) P[n] = 0;
  for (int n=2; n<M; ++n) {
    for (int k=1; k*(3*k-1)/2<=n; ++k) {
      if (k*(3*k+1)/2<=n)
	P[n] = (P[n]+((k+1)%2==0?1:-1)*(P[n-k*(3*k+1)/2]+P[n-k*(3*k-1)/2]))%1000000007;
      else P[n] = (P[n]+((k+1)%2==0?1:-1)*P[n-k*(3*k-1)/2])%1000000007;
    }
    if (P[n]<0) P[n] = (P[n]+1000000007)%1000000007;
  }
}

int main() {
  int T,N;
  precomp();
  cin >> T;
  for (int t=0; t<T; ++t) {
    cin >> N;
    cout << P[N] << endl;
  } 
  return 0;
}
