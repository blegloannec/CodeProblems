#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>
using namespace std;

int N,S;
vector< unordered_set<int> > G;
vector<int> Dist;

/*
  BFS in the complementary of a sparse (enough) graph
  N ~ 10^5  &  M = O(N)  (or at least manageable << N^2)
*/
void complement_bfs() {
  Dist.resize(N,-1);
  Dist[S] = 0;
  vector<int> Vertices;  // list of unvisited vertices
  for (int u=0; u<N; ++u)
    if (u!=S) Vertices.push_back(u);
  queue<int> Q;
  Q.push(S);
  while (!Q.empty()) {
    int u = Q.front();
    Q.pop();
    vector<int> RemVert;
    for (int v : Vertices) {
      if (G[u].find(v)==G[u].end()) {
	Dist[v] = Dist[u] + 1;
	Q.push(v);
      }
      else RemVert.push_back(v);
    }
    swap(Vertices,RemVert);
    /*
      After the i-th step, where vertex u(i) is popped, Vertices(i)
      is a subset of G[u(i)] (even more precisely, its intersection
      with Vertices(i-1)).
      Thus instead of iterating over the neighbors of u(i),
      we iterate over a subset of the neighbors of u(i-1).
      It is pretty clear that this is perfectly equivalent complexity-wise
      and that the complexity is O(N + M).
    */
  }
}

int main() {
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    int M;
    cin >> N >> M;
    G.resize(N);
    for (int i=0; i<M; ++i) {
      int x,y;
      cin >> x >> y; --x; --y;
      G[x].insert(y);
      G[y].insert(x);
    }
    cin >> S; --S;
    complement_bfs();
    bool first = true;
    for (int u=0; u<N; ++u)
      if (u!=S) {
	if (first) first = false;
	else cout << ' ';
	cout << Dist[u];
      }
    cout << endl;
    // cleaning
    G.clear();
    Dist.clear();
  }
  return 0;
}
