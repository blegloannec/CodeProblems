// NWERC 2008
// 4287 on archive, 12167 on UVa

#include <iostream>
#include <vector>
using namespace std;

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
  int c;
  cin >> c;
  while (c-->0) {
    int n,m;
    cin >> n >> m;
    graph G(n);
    for (int i=0; i<m; ++i) {
      int a,b;
      cin >> a >> b; --a; --b;
      G[a].push_back(b);
    }
    vector<int> compo;
    int C = strongly_connected_components(G,compo);
    if (C==1) {
      cout << 0 << endl;
      continue;
    }
    vector<bool> source(C,true), sink(C,true);
    int nb_source = C, nb_sink = C;
    for (int u=0; u<n; ++u)
      for (auto iv=G[u].begin(); iv!=G[u].end(); ++iv)
	if (compo[u]!=compo[*iv]) {
	  if (sink[compo[u]]) {
	    sink[compo[u]] = false;
	    --nb_sink;
	  }
	  if (source[compo[*iv]]) {
	    source[compo[*iv]] = false;
	    --nb_source;
	  }
	}
    cout << max(nb_source,nb_sink) << endl;
  }
  return 0;
}
