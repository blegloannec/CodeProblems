#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct edge {
  int u,v,w;
  edge(int u, int v, int w) : u(u), v(v), w(w) {}
  bool operator<(const edge &B) const {
    return w<B.w;
  }
};

int N;
vector<edge> E;
vector<int> T;

int find(int x) {
  if (T[x]<0) return x;
  T[x] = find(T[x]);
  return T[x];
}

void merge(int x, int y) {
  int x0 = find(x), y0 = find(y);
  if (x0!=y0) T[y0] = x0;
}

int max_edge_dist(int start, int dest) {
  T.resize(N,-1);
  sort(E.begin(),E.end());
  for (edge &e : E) {
    merge(e.u,e.v);
    if (find(start)==find(dest)) return e.w;
  }
  return -1;
}

int main() {
  int M;
  cin >> N >> M;
  for (int i=0; i<M; ++i) {
    int u,v,w;
    cin >> u >> v >> w; --u; --v;
    E.push_back(edge(u,v,w));
  }
  int res = max_edge_dist(0,N-1);
  if (res<0) cout << "NO PATH EXISTS" << endl;
  else cout << res << endl;
  return 0;
}
