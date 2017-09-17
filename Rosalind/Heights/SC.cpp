#include <iostream>
#include <vector>
using namespace std;

/*
  On construit le DAG des composantes connexes, si le graphe est semi-connexe
  alors ce DAG doit avoir une unique composante source (sinon elles seraient
  inaccessibles entre-elles) et cette propriete doit etre preservee lorsque
  l'on retire cette composante, autrement dit le DAG doit contenir une chaine
  visitant toutes les composantes depuis la source, ou autrement dit un chemin
  hamiltonien (cf. HDAG).
  O(n^2) ou O(n+m) suivant les representations utilisees
*/

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

// identique a hamiltonian() de HDAG
bool semi_connected(vector< vector<bool> > &DAG) {
  // la numerotation est supposee deja suivre un ordre topologique
  for (int i=0; i<(int)DAG.size()-1; ++i)
    if (!DAG[i][i+1]) return false;
  return true;
}

int main() {
  int k;
  cin >> k;
  for (int t=1; t<=k; ++t) {
    int n,m;
    cin >> n >> m;
    graph G(n);
    for (int i=0; i<m; ++i) {
      int u,v;
      cin >> u >> v;
      G[u-1].push_back(v-1);
    }
    vector<int> compo;
    int nc = strongly_connected_components(G,compo);
    // construction du DAG des composantes connexes
    // du fait de la methode de construction, la numerotation
    // des composantes suit deja un ordre topologique
    vector< vector<bool> > DAG(nc);
    for (int i=0; i<nc; ++i) DAG[i].resize(nc,false);
    for (int u=0; u<n; ++u)
      for (auto iv=G[u].begin(); iv!=G[u].end(); ++iv)
	if (compo[u]!=compo[*iv]) DAG[compo[u]][compo[*iv]] = true;
    cout << (semi_connected(DAG) ? 1 : -1) << (t==k ? '\n' : ' ');
  }
  return 0;
}
