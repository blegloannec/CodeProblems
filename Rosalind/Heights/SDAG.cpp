#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int n;
vector< vector< pair<int,int> > > G;
vector<int> Dist;

void topo_dist(int u0=0) {
  vector<int> Din(n,0);
  for (int u=0; u<n; ++u)
    for (auto iv=G[u].begin(); iv!=G[u].end(); ++iv)
      ++Din[iv->first];
  vector<int> Q;
  for (int u=0; u<n; ++u)
    if (Din[u]==0) Q.push_back(u);
  Dist.resize(n,INT_MAX);
  Dist[u0] = 0;
  while (!Q.empty()) {
    int u = Q.back();
    Q.pop_back();
    for (auto iv=G[u].begin(); iv!=G[u].end(); ++iv) {
      int v = iv->first;
      if (Dist[u]!=INT_MAX)
	Dist[v] = min(Dist[v], Dist[u] + iv->second);
      --Din[v];
      if (Din[v]==0) Q.push_back(v);
    }
  }
}

int main() {
  int m;
  cin >> n >> m;
  G.resize(n);
  for (int i=0; i<m; ++i) {
    int u,v,w;
    cin >> u >> v >> w;
    G[u-1].push_back(make_pair(v-1,w));
  }
  topo_dist();
  for (int u=0; u<n; ++u) {
    if (Dist[u]==INT_MAX) cout << 'x';
    else cout << Dist[u];
    if (u==n-1) cout << endl;
    else cout << ' ';
  }
  return 0;
}
