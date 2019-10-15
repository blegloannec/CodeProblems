#include <cstdio>
#include <vector>
using namespace std;
using ll = long long;

int N,K;
vector<ll> A;

/*
  /!\ "The subarrays are required to be disjoint.
       A subarray may end at index i and another subarray start at index i+1.
       No subarray is allowed to be empty."
*/

ll max_k_sub() {
  ll S = 0;
  vector<ll> Overall(K+1,0), Current(K+1,0);
  for (int i=0; i<N; ++i) {
    if (i+1<=K) {  // /!\ Init.
      S += A[i];
      Current[i+1] = S;
      Overall[i+1] = S;
    }
    for (int k=min(i,K); k>0; --k) {
      Current[k] = max(Overall[k-1]+A[i], Current[k]+A[i]);
      Overall[k] = max(Overall[k], Current[k]);
    }
  }
  return Overall[K];
}

int main() {
  scanf("%d %d", &N, &K);
  A.resize(N);
  for (int i=0; i<N; ++i) scanf("%lld", &A[i]);
  printf("%lld\n", max_k_sub());
  return 0;
}
