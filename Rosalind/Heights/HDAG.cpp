#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/*
  A Hamiltonian path in a DAG must follow a topological ordering.
  So we topologically sort the vertices and check whether there is an edge
  between consecutive vertices in the order.
*/

int n;
vector< vector<int> > G;
vector<int> T,O;
int tps = 0;

void dfs_topo(int u) {
  for (auto iv=G[u].begin(); iv!=G[u].end(); ++iv)
    if (T[*iv]<0) dfs_topo(*iv);
  T[u] = tps++;
  O.push_back(u);
}

void topo_sort() {
  T.resize(n,-1);
  for (int u=0; u<n; ++u)
    if (T[u]<0) dfs_topo(u);
  reverse(O.begin(),O.end());
}

// O(m), could be done in O(n) using (unordered) adjacency sets (i.e. hash
// tables) or the adjacency matrix.
bool hamiltonian() {
  topo_sort();
  for (int i=0; i<n-1; ++i)
    if (find(G[O[i]].begin(),G[O[i]].end(),O[i+1])==G[O[i]].end())
      return false;
  return true;
}

int main() {
  int k,m;
  cin >> k;
  for (int t=1; t<=k; ++t) {
    cin >> n >> m;
    G.resize(n);
    for (int i=0; i<m; ++i) {
      int u,v;
      cin >> u >> v;
      G[u-1].push_back(v-1);
    }
    if (hamiltonian()) {
      cout << "1 ";
      for (int i=0; i<n; ++i) cout << O[i]+1 << (i==n-1 ? '\n' : ' ');
    }
    else cout << -1 << endl;
    // cleaning
    G.clear();
    T.clear();
    O.clear();
    tps = 0;
  }
  return 0;
}
