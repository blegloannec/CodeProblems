#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int n;
vector< vector< pair<int,int> > > G;
vector<int> Dist;

// assuming there are no negative cycles
void bellman_ford(int u0=0) {
  Dist.resize(n,INT_MAX);
  Dist[u0] = 0;
  for (int k=0; k<n-1; ++k)
    for (int u=0; u<n; ++u)
      if (Dist[u]<INT_MAX)
	for (auto iv=G[u].begin(); iv<G[u].end(); ++iv)
	  Dist[iv->first] = min(Dist[iv->first], Dist[u] + iv->second);
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
  bellman_ford();
  for (int u=0; u<n; ++u) {
    if (Dist[u]==INT_MAX) cout << 'x';
    else cout << Dist[u];
    if (u==n-1) cout << endl;
    else cout << ' ';
  }
  return 0;
}
