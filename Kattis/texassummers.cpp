#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

typedef long long weight;
const weight INF = 1LL<<60;

int N;
vector<weight> X,Y;
vector< vector<weight> > D;

vector<int> dijkstra(int u0, int uf) {
  vector<weight> Dist(N, INF);
  vector<int> Pred(N, -1);
  Dist[u0] = 0;
  priority_queue< pair<weight,int> > Q;
  Q.push(make_pair(-Dist[u0], u0));
  while (!Q.empty()) {
    weight d = -Q.top().first;
    int u = Q.top().second;
    Q.pop();
    if (Dist[u]<d) continue;
    for (int v=0; v<N; ++v)
      if (Dist[u]+D[u][v] < Dist[v]) {
	Dist[v] = Dist[u] + D[u][v];
	Pred[v] = u;
	Q.push(make_pair(-Dist[v], v));
      }
  }
  vector<int> Path;
  int u = uf;
  while (u!=u0) {
    Path.push_back(u);
    u = Pred[u];
  }
  Path.push_back(u0);
  reverse(Path.begin(), Path.end());
  return Path;
}

int main() {
  cin >> N;
  N += 2;
  X.resize(N); Y.resize(N);
  for (int i=0; i<N; ++i)
    cin >> X[i] >> Y[i];
  auto sqr = [](weight x){ return x*x; };
  D.resize(N, vector<weight>(N,0));
  for (int u=0; u<N; ++u)
    for (int v=u+1; v<N; ++v)
      D[u][v] = D[v][u] = sqr(X[u]-X[v]) + sqr(Y[u]-Y[v]);
  vector<int> Path = dijkstra(N-2, N-1);
  if (Path.size()==2) cout << "-\n";
  else
    for (int i=1; i<(int)Path.size()-1; ++i)
      cout << Path[i] << '\n';
  return 0;
}
