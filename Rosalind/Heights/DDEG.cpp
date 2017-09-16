#include <iostream>
#include <vector>
using namespace std;

int main() {
  int n,m;
  cin >> n >> m;
  vector< vector<int> > G(n);
  for (int i=0; i<m; ++i) {
    int u,v;
    cin >> u >> v; --u; --v;
    G[u].push_back(v);
    G[v].push_back(u);
  }
  for (int u=0; u<n; ++u) {
    int vu = 0;
    for (vector<int>::iterator iv=G[u].begin(); iv<G[u].end(); ++iv)
      vu += G[*iv].size();
    cout << vu;
    if (u==n-1) cout << endl;
    else cout << ' ';
  }
  return 0;
}
