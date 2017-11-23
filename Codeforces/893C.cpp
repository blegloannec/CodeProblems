#include <iostream>
#include <vector>
using namespace std;

int n;
vector< vector<int> > G;
vector<int> C;
vector<bool> seen;

int dfs(int u) {
  seen[u] = true;
  int m = C[u];
  for (auto iv=G[u].begin(); iv!=G[u].end(); ++iv)
    if (!seen[*iv]) m = min(m,dfs(*iv));
  return m;
}

int main() {
  int m;
  cin >> n >> m;
  G.resize(n);
  C.resize(n);
  for (int i=0; i<n; ++i) cin >> C[i];
  for (int i=0; i<m; ++i) {
    int x,y;
    cin >> x >> y; --x; --y;
    G[x].push_back(y);
    G[y].push_back(x);
  }
  seen.resize(n,false);
  long long res = 0;
  for (int u=0; u<n; ++u)
    if (!seen[u]) res += dfs(u);
  cout << res << endl;
  return 0;
}
