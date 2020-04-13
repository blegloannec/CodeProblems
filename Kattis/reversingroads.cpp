#include <iostream>
#include <vector>
using namespace std;

typedef pair<int,int> edge;
typedef vector<edge> edges;

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

int strongly_connected_components(graph &G, vector<int> &compo, bool connectedness=false) {
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
      if (connectedness && c>1) break;  // only checking connectedness
    }
  return c;
}

graph build_graph(int n, const edges &E) {
  graph G(n);
  for (const auto &e : E)
    G[e.first].push_back(e.second);
  return G;
}

int main() {
  int n, m, t = 1;
  while (cin >> n >> m) {
    edges E;
    for (int i=0; i<m; ++i) {
      int a,b;
      cin >> a >> b;
      E.push_back(make_pair(a,b));
    }
    graph G = build_graph(n, E);
    vector<int> compo;
    int C = strongly_connected_components(G,compo);
    cout << "Case " << t++ << ": ";
    if (C==1) {
      cout << "valid" << endl;
      continue;
    }
    bool invalid = true;
    for (int i=0; i<m && invalid; ++i) {
      if (compo[E[i].first]!=compo[E[i].second]) {  // small useless optim.
	swap(E[i].first, E[i].second);
	G = build_graph(n, E);
	vector<int> compo0;
	C = strongly_connected_components(G, compo0, true);
	swap(E[i].first, E[i].second);
	if (C==1) {
	  cout << E[i].first << " " << E[i].second << endl;
	  invalid = false;
	}
      }
    }
    if (invalid) cout << "invalid" << endl;
  }
  return 0;
}
