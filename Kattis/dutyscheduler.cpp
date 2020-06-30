#include <iostream>
#include <vector>
#include <climits>
using namespace std;

typedef int elem;
const elem INF = INT_MAX;

int m,n,N;
vector< vector<int> > G;
vector< vector<elem> > C, F;
// G the adjacency lists graph (with reverse arcs!)
// C the capacity matrix
// F the flow matrix (anti-symmetric)

elem _residual_dfs(vector<int> &Pred, int u, int t, elem min_flow=1) {
  if (u==t) return INF;
  for (int v : G[u]) {
    elem Ruv = C[u][v] - F[u][v];  // residual capacity
    if (Ruv>=min_flow && Pred[v]<0) {
      Pred[v] = u;
      elem f = _residual_dfs(Pred, v, t, min_flow);
      if (f>0) return min(f, Ruv);
    }
  }
  return 0;
}

// (re)init. Pred  +  _residual_dfs
elem residual_dfs(vector<int> &Pred, int s, int t, elem min_flow=1) {
  Pred.resize(N);
  fill(Pred.begin(), Pred.end(), -1);
  Pred[s] = s;
  return _residual_dfs(Pred, s, t, min_flow);
}

elem ford_fulkerson(int s, int t) {
  F.clear();
  F.resize(N, vector<elem>(N, 0));
  while (true) {
    vector<int> Pred;
    // classic Ford-Fulkerson in O(n * m * c)
    elem f = residual_dfs(Pred, s, t);
    if (f==0) break;
    int v = t, u = Pred[t];
    while (u!=v) {
      F[u][v] += f;
      F[v][u] = -F[u][v];
      v = u; u = Pred[v];
    }
  }
  // computing flow
  elem f = 0;
  for (int v : G[s]) f += F[s][v];
  return f;
}

void init_source(int k) {
  for (int i=1; i<=m; ++i) C[0][i] = k;
}

int main() {
  cin >> m >> n;
  N = m+n+2;
  C.resize(N, vector<elem>(N, 0));
  vector<string> Name(m+1);
  for (int i=1; i<=m; ++i) {
    int D;
    cin >> Name[i] >> D;
    for (int j=0; j<D; ++j) {
      int d;
      cin >> d;
      C[i][m+d] = 1;
    }
  }
  int K = 1;
  init_source(K);
  for (int d=1; d<=n; ++d) C[m+d][N-1] = 2;
  // building proper graph (with proper & unique reverse arcs)
  G.resize(N);
  for (int u=0; u<N; ++u)
    for (int v=u+1; v<N; ++v)
      if (C[u][v]>0 || C[v][u]>0) {
	G[u].push_back(v);
	G[v].push_back(u);
      }
  // F-F
  while (ford_fulkerson(0, N-1)<2*n)
    init_source(++K);
  cout << K << endl;
  for (int d=1; d<=n; ++d) {
    cout << "Day " << d << ":";
    for (int i=1; i<=m; ++i)
      if (F[i][m+d]>0)
	cout << ' ' << Name[i];
    cout << endl;
  }
  return 0;
}
