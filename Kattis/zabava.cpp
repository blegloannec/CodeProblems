#include <cstdio>
#include <vector>
using namespace std;
using ll = long long;

int N,M,K;
vector<int> B;

ll sum(ll n) {
  return n*(n+1)/2;
}

// minimizing the noise over size n with k cuts
// Ex.: noise(10,3) -> n = 3*(k+1)+1 -> 4|3|3 -> 22
ll noise(int n, int k) {
  ll q = n/(k+1), r = n%(k+1);
  return r*sum(q+1) + (k+1-r)*sum(q);
}

// DP in O(M * K^2)
ll dp() {
  vector<ll> DP(K+1,0);
  for (int m=0; m<M; ++m)
    if (B[m]>0)
      for (int k=K; k>=0; --k) {
	DP[k] += noise(B[m],0);
	for (int km=1; km<=k; ++km)
	  DP[k] = min(DP[k], DP[k-km]+noise(B[m],km));
      }
  return DP[K];
}

int main() {
  scanf("%d %d %d", &N, &M, &K);
  B.resize(M,0);
  for (int i=0; i<N; ++i) {
    int m;
    scanf("%d", &m); --m;
    ++B[m];
  }
  printf("%lld\n", dp());
  return 0;
}
