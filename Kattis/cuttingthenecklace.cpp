#include <cstdio>
#include <vector>
using namespace std;
using ll = long long;

int N,K;
vector<ll> W; 

bool necklace() {
  ll S = 0;
  for (ll w : W) S += w;
  if (S%K!=0) return false;
  ll each = S/K, curr = 0;
  vector<int> Succ(N,-1);
  for (int l=0, r=0; l<N; ++l) {
    while (curr<each) {
      curr += W[r++];
      if (r==N) r = 0;
    }
    if (curr==each) Succ[l] = r;
    curr -= W[l];
  }
  vector<bool> seen(N,false);
  for (int i=0; i<N; ++i)
    if (!seen[i]) {
      seen[i] = true;
      int j = Succ[i];
      while (j>=0 && !seen[j]) {
	seen[j] = true;
	j = Succ[j];
      }
      if (j==i) return true;
    }
  return false;
}

int main() {
  scanf("%d %d", &K, &N);
  W.resize(N);
  for (int i=0; i<N; ++i) scanf("%lld", &W[i]);
  printf(necklace() ? "YES\n" : "NO\n");
  return 0;
}
