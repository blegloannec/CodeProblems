#include <cstdio>
#include <vector>
#include <queue>
using namespace std;

int N;
vector< vector<int> > G;

int bfs(int u0, int u1) {
  vector<int> Dist(N,-1);
  Dist[u0] = 0;
  deque<int> Q;
  Q.push_back(u0);
  while (!Q.empty()) {
    int u = Q.front();
    Q.pop_front();
    if (u==u1) break;
    for (int v : G[u])
      if (Dist[v]<0) {
	Dist[v] = Dist[u]+1;
	Q.push_back(v);
      }
  }
  return Dist[u1];
}

int main() {
  int M;
  scanf("%d %d", &N, &M);
  G.resize(N);
  for (int i=0; i<M; ++i) {
    int a,b;
    scanf("%d %d", &a, &b);
    --a; --b;
    G[a].push_back(b);
    G[b].push_back(a);
  }
  int res = bfs(0, N-1) - 1;
  printf("%d\n", res);
  return 0;
}
