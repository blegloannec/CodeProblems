#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

const int N = (int)sqrt(1000000000)+1;
vector<bool> P(N,true);

void sieve() {
  P[0] = P[1] = false;
  for (int i=2; i*i<N; ++i)
    if (P[i])
      for (int k=2*i; k<N; k+=i)
	P[k] = false;
}

// crible pour marquer les nb composes L <= n <= R
vector<bool> prime_int(int L, int R) {
  int S = (int)sqrt(R);
  vector<bool> D(R-L+1,true);
  for (int p=2; p<=S; ++p)
    if (P[p])
      for (int n=max(2,(L+p-1)/p)*p; n<R+1; n+=p)
	D[n-L] = false;
  return D;
}

int main() {
  int T,m,n;
  sieve();
  cin >> T;
  for (int t=0; t<T; ++t) {
    cin >> m >> n;
    vector<bool> D = prime_int(m,n);
    for (int i=m; i<=n; ++i)
      if (i>1 && D[i-m]) cout << i << endl;
    cout << endl;
  }
  return 0;
}
