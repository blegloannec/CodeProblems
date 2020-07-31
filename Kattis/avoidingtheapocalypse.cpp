/*
  Ford-Fulkerson in the time-layered graph
  where vertices are (original vertex, time)
*/
#include <iostream>
#include <vector>
using namespace std;

typedef char elem;
const elem INF = 127;
typedef pair<int,int> edge;
#define _v_ first
#define _e_ second

int N,E;
vector< vector<edge> > G;
vector<elem> C, F;
// G the adjacency lists graph (with reverse arcs!)
// C the edges capacity list
// F the edge flow list
vector<int> ArcU, ArcV, ArcRev;

void add_arc(int u, int v, elem c) {
  ArcU.push_back(u);
  ArcV.push_back(v);
  C.push_back(c);
  G[u].push_back(make_pair(v, E++));
  ArcV.push_back(u);
  ArcU.push_back(v);
  C.push_back(0);
  G[v].push_back(make_pair(u, E++));
  ArcRev.push_back(E-1);
  ArcRev.push_back(E-2);
}

elem _residual_dfs(vector<int> &PredE, int u, int t) {
  if (u==t) return INF;
  for (const edge &ve : G[u]) {
    int v = ve._v_, e = ve._e_;
    elem Ruv = C[e] - F[e];  // residual capacity
    if (Ruv>0 && PredE[v]<0) {
      PredE[v] = e;
      elem f = _residual_dfs(PredE, v, t);
      if (f>0) return min(f, Ruv);
    }
  }
  return 0;
}

elem ford_fulkerson(int s, int t) {
  F.resize(E, 0);
  elem flow = 0;
  while (true) {
    vector<int> PredE(N, -1);
    PredE[s] = E;
    // classic Ford-Fulkerson in O(n * m * c)
    elem f = _residual_dfs(PredE, s, t);
    if (f==0) break;
    flow += f;
    int v = t, e = PredE[t];
    while (v!=s) {
      F[e] += f;
      F[ArcRev[e]] = -F[e];
      v = ArcU[e]; e = PredE[v];
    }
  }
  return flow;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    int n,u0,g,S,m,r;
    cin >> n;
    cin >> u0 >> g >> S; --u0;
    cin >> m;
    vector<int> M(m);
    for (int i=0; i<m; ++i) {
      cin >> M[i]; --M[i];
    }
    cin >> r;
    N = (S+1)*n+2;
    G.resize(N);
    E = 0;
    // vertex (u,t) index
    auto idx = [n](int u, int t) { return 1+t*n+u; };
    for (int i=0; i<r; ++i) {
      int u,v,p,t;
      cin >> u >> v >> p >> t; --u; --v;
      for (int s=0; s+t<=S; ++s)
	add_arc(idx(u,s), idx(v,s+t), p);
    }
    // arcs (u,t) -> (u,t+1)
    for (int u=0; u<n; ++u)
      for (int s=0; s<S; ++s)
	add_arc(idx(u,s), idx(u,s+1), g);
    // arc source -> (u0,0)
    add_arc(0, idx(u0,0), g);
    // arcs (exit, final time) -> sink
    for (int u : M) add_arc(idx(u,S), N-1, g);
    cout << (int)ford_fulkerson(0, N-1) << endl;
    // cleaning
    G.clear();
    C.clear(); F.clear();
    ArcU.clear(); ArcV.clear(); ArcRev.clear();
  }
  return 0;
}
