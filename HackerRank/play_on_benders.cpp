#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int N;
vector< vector<int> > DAG;
vector<int> G;

int grundy(int u) {
  if (G[u]<0) {
    vector<int> V;
    for (int v : DAG[u]) V.push_back(grundy(v));
    // compute g = mex(V)
    sort(V.begin(),V.end());
    auto last = unique(V.begin(),V.end());
    V.resize(distance(V.begin(),last));
    int g = 0;
    while (g<(int)V.size() && g==V[g]) ++g;
    G[u] = g;
  }
  return G[u];
}

int main() {
  int M, Q;
  scanf("%d %d", &N, &M);
  DAG.resize(N);
  for (int i=0; i<M; ++i) {
    int u, v;
    scanf("%d %d", &u, &v); --u; --v;
    DAG[u].push_back(v);
  }
  G.resize(N,-1);
  for (int u=0; u<N; ++u) grundy(u);
  scanf("%d", &Q);
  for (int i=0; i<Q; ++i) {
    int K, g = 0;
    scanf("%d", &K);
    for (int j=0; j<K; ++j) {
      int b;
      scanf("%d", &b); --b;
      g ^= grundy(b);
    }
    printf(g==0 ? "Iroh\n" : "Bumi\n");
  }
  return 0;
}
