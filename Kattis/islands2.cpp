#include <cstdio>
#include <vector>
#include <cmath>
using namespace std;
using ll = long long;

#define SQR(X) ((X)*(X))

bool pt_in_circ(ll x, ll y, ll xc, ll yc, ll rc) {
  return SQR(x-xc)+SQR(y-yc) < SQR(rc);
}

bool circ_intersect(ll x1, ll y1, ll r1, ll x2, ll y2, ll r2) {
  return SQR(x1-x2)+SQR(y1-y2) <= SQR(r1+r2);
}

double tunnel(ll x1, ll y1, ll r1, ll x2, ll y2, ll r2) {
  return sqrt(SQR(x1-x2)+SQR(y1-y2)) - (r1+r2) + 200.;
}


/* ===== SCC ===== */
typedef vector< vector<int> > graph;

void reverse_graph(graph &G, graph &R) {
  R.resize(G.size());
  for (unsigned int u=0; u<G.size(); ++u)
    for (vector<int>::iterator it=G[u].begin(); it!=G[u].end(); ++it)
      R[*it].push_back(u);
}

void dfs_topo(graph &G, int u, vector<bool> &seen, vector<int> &topo) {
  if (seen[u]) return;
  seen[u] = true;
  for (vector<int>::iterator it=G[u].begin(); it!=G[u].end(); ++it)
    dfs_topo(G,*it,seen,topo);
  topo.push_back(u);
}

void dfs_compo(graph &G, int u, int c, vector<int> &compo) {
  if (compo[u]>=0) return;
  compo[u] = c;
  for (vector<int>::iterator it=G[u].begin(); it!=G[u].end(); ++it)
    dfs_compo(G,*it,c,compo);
}

int strongly_connected_components(graph &G, vector<int> &compo) {
  int N = G.size();
  vector<bool> seen(N,false);
  vector<int> topo;
  for (int u=0; u<N; ++u) dfs_topo(G,u,seen,topo);
  graph R;
  reverse_graph(G,R);
  compo.resize(N,-1);
  int c = 0;
  for (int i=N-1; i>=0; --i)
    if (compo[topo[i]]<0) {
      dfs_compo(R,topo[i],c,compo);
      ++c;
    }
  return c;
}
/* ===== ===== */


int main() {
  int N,M; ll K;
  scanf("%d %d %lld", &N, &M, &K);
  vector<ll> IX(N),IY(N),IR(N);
  for (int i=0; i<N; ++i)
    scanf("%lld %lld %lld", &IX[i], &IY[i], &IR[i]);
  vector<ll> PX(M),PY(M),PR(M);
  for (int j=0; j<M; ++j) {
    scanf("%lld %lld %lld", &PX[j], &PY[j], &PR[j]);
    PR[j] *= K;
  }
  // building islands directed graph
  graph G(N);
  { // building islands graph matrix
    // (to avoid a possibly significant number of duplicated edges)
    vector< vector<bool> > E(N, vector<bool>(N, false));
    for (int j=0; j<M; ++j) {
      int i0 = -1;
      vector<int> I;
      for (int i=0; i<N; ++i) {
	if (i0<0 && pt_in_circ(PX[j],PY[j], IX[i],IY[i],IR[i]))
	  i0 = i;
	else if ((i0<0 || !E[i0][i]) && circ_intersect(PX[j],PY[j],PR[j], IX[i],IY[i],IR[i]))
	  I.push_back(i);
      }
      for (int i : I) E[i0][i] = true;
    }
    for (int u=0; u<N; ++u)
      for (int v=0; v<N; ++v)
	if (E[u][v]) G[u].push_back(v);
  }
  // computed connected components
  vector<int> Comp;
  int C = strongly_connected_components(G, Comp);
  // computing tunnel
  if (C==1) printf("0\n");  // 1 component, tunnel not required
  else if (C==2) {  // 2 components, computing the best tunnel between
    double d = 1e12;
    for (int u=0; u<N; ++u)
      for (int v=u+1; v<N; ++v)
	if (Comp[u]!=Comp[v])
	  d = min(d, tunnel(IX[u],IY[u],IR[u], IX[v],IY[v],IR[v]));
    printf("%.6lf\n", d);
  }
  else {  // more components
    // identifying sources and sinks
    vector<bool> Source(C, true), Sink(C, true);
    for (int u=0; u<N; ++u)
      for (int v : G[u])
	if (Comp[u]!=Comp[v]) {
	  Sink[Comp[u]] = false;
	  Source[Comp[v]] = false;
	}
    int c0 = -1, cf = -1;
    bool unique = true;
    for (int c=0; c<C && unique; ++c) {
      if (Source[c]) {
	if (c0<0) c0 = c;
	else unique = false;
      }
      if (Sink[c]) {
	if (cf<0) cf = c;
	else unique = false;
      }
    }
    if (!unique) printf("impossible\n");
    else {  // 1 source, 1 sink, computing the best tunnel between
      double d = 1e12;
      for (int u=0; u<N; ++u)
	if (Comp[u]==c0)
	  for (int v=0; v<N; ++v)
	    if (Comp[v]==cf)
	      d = min(d, tunnel(IX[u],IY[u],IR[u], IX[v],IY[v],IR[v]));
      printf("%.6lf\n", d);
    }
  }
  return 0;
}
