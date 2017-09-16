#include <iostream>
#include <vector>
using namespace std;

int n;
vector< vector<int> > G(n);
vector<int> C;

bool dfs_color2(int u) {
  for (auto iv=G[u].begin(); iv!=G[u].end(); ++iv) {
    if (C[*iv]<0) {
      C[*iv] = 1-C[u];
      if (!dfs_color2(*iv)) return false;
    }
    else if (C[*iv]==C[u]) return false;
  }
  return true;
}

bool color2() {
  C.resize(n,-1);
  for (int u=0; u<n; ++u)
    if (C[u]<0) {
      C[u] = 0;
      if (!dfs_color2(u)) return false;
    }
  return true;
}

int main() {
  int k;
  cin >> k;
  for (int t=1; t<=k; ++t) {
    int m;
    cin >> n >> m;
    G.resize(n);
    for (int i=0; i<m; ++i) {
      int u,v;
      cin >> u >> v; --u; --v;
      G[u].push_back(v);
      G[v].push_back(u);
    }
    cout << (color2() ? 1 : -1);
    if (t==k) cout << endl;
    else cout << ' ';
    // cleaning
    G.clear();
    C.clear();
  } 
  return 0;
}
