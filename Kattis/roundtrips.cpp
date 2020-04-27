/*
  Number of edges one can add to a digraph without creating any new cycle.
  Clearly no edge can be added within any strongly connected component.
  Consider an arbitrary topological ordering of the connected components,
  one can add as many edges as one wants between connected components
  provided that they respect the topological ordering.
*/
#include <cstdio>
#include <vector>
using namespace std;
using ll = long long;

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

int main() {
  int n,m;
  scanf("%d %d", &n, &m);
  graph G(n);
  for (int i=0; i<m; ++i) {
    int u,v;
    scanf("%d %d", &u, &v);
    G[u].push_back(v);
  }
  vector<int> compo;
  int C = strongly_connected_components(G, compo);
  vector<int> comp_size(C, 0);
  int between_comp = 0;
  for (int u=0; u<n; ++u) {
    ++comp_size[compo[u]];
    for (int v : G[u])
      if (compo[u]!=compo[v]) ++between_comp;
  }
  // "undirected" edges (as for each such edge, there is exactly one valid
  // direction to add) - existing edges between components
  ll edges = n*(n-1LL)/2LL - between_comp;
  // remove the edges within components
  for (int c=0; c<C; ++c)
    edges -= comp_size[c]*(comp_size[c]-1LL)/2LL;
  printf("%lld\n", edges);
  return 0;
}
