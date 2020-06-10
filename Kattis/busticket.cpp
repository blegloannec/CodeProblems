#include <cstdio>
#include <vector>
using namespace std;
using ll = long long;

int main() {
  ll S,P; int M,N;
  scanf("%lld %lld %d %d", &S, &P, &M, &N);
  vector<int> T(N+1);
  for (int i=1; i<=N; ++i) scanf("%d", &T[i]);
  vector<ll> DP(N+1);
  DP[0] = 0LL;
  for (int i=1, l=1; i<=N; ++i) {
    while (l<i && T[i]-T[l]>=M) ++l;
    DP[i] = min(DP[i-1]+S, DP[l-1]+P);
  }
  printf("%lld\n", DP.back());
  return 0;
}
