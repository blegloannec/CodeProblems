#include <iostream>
#include <vector>
using namespace std;

/*
  On commence comme pour la construction des composantes fortement connexes
  par un pseudo tri topologique. On sait alors que le dernier sommet dans
  l'ordre obtenu appartient a une composante connexe source. Si le graphe
  admet une source generale, alors il n'a qu'une seule composante connexe
  source et n'importe lequel de ses sommets est une source generale. Il suffit
  donc de verifier par un parcours que tous les sommets sont accessibles
  depuis ce sommet candidat.
*/

typedef vector< vector<int> > graph;

void dfs_topo(graph &G, int u, vector<bool> &seen, vector<int> &topo) {
  if (seen[u]) return;
  seen[u] = true;
  for (vector<int>::iterator it=G[u].begin(); it!=G[u].end(); ++it)
    dfs_topo(G,*it,seen,topo);
  topo.push_back(u);
}

void dfs(graph &G, int u, vector<bool> &seen) {
  seen[u] = true;
  for (auto iv=G[u].begin(); iv!=G[u].end(); ++iv)
    if (!seen[*iv]) dfs(G,*iv,seen);
}

int general_sink(graph &G) {
  int N = G.size();
  vector<bool> seen(N,false);
  vector<int> topo;
  for (int u=0; u<N; ++u) dfs_topo(G,u,seen,topo);
  int gs = topo[N-1]; // candidat
  // verification
  fill(seen.begin(),seen.end(),false);
  dfs(G,gs,seen);
  for (int u=0; u<N; ++u) if (!seen[u]) return -1;
  return gs;
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
    int gs = general_sink(G);
    cout << (gs<0 ? -1 : gs+1) << (t==k ? '\n' : ' ');
  }
  return 0;
}
