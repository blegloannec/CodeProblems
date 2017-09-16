#include <iostream>
#include <vector>
using namespace std;

int n;
vector< vector< pair<int,int> > > G;
vector<int> Dist;

bool bellman_ford(int u0=0) {
  Dist.resize(n,1000000000);
  Dist[u0] = 0;
  for (int k=0; k<n-1; ++k)
    for (int u=0; u<n; ++u)
      for (auto iv=G[u].begin(); iv<G[u].end(); ++iv)
	Dist[iv->first] = min(Dist[iv->first], Dist[u] + iv->second);
  // checking for negative cycles
  for (int u=0; u<n; ++u)
    for (auto iv=G[u].begin(); iv<G[u].end(); ++iv)
      if (Dist[u] + iv->second < Dist[iv->first]) return false;
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
      int u,v,w;
      cin >> u >> v >> w;
      G[u-1].push_back(make_pair(v-1,w));
    }
    cout << (bellman_ford() ? -1 : 1);
    if (t==k) cout << endl;
    else cout << ' ';
    // cleaning
    G.clear();
    Dist.clear();
  }
  return 0;
}
