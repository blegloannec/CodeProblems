#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
using ll = long long;

// slightly overrated (hard 70pt) for a not-so-tricky binary search based pb

int N;
vector<ll> A,S;

ll sum_abs(ll x) {
  int i = distance(A.begin(),lower_bound(A.begin(),A.end(),-x));
  ll S0 = i>0 ? S[i-1] : 0;
  return -(S0+i*x) + S.back()-S0+(N-i)*x;
}

int main() {
  scanf("%d",&N);
  A.resize(N);
  for (int i=0; i<N; ++i) scanf("%lld",&A[i]);
  sort(A.begin(),A.end());
  S = A;
  for (int i=1; i<N; ++i) S[i] += S[i-1];
  int Q;
  scanf("%d",&Q);
  ll x = 0;
  for (int q=0; q<Q; ++q) {
    int dx;
    scanf("%d",&dx);
    x += dx;
    printf("%lld\n",sum_abs(x));
  }
  return 0;
}
