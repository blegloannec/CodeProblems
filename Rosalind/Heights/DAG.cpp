#include <iostream>
#include <vector>
using namespace std;

int n;
vector< vector<int> > G;
vector<bool> Grey,Black;

bool dfs_acyclic(int u) {
  Grey[u] = true;
  for (auto iv=G[u].begin(); iv!=G[u].end(); ++iv)
    if (!Black[*iv]) {
      if (Grey[*iv]) return false;
      else if (!dfs_acyclic(*iv)) return false;
    }
  Black[u] = true;
  return true;
}

bool acyclic() {
  for (int u=0; u<n; ++u)
    if (!Black[u])
      if (!dfs_acyclic(u)) return false;
  return true;
}

int main() {
  int k;
  cin >> k;
  for (int t=1; t<=k; ++t) {
    int m;
    cin >> n >> m;
    G.resize(n);
    Black.resize(n,false);
    Grey.resize(n,false);
    for (int i=0; i<m; ++i) {
      int u,v;
      cin >> u >> v;
      G[u-1].push_back(v-1);
    }
    cout << (acyclic() ? 1: -1);
    if (t==k) cout << endl;
    else cout << ' ';
    // cleaning
    G.clear();
    Black.clear();
    Grey.clear();
  }
  return 0;
}
