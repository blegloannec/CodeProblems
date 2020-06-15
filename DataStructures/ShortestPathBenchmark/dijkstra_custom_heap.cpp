#include "graph.h"
#include <cassert>


struct UpdatableHeap {  // custom updatable MIN heap
  int n, nmax;          // current size, max size
  vector<int> H, Idx;   // heap, index table
  vector<weight> W;     // weight table
  
  UpdatableHeap(int size) {
    n = 0;
    nmax = size;
    H.resize(nmax);
    Idx.resize(nmax, -1);
    W.resize(nmax);
  }

  bool empty() const {
    return n==0;
  }
  
  void _swap(int i, int j) {
    swap(H[i], H[j]);
    Idx[H[i]] = i;
    Idx[H[j]] = j;
  }
  
  void _percolate_up(int i) {
    int i0 = (i-1)/2;
    while (i0>=0 && W[H[i0]]>W[H[i]]) {
      _swap(i, i0);
      i = i0; i0 = (i-1)/2;
    }
  }
  
  void _percolate_down(int i) {
    int l = 2*i+1, r = 2*i+2;
    while ((l<n && W[H[i]]>W[H[l]]) || (r<n && W[H[i]]>W[H[r]])) {
      int j = (r<n && W[H[r]]<=W[H[l]]) ? r : l;
      _swap(i, j);
      i = j; l = 2*i+1; r = 2*i+2;
    }
  }
  
  void _push(int u, weight w) {
    assert(n<nmax);
    H[n] = u;
    Idx[u] = n;
    ++n;
    W[u] = w;
    _percolate_up(n-1);
  }
  
  void _update(int u, weight w) {
    W[u] = w;
    _percolate_up(Idx[u]);
    _percolate_down(Idx[u]);
  }
  
  void set(int u, weight w) {  // push or update
    assert(0<=u && u<nmax);
    if (Idx[u]<0) _push(u, w);
    else _update(u,w);
  }
  
  int pop() {
    assert(!H.empty());
    int root = H[0];
    _swap(0, n-1);
    --n;  // ~pop back
    _percolate_down(0);
    return root;
  }
};


vector<weight> dijkstra_custom_heap(const graph &G, int u0) {
  int n = G.size();
  vector<weight> Dist(n, INF);
  Dist[u0] = 0;
  UpdatableHeap Q(n);
  Q.set(u0, Dist[u0]);
  while (!Q.empty()) {
    int u = Q.pop();
    for (const edge &e : G[u]) {
      int v = e._v_;
      weight w = e._w_;
      if (Dist[u]+w < Dist[v]) {
	Dist[v] = Dist[u]+w;
	Q.set(v, Dist[v]);
      }
    }
  }
  return Dist;
}
