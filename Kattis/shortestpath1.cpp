#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int n,m;
vector< vector< pair<int,int> > > G;
vector<int> D;

void dijkstra(int s) {
  D.resize(n,-1);
  D[s] = 0;
  priority_queue< pair<int,int> > Q;
  Q.push(make_pair(0,s));
  while (!Q.empty()) {
    int u = Q.top().second, d = -Q.top().first;
    Q.pop();
    if (d>D[u]) continue;
    for (auto iv=G[u].begin(); iv!=G[u].end(); ++iv) {
      int v = iv->first, w = iv->second;
      if (D[v]<0 || d+w<D[v]) {
	D[v] = d+w;
	Q.push(make_pair(-D[v],v));
      }
    }
  }
}

int main() {
  int q,s;
  while (cin >> n >> m >> q >> s) {
    if (n==0) break;
    G.resize(n);
    for (int i=0; i<m; ++i) {
      int u,v,w;
      cin >> u >> v >> w;
      G[u].push_back(make_pair(v,w));
    }
    dijkstra(s);
    for (int i=0; i<q; ++i) {
      int t;
      cin >> t;
      if (D[t]<0) cout << "Impossible" << endl;
      else cout << D[t] << endl;
    }
    cout << endl;
    // cleaning
    G.clear();
    D.clear();
  }
  return 0;
}
