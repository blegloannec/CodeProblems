/*
  That's a Max-Cut problem https://en.wikipedia.org/wiki/Maximum_cut
  This is NP-hard, yet here we only need a good enough approximation.
  Lots of randomized approaches can pass, however there even exists a
  simple deterministic greedy approach in O(n+m).
  https://algorithmist.com/index.php/UVa_10982
  
  Let us build a partition into two subsets A and B.
  We will treat the vertices in an arbitrary order (e.g. their number).
  For each vertex u, consider the set E(u) of edges (u,v) such
  that v has already been considered before u (e.g. v<u), and consequently
  already been assigned to one of the two subsets.
  If the majority of vertices in E(u) are in A/B, assign u to B/A.
  This guaranties that we cut at least |E(u)|/2 edges.
  As the E(u) form a partition of the set of edges, this greedy
  algorithm is guaranteed to cut at least half the edges (which is
  consequently always possible, the "Impossible" output never happens).
*/
#include <iostream>
#include <vector>
using namespace std;

int N;
vector< vector<int> > E;

void greedy_maxcut_approx(vector<bool> &Subset) {
  for (int u=0; u<N; ++u) {
    int V[] = {0,0};
    for (int v : E[u]) ++V[Subset[v]];
    Subset[u] = V[1]<V[0];
  }
}

int main() {
  int T;
  cin >> T;
  for (int t=1; t<=T; ++t) {
    int M;
    cin >> N >> M;
    E.resize(N);
    for (int i=0; i<M; ++i) {
      int u,v;
      cin >> u >> v; --u; --v;
      if (u<v) swap(u,v);
      E[u].push_back(v);  // we only set the properly ordered edge
    }
    vector<bool> Subset(N);
    greedy_maxcut_approx(Subset);
    vector<int> Sol;
    for (int u=0; u<N; ++u)
      if (Subset[u]) Sol.push_back(u+1);
    int s = Sol.size();
    cout << "Case #" << t << ": " << s << endl;
    for (int i=0; i<s; ++i)
      cout << Sol[i] << (i==s-1 ? '\n' : ' ');
    // cleaning
    E.clear();
  }
  return 0;
}
