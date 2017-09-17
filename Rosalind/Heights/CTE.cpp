#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int n;
vector< vector< pair<int,int> > > G;
vector<int> Dist;

int dijkstra(int u0, int uf) {
  Dist.resize(n,-1);
  priority_queue< pair<int,int> > Q;
  Dist[u0] = 0;
  Q.push(make_pair(0,u0));
  while (!Q.empty()) {
    int u = Q.top().second;
    int du = -Q.top().first;
    Q.pop();
    if (u==uf) return du; // destination reached
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
  return -1;
}

int main() {
  int k;
  cin >> k;
  for (int t=1; t<=k; ++t) {
    int m,u0,v0,w0;
    cin >> n >> m;
    G.resize(n);
    for (int i=0; i<m; ++i) {
      int u,v,w;
      cin >> u >> v >> w; --u; --v;
      G[u].push_back(make_pair(v,w));
      if (i==0) {
	u0 = u;	v0 = v;	w0 = w;
      }
    }
    int d = dijkstra(v0,u0);
    cout << (d<0 ? -1 : d+w0) << (t==k ? '\n' : ' ');
    // cleaning
    G.clear();
    Dist.clear();
  }
  return 0;
}
