#include <cstdio>
using namespace std;
using ll = long long;

const ll P = 1000000007;
const int NMAX = 1202;

int N;
ll S[NMAX], F[NMAX], B[NMAX][NMAX], DP[NMAX][NMAX];

// O(N^3) DP with N ~ 10^3 but a reasonably small constant factor
void dp() {
  for (int i=0; i<=N; ++i)
    for (int j=0; j<=N; ++j)
      DP[i][j] = 0;
  // DP[i][k] = number of ways to produce V[i...] starting with k arrays
  DP[N][0] = 1;
  for (int i=N-1; i>=0; --i)
    for (int j=i; j<N; ++j) {
      if (j>i && S[j-1]>S[j]) break;
      // V[i..j] is non-decreasing
      int k = j-i+1;
      DP[i][k] = DP[j+1][0];
      for (int l=1; l<=k && DP[j+1][l]>0; ++l)
	DP[i][k] = (DP[i][k] + ((B[k][l] * ((F[l] * DP[j+1][l]) % P)) % P)) % P;
    }
}

int main() {
  // factorial mod
  F[0] = 1;
  for (int n=1; n<NMAX; ++n)
    F[n] = (n*F[n-1]) % P;
  // binomial mod
  B[0][0] = 1;
  for (int n=1; n<NMAX; ++n) {
    B[n][0] = B[n][n] = 1;
    for (int p=1; p<n; ++p)
      B[n][p] = (B[n-1][p-1] + B[n-1][p]) % P;
  }
  // main
  scanf("%d", &N);
  for (int i=0; i<N; ++i) scanf("%lld", &S[i]);
  dp();
  ll res = 0;
  for (ll v : DP[0]) res = (res + v) % P;
  printf("%lld\n", res);
  return 0;
}
