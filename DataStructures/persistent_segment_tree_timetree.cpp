#include <iostream>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <cassert>
#include <algorithm>
using namespace std;

/*
  Array-based implementation of Persistent Segment Tree for an
  arbitrary tree of timelines.
*/

/* ===== BEGIN PersistentSegmentTree ===== */
typedef int elem;

struct PersistentSegmentTree {
  const elem NEUTRAL = 1<<30; // neutre pour l'operation, ici l'infini
  unsigned int N;
  vector< vector<int> > LVersion, RVersion;
  vector< vector<elem> > S;

  // operation utilisee, ici min
  static elem op(elem a, elem b) {
    return min(a,b);
  }

  PersistentSegmentTree() {}
  PersistentSegmentTree(unsigned int n) {init(n);}
  PersistentSegmentTree(const vector<elem> &T) {init(T);}

  void init(unsigned int n);
  void init(const vector<elem> &T);

  void _set(int v, int p, int mask, int i, elem x);
  // creates a new version based on version v0
  void set(int v0, int i, elem x) {
    _set(v0,1,N>>1,i,x);
  }

  elem _range(int v, int p, int start, int span, int i, int j) const;  
  // returns op{t[i], ..., t[j]} in version v
  elem range(int v, int i, int j) const {
    return _range(v,1,0,N,i,j+1);
  }
  elem get(int v, int i) const {
    return range(v,i,i);
  }
};

void PersistentSegmentTree::init(unsigned int n) {
  N = 1;
  while (N<n) N <<= 1;
  S.resize(2*N);
  LVersion.resize(N);
  RVersion.resize(N);
  for (unsigned int i=0; i<2*N; ++i) {
    S[i].resize(1,NEUTRAL);
    if (i<N) {
      LVersion[i].resize(1,0);
      RVersion[i].resize(1,0);
    }
  }
}

void PersistentSegmentTree::init(const vector<elem> &T) {
  init(T.size());
  for (unsigned int i=0; i<T.size(); ++i) S[N+i][0] = T[i];
  for (int p=N-1; p>0; --p) S[p][0] = op(S[2*p][0],S[2*p+1][0]);
}

void PersistentSegmentTree::_set(int v, int p, int mask, int i, elem x) {
  if (mask==0)  // p==N+i
    S[p].push_back(x);
  else {
    if ((i&mask)==0) {  // leaf i is in the left subtree of p
      _set(LVersion[p][v],2*p,mask>>1,i,x);
      LVersion[p].push_back(S[2*p].size()-1);
      RVersion[p].push_back(RVersion[p][v]);
    }
    else {
      _set(RVersion[p][v],2*p+1,mask>>1,i,x);
      LVersion[p].push_back(LVersion[p][v]);
      RVersion[p].push_back(S[2*p+1].size()-1);
    }
    S[p].push_back(op(S[2*p][LVersion[p].back()],S[2*p+1][RVersion[p].back()]));
  }
}

elem PersistentSegmentTree::_range(int v, int p, int start, int span, int i, int j) const {
  if (start+span<=i || j<=start) return NEUTRAL;
  if (i<=start && start+span<=j) return S[p][v];
  elem left = _range(LVersion[p][v],2*p,start,span/2,i,j);
  elem right = _range(RVersion[p][v],2*p+1,start+span/2,span/2,i,j);
  return op(left,right);
}
/* ===== END PersistentSegmentTree ===== */


int main() {
  srand(time(NULL));
  int n = 2000;
  vector<int> T(n);
  for (int i=0; i<n; ++i) T[i] = rand()%n;
  PersistentSegmentTree PST(T);
  vector< vector<int> > S;
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
