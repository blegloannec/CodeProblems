/*
  O(N log N) sorting + union-find
  NB: usual approach when dealing with max-edge distance in graphs
*/
#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>
using namespace std;
using ll = long long;

struct edge {
  int u,v,w;
  edge(int u, int v, int w) : u(u), v(v), w(w) {}
  bool operator<(const edge &B) const { return w<B.w; }
};

int N;
vector<edge> E;
vector<int> T;
vector<ll> S, Count;

int find(int x) {
  if (T[x]<0) return x;
  T[x] = find(T[x]);
  return T[x];
}

void merge(int i) {
  int u0 = find(E[i].u), v0 = find(E[i].v);
  assert(u0!=v0);
  Count[i] = S[u0]*S[v0];  // counting paths having E[i] as max edge
  T[v0] = u0;
  S[u0] += S[v0];
}

int main() {
  int Q;
  cin >> N >> Q;
  for (int i=0; i<N-1; ++i) {
    int u,v,w;
    cin >> u >> v >> w; --u; --v;
    E.push_back(edge(u,v,w));
  }
  sort(E.begin(),E.end());  // sorting edges by weight
  T.resize(N,-1);
  S.resize(N,1);
  Count.resize(N-1);
  for (int i=0; i<N-1; ++i) merge(i);
  for (int i=1; i<N-1; ++i) Count[i] += Count[i-1];
  for (int q=0; q<Q; ++q) {
    int L,R;
    cin >> L >> R;
    int l = distance(E.begin(), lower_bound(E.begin(),E.end(),edge(0,0,L)));
    int r = distance(E.begin(), upper_bound(E.begin(),E.end(),edge(0,0,R)))-1;
    ll res = r>=0 ? Count[r] - (l-1>=0 ? Count[l-1] : 0) : 0;
    cout << res << endl;
  }
  return 0;
}
