#include <iostream>
#include <vector>
using namespace std;

int n;
vector< vector<int> > G(n);
vector<int> C;

void dfs(int u) {
  for (auto iv=G[u].begin(); iv!=G[u].end(); ++iv)
    if (C[*iv]<0) {
      C[*iv] = C[u];
      dfs(*iv);
    }
}

int connected_components() {
  C.resize(n,-1);
  int c = 0;
  for (int u=0; u<n; ++u)
    if (C[u]<0) {
      C[u] = c++;
      dfs(u);
    }
  return c;
}

int main() {
  int m;
  cin >> n >> m;
  G.resize(n);
  for (int i=0; i<m; ++i) {
    int u,v;
    cin >> u >> v; --u; --v;
    G[u].push_back(v);
    G[v].push_back(u);
  }
  cout << connected_components() << endl;
  return 0;
}
