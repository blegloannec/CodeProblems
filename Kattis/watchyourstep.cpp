#include <cstdio>
#include <vector>
#include <bitset>
using namespace std;

/* === Strongly Connected Components === */
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
/* === End === */


const int CMAX = 2500;
int C;
vector< bitset<CMAX> > CompDAG;
vector<int> Size, ReachCnt;

int reachable(int u) {
  if (ReachCnt[u]<0) {
    bitset<CMAX> V = CompDAG[u];
    for (int v=0; v<C; ++v)
      if (V[v]) {
	reachable(v);
	CompDAG[u] |= CompDAG[v];
      }
    ReachCnt[u] = Size[u];
    for (int v=0; v<C; ++v)
      if (CompDAG[u][v])
	ReachCnt[u] += Size[v];
  }
  return ReachCnt[u];
}

int main() {
  int N, M = 0;
  scanf("%d", &N);
  graph G(N);
  for (int i=0; i<N; ++i)
    for (int j=0; j<N; ++j) {
      int e;
      scanf("%d", &e);
      if (e) {
	G[i].push_back(j);
	++M;
      }
    }
  vector<int> Compo;
  C = strongly_connected_components(G, Compo);
  Size.resize(C,0);
  for (int c : Compo) ++Size[c];
  CompDAG.resize(C);
  for (int u=0; u<N; ++u)
    for (int v : G[u])
      if (Compo[u]!=Compo[v])
	CompDAG[Compo[u]][Compo[v]] = true;
  ReachCnt.resize(C,-1);
  int res = -M;
  for (int c=0; c<C; ++c)
    res += Size[c]*(reachable(c)-1);
  printf("%d\n", res);
  return 0;
}
