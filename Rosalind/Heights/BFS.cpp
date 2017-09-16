#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int n;
vector< vector<int> > G;
vector<int> Dist;

void bfs(int u0=0) {
  Dist.resize(n,-1);
  queue<int> Q;
  Dist[u0] = 0;
  Q.push(u0);
  while (!Q.empty()) {
    int u = Q.front();
    Q.pop();
    for (vector<int>::iterator iv=G[u].begin(); iv<G[u].end(); ++iv)
      if (Dist[*iv]<0) {
	Dist[*iv] = Dist[u]+1;
	Q.push(*iv);
      }
  }
}

int main() {
  int m;
  cin >> n >> m;
  G.resize(n);
  for (int i=0; i<m; ++i) {
    int u,v;
    cin >> u >> v;
    G[u-1].push_back(v-1);
  }
  bfs();
  for (int u=0; u<n; ++u) {
    cout << Dist[u];
    if (u==n-1) cout << endl;
    else cout << ' ';
  }
  return 0;
}
