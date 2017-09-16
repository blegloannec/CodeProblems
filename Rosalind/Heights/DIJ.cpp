#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int n;
vector< vector< pair<int,int> > > G;
vector<int> Dist;

void dijkstra(int u0=0) {
  Dist.resize(n,-1);
  priority_queue< pair<int,int> > Q;
  Dist[u0] = 0;
  Q.push(make_pair(0,u0));
  while (!Q.empty()) {
    int u = Q.top().second;
    int du = -Q.top().first;
    Q.pop();
    if (du>Dist[u]) continue;
    for (auto iv=G[u].begin(); iv<G[u].end(); ++iv) {
      int v = iv->first;
      int w = iv->second;
      if (Dist[v]<0 || Dist[u]+w<Dist[v]) {
	Dist[v] = Dist[u]+w;
	Q.push(make_pair(-Dist[v],v));
      }
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
  dijkstra();
  for (int u=0; u<n; ++u) {
    cout << Dist[u];
    if (u==n-1) cout << endl;
    else cout << ' ';
  }
  return 0;
}
