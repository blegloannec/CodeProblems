#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
using ll = long long;

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

ll kruskal() {
  T.resize(N,-1);
  sort(E.begin(),E.end());
  ll W = 0;
  for (edge &e : E)
    if (find(e.u)!=find(e.v)) {
      merge(e.u,e.v);
      W += e.w;
    }
  return W;
}

int main() {
  int M;
  cin >> N >> M;
  for (int i=0; i<M; ++i) {
    int u,v,w;
    cin >> u >> v >> w; --u; --v;
    E.push_back(edge(u,v,w));
  }
  cout << kruskal() << endl;
  return 0;
}
