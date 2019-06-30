/*
  O(N log N) approach by building a forest of K trees (~Kruskal)
  picking greedily the non-connecting edges in decreasing order of weight.
  This works in a tree as we know we always cut exactly K-1 edges
  (hence the an-edge-for-an-edge reasoning makes sense).
  This would not work in a general graph:
               o        (the 3-edge would be kept
              / \        forcing to cut 2 2-edges)
             2   2
            /     \
   A --3-- o       B
            \     /
             2   2
              \ /
               o

  NB: Editorial gives a O(N) DP approach.
*/
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
using ll = long long;

struct edge {
  int u,v,w;
  edge(int u, int v, int w) : u(u), v(v), w(w) {}
  bool operator<(const edge &B) const {
    return w>B.w;  // /!\ inversed for decreasing order!
  }
};

int N;
vector<edge> E;
vector<int> T;
vector<bool> Machine;

int find(int x) {
  if (T[x]<0) return x;
  T[x] = find(T[x]);
  return T[x];
}

void merge(int x, int y) {
  int x0 = find(x), y0 = find(y);
  if (x0!=y0) {
    T[y0] = x0;
    Machine[x0] = Machine[x0] || Machine[y0];
  }
}

ll disconnect() {
  T.resize(N,-1);
  sort(E.begin(),E.end());
  ll W = 0;
  for (edge &e : E)
    if (Machine[find(e.u)] && Machine[find(e.v)]) W += e.w;
    else merge(e.u, e.v);
  return W;
}

int main() {
  int K;
  cin >> N >> K;
  for (int i=0; i<N-1; ++i) {
    int u,v,w;
    cin >> u >> v >> w;
    E.push_back(edge(u,v,w));
  }
  Machine.resize(N,false);
  for (int i=0; i<K; ++i) {
    int u;
    cin >> u;
    Machine[u] = true;
  }
  cout << disconnect() << endl;
  return 0;
}
