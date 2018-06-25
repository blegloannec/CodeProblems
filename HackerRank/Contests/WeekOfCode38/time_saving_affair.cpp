#include <iostream>
#include <vector>
#include <queue>
using namespace std;

typedef long long ent;

int n;
ent k;
vector< vector< pair<int,int> > > G;
vector<ent> Dist;

ent dijkstra(int u0, int u1) {
  Dist.resize(n,-1);
  priority_queue< pair<ent,int> > Q;
  Dist[u0] = 0;
  Q.push(make_pair(0,u0));
  while (!Q.empty()) {
    int u = Q.top().second;
    ent du = -Q.top().first;
    Q.pop();
    if (du>Dist[u]) continue;
    if (u==u1) break;
    if ((du/k)%2==1) du = ((du+k)/k)*k;  // attente au feu rouge
    for (auto iv=G[u].begin(); iv<G[u].end(); ++iv) {
      int v = iv->first;
      ent w = iv->second;
      if (Dist[v]<0 || du+w<Dist[v]) {
	Dist[v] = du+w;
	Q.push(make_pair(-Dist[v],v));
      }
    }
  }
  return Dist[u1];
}

int main() {
  cin >> n;
  cin >> k;
  int m;
  cin >> m;
  G.resize(n);
  for (int i=0; i<m; ++i) {
    int u,v,w;
    cin >> u >> v >> w; --u; --v;
    G[u].push_back(make_pair(v,w));
    G[v].push_back(make_pair(u,w));
  }
  cout << dijkstra(0,n-1) << endl;
  return 0;
}
