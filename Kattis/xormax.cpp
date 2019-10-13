/*
  Gaussian elimination
  https://www.geeksforgeeks.org/find-maximum-subset-xor-given-set/
*/
#include <cstdio>
#include <vector>
using namespace std;
using ll = long long;

int N;
vector<ll> A;

ll max_xor_subset() {
  int bit = 60, idx = 0;
  while (bit>=0 && idx<N) {
    int imax = idx;
    for (int i=idx; i<N; ++i)
      if (A[i]>A[imax])
	imax = i;
    ll Amax = A[imax];
    while (bit>=0 && ((Amax>>bit)&1)==0) --bit;
    if (bit>=0) {
      swap(A[idx],A[imax]);
      for (int i=0; i<N; ++i)
	if (i!=idx && (A[i]>>bit)&1)
	  A[i] ^= Amax;
      ++idx;
      --bit;
    }
  }
  ll res = 0;
  for (int i=0; i<N; ++i) res ^= A[i];
  return res;
}

int main() {
  scanf("%d", &N);
  A.resize(N);
  for (int i=0; i<N; ++i) scanf("%lld", &A[i]);
  printf("%lld\n", max_xor_subset());
  return 0;
}
