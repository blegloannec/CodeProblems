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

void _level_bfs(vector<int> &Lvl, int s, int t) {
  //Lvl.resize(N, -1);
  fill(Lvl.begin(), Lvl.end(), -1);
  Lvl[s] = 0;
  queue<int> Q;
  Q.push(s);
  while (!Q.empty()) {
    int u = Q.front();
    if (u==t) break;
    Q.pop();
    for (int v : G[u]) {
      elem Ruv = C[u][v] - F[u][v];  // residual capacity
      if (Ruv>0 && Lvl[v]<0) {
	Lvl[v] = Lvl[u] + 1;
	Q.push(v);
      }
    }
  }
}

elem _dinic_step(vector<int> &Lvl, int u, int t, elem max_flow=INF) {
  if (max_flow<=0) return 0;
  if (u==t) return max_flow;
  elem flow = 0;
  for (int v : G[u])
    if (Lvl[v]==Lvl[u]+1) {
      elem Ruv = C[u][v] - F[u][v];  // current residual flow
      if (Ruv>0) {
	elem f = _dinic_step(Lvl, v, t, min(Ruv, max_flow));
	if (f>0) {
	  flow += f;
	  F[u][v] += f;
	  F[v][u] = -F[u][v];
	  max_flow -= f;
	}
      }
    }
  // if no more flow from u to t, we "remove" u (setting its level to -1)
  // in order to spare any future useless call to u
  if (flow==0) Lvl[u] = -1;
  return flow;
}

elem dinic(int s, int t) {
  F.resize(N, vector<elem>(N, 0));
  vector<int> Lvl(N);
  elem flow = 0;
  while (true) {
    _level_bfs(Lvl, s, t);
    if (Lvl[t]<0) break;
    elem f = _dinic_step(Lvl, s, t);
    flow += f;
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
  // Dinic
  elem f = dinic(S, T);
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
