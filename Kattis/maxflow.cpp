#include <cstdio>
#include <vector>
#include <queue>
#include <climits>
using namespace std;

typedef int elem;
const elem INF = INT_MAX;

int N;
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

elem binary_residual_dfs(vector<int> &Pred, int s, int t) {
  static int B = 30;  // largest B such that 2^B < expected flow
  while (B>=0) {
    // looking for an augmenting flow >= 2^B
    elem f = residual_dfs(Pred, s, t, 1LL<<B);
    if (f>0) return f;
    else --B;  // otherwise decrement B
  }
  return 0;
}

elem residual_bfs(vector<int> &Pred, int s, int t) {
  Pred.resize(N, -1);
  Pred[s] = s;
  vector<elem> ResF(N, 0);
  ResF[s] = INF;
  queue<int> Q;
  Q.push(s);
  while (!Q.empty()) {
    int u = Q.front();
    if (u==t) break;
    Q.pop();
    for (int v : G[u]) {
      elem Ruv = C[u][v] - F[u][v];  // residual capacity
      if (Ruv>0 && Pred[v]<0) {
	Pred[v] = u;
	ResF[v] = min(ResF[u], Ruv);
	Q.push(v);
      }
    }
  }
  return ResF[t];
}

elem ford_fulkerson(int s, int t) {
  F.resize(N, vector<elem>(N, 0));
  elem flow = 0;
  while (true) {
    vector<int> Pred;
    // classic Ford-Fulkerson in O(n * m * c)
    //elem f = residual_dfs(Pred, s, t);
    // binary optimized Ford-Fulkerson in O(n * m * log c)
    elem f = binary_residual_dfs(Pred, s, t);
    // Edmonds-Karp in O(n * m^2)
    //elem f = residual_bfs(Pred, s, t);
    if (f==0) break;
    flow += f;
    int v = t, u = Pred[t];
    while (u!=v) {
      F[u][v] += f;
      F[v][u] = -F[u][v];
      v = u; u = Pred[v];
    }
  }
  return flow;
}

int main() {
  int M,S,T;
  scanf("%d %d %d %d", &N, &M, &S, &T);
  C.resize(N, vector<elem>(N, 0));
  for (int i=0; i<M; ++i) {
    int u,v;
    elem c;
    scanf("%d %d %d", &u, &v, &c);
    C[u][v] = c;
  }
  // building proper graph (with proper & unique reverse arcs)
  G.resize(N);
  for (int u=0; u<N; ++u)
    for (int v=u+1; v<N; ++v)
      if (C[u][v]>0 || C[v][u]>0) {
	G[u].push_back(v);
	G[v].push_back(u);
      }
  // F-F
  elem f = ford_fulkerson(S, T);
  // output
  vector< pair<int,int> > E;
  for (int u=0; u<N; ++u)
    for (int v=0; v<N; ++v)
      if (F[u][v]>0)
	E.push_back(make_pair(u,v));
  printf("%d %d %d\n", N, f, (int)E.size());
  for (const auto &e : E)
    printf("%d %d %d\n", e.first, e.second, F[e.first][e.second]);
  return 0;
}
