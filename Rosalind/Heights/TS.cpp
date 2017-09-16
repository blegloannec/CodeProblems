#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// DFS-based (visit end time) topological sort
// see also SDAG for the in-degree counting approach

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

int main() {
  int m;
  cin >> n >> m;
  G.resize(n);
  for (int i=0; i<m; ++i) {
    int u,v;
    cin >> u >> v;
    G[u-1].push_back(v-1);
  }
  topo_sort();
  for (int i=0; i<n; ++i) {
    cout << O[i]+1;
    if (i==n-1) cout << endl;
    else cout << ' ';
  }
  return 0;
}
