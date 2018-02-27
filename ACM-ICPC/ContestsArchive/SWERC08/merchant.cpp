#include <iostream>
using namespace std;

typedef long long ent;

const int NMAX = 301;
int n,m;
ent M;
int C[NMAX];
ent B[NMAX][NMAX], memo[NMAX][NMAX];

bool valid() {
  for (int i=n-1; i>=0; --i)
    if (C[i]>n-i) return false;
  return true;
}

void precomp_binom() {
  B[0][0] = 1;
  for (int i=1; i<=n-m; ++i) {
    B[i][0] = 1;
    for (int j=1; j<=i; ++j)
      B[i][j] = (B[i-1][j-1]+B[i-1][j]) % M;
  }
}

void init_memo() {
  for (int i=0; i<=n; ++i)
    for (int j=0; j<=n-m; ++j)
      memo[i][j] = -1;
  memo[n][0] = 1;
  for (int j=1; j<=n-m; ++j)
    memo[n][j] = 0;
}

// affectations de k marchands etrangers aux emplacements 0<=i,...,n-1
ent dp(int i, int k) {
  if (memo[i][k]>=0) return memo[i][k];
  ent res = 0;
  int f = n-i-C[i]; // places libres
  if (k<=f)
    for (int a=0; a<=k; ++a) // marchands envoyes en i
      res = (res + B[k][a]*dp(i+1,k-a)) % M;
  memo[i][k] = res;
  return res;
}

int main() {
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    cin >> n >> m >> M;
    for (int i=0; i<n; ++i) C[i] = 0;
    for (int i=0; i<m; ++i) {
      int a,b;
      cin >> a >> b;
      ++C[b-1];
    }
    for (int i=n-2; i>=0; --i) C[i] += C[i+1];
    if (!valid()) cout << "NO" << endl;
    else {
      precomp_binom();
      init_memo();
      cout << "YES " << dp(0,n-m) << endl;
    }
  }
  return 0;
}
