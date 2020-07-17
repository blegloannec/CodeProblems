#include <iostream>
#include <vector>
using namespace std;

const int N = 36;
typedef long long mask;
const mask full = (1LL<<N)-1LL;

vector<mask> G(N);
int best;

int ones(mask m) {
  int o = 0;
  while (m>0) {
    if (m&1) ++o;
    m >>= 1;
  }
  return o;
}

void backtrack(int i=0, mask a=0, int oa=0, mask b=full) {
  int ob = ones(b);
  best = max(best, min(oa, ob));
  if (i<N && oa<ob && ob>best && oa+N-i>best) {
    backtrack(i+1, a|(1LL<<i), oa+1, b&G[i]);
    backtrack(i+1, a, oa, b);
  }
}

int main() {
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    int M;
    cin >> M;
    fill(G.begin(), G.end(), 0LL);
    for (int i=0; i<M; ++i) {
      int u,v;
      cin >> u >> v; --u; --v;
      G[u] |= 1LL<<v;
    }
    best = 0;
    backtrack();
    cout << best << endl;
  }
  return 0;
}
