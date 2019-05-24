/*
  That's a Max-Cut problem https://en.wikipedia.org/wiki/Maximum_cut
  This is NP-hard, yet here we only need a good enough approximation.
  Lots of randomized approaches can pass, however there even exists a
  simple deterministic greedy approach in O(n+m):
  https://algorithmist.com/index.php/UVa_10982
*/
#include <iostream>
#include <vector>
using namespace std;

int N, S;
vector< vector<int> > G;
vector<bool> Subset;

int greedy_maxcut() {
  S = 0;
  Subset.resize(N);
  int res = 0;
  for (int u=0; u<N; ++u) {
    int v0 = 0, v1 = 0;
    for (int v : G[u])
      if (v<u) {
	if (Subset[v]) ++v0;
	else ++v1;
      }
    if (v0>v1) {
      Subset[u] = false;
      res += v1;
    }
    else {
      ++S;
      Subset[u] = true;
      res += v0;
    }
  }
  return res;
}

int main() {
  int T;
  cin >> T;
  for (int t=1; t<=T; ++t) {
    int M;
    cin >> N >> M;
    G.resize(N);
    for (int i=0; i<M; ++i) {
      int u,v;
      cin >> u >> v; --u; --v;
      G[u].push_back(v);
      G[v].push_back(u);
    }
    int res = greedy_maxcut();
    if (2*res>M)
      cout << "Case #" << t << ": Impossible" << endl;
    else {
      cout << "Case #" << t << ": " << S << endl;
      bool first = true;
      for (int u=0; u<N; ++u)
	if (Subset[u]) {
	  if (first) first = false;
	  else cout << ' ';
	  cout << u+1;
	}
      cout << endl;
    }
    // cleaning
    G.clear();
  }
  return 0;
}
