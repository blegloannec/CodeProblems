#include <iostream>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <cassert>
#include <algorithm>
using namespace std;

/*
  Sparse implementation of Persistent Segment Tree for an
  arbitrary tree of timelines.
*/

/* ===== BEGIN SparsePersistSegtree ===== */
typedef int elem;

struct SparsePersistSegtree {
  const elem NEUTRAL = 1<<30; // neutre pour l'operation, ici l'infini
  const int NIL = 0;  // convenient sentinel
  const int root = 1;
  unsigned int N;
  vector<int> L, R;
  vector< vector<int> > LVersion, RVersion;
  vector< vector<elem> > S;

  // operation utilisee, ici min
  static elem op(elem a, elem b) {
    return min(a,b);
  }

  SparsePersistSegtree() {}
  SparsePersistSegtree(unsigned int n) {init(n);}

  int new_node();
  void init(unsigned int n);

  void _set(int v, int p, int mask, int i, elem x);
  // creates a new version based on version v0
  void set(int v0, int i, elem x) {
    _set(v0,root,N>>1,i,x);
  }

  elem _range(int v, int p, int start, int span, int i, int j) const;  
  // returns op{t[i], ..., t[j]} in version v
  elem range(int v, int i, int j) const {
    return _range(v,root,0,N,i,j+1);
  }
  elem get(int v, int i) const {
    return range(v,i,i);
  }
};

int SparsePersistSegtree::new_node() {
  int u = S.size();
  S.resize(u+1);
  S[u].push_back(NEUTRAL);
  L.push_back(NIL);
  R.push_back(NIL);
  LVersion.resize(u+1);
  LVersion[u].push_back(0);
  RVersion.resize(u+1);
  RVersion[u].push_back(0);
  return u;
}

void SparsePersistSegtree::init(unsigned int n) {
  N = 1;
  while (N<n) N <<= 1;
  new_node();  // 0 NIL
  new_node();  // 1 root
}

void SparsePersistSegtree::_set(int v, int p, int mask, int i, elem x) {
  if (mask==0)  // p is the leaf i
    S[p].push_back(x);
  else {
    if ((i&mask)==0) {  // leaf i is in the left subtree of p
      if (L[p]==NIL) {
	int u = new_node();
	L[p] = u;
      }
      _set(LVersion[p][v],L[p],mask>>1,i,x);
      LVersion[p].push_back(S[L[p]].size()-1);
      RVersion[p].push_back(RVersion[p][v]);
    }
    else {
      if (R[p]==NIL) {
	int u = new_node();
	R[p] = u;
      }
      _set(RVersion[p][v],R[p],mask>>1,i,x);
      LVersion[p].push_back(LVersion[p][v]);
      RVersion[p].push_back(S[R[p]].size()-1);
    }
    // no problem here thanks to the NIL sentinel
    S[p].push_back(op(S[L[p]][LVersion[p].back()],S[R[p]][RVersion[p].back()]));
  }
}

elem SparsePersistSegtree::_range(int v, int p, int start, int span, int i, int j) const {
  if (p==NIL) return NEUTRAL;
  if (start+span<=i || j<=start) return NEUTRAL;
  if (i<=start && start+span<=j) return S[p][v];
  elem left = _range(LVersion[p][v],L[p],start,span/2,i,j);
  elem right = _range(RVersion[p][v],R[p],start+span/2,span/2,i,j);
  return op(left,right);
}
/* ===== END SparsePersistSegtree ===== */


int main() {
  srand(time(NULL));
  int n = 2000;
  SparsePersistSegtree PST(n);
  vector< vector<int> > S;
  vector<int> T(n,PST.NEUTRAL);
  S.push_back(T);
  for (int t=1; t<n; ++t) {
    int v0 = rand()%t;
    int i = rand()%n;
    int x = rand()%n;
    PST.set(v0,i,x);
    vector<int> St = S[v0];
    St[i] = x;
    S.push_back(St);
    for (int i=0; i<n; ++i) assert(St[i]==PST.get(t,i));
  }
  return 0;
}
