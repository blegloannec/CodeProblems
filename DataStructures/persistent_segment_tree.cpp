#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>
using namespace std;

typedef int elem;

/* ===== BEGIN PersistentSegmentTree ===== */
struct PersistentSegmentTree {
  const elem NEUTRAL = 1<<30; // neutre pour l'operation, ici l'infini
  unsigned int N;
  vector< vector<elem> > S;
  const int init_time = 0;
  vector< vector<int> > Time;

  // operation utilisee, ici min
  static elem op(elem a, elem b) {
    return min(a,b);
  }

  PersistentSegmentTree() {}
  PersistentSegmentTree(const vector<elem> &T) {
    init(T);
  }

  void init(const vector<elem> &T);

  elem get(int i) const {
    return S[N+i].back();
  }

  elem _persistent_get(int t, int i) const;
  elem persistent_get(int t, int i) const {
    return _persistent_get(t,N+i);
  }
  
  void persistent_set(int t, int i, elem v);
  
  elem _range(int p, int start, int span, int i, int j) const;
  elem _persistent_range(int t, int p, int start, int span, int i, int j) const;
  
  // returns op{t[i], t[i+1], ..., t[j]}
  elem range(int i, int j) const {
    return _range(1,0,N,i,j+1);
  }

  elem persistent_range(int t, int i, int j) const {
    return _persistent_range(t,1,0,N,i,j+1);
  }
};

void PersistentSegmentTree::init(const vector<elem> &T) {
  N = 1;
  while (N<T.size()) N <<= 1;
  S.resize(2*N);
  Time.resize(2*N);
  for (unsigned int i=0; i<2*N; ++i) {
    S[i].resize(1,NEUTRAL);
    Time[i].resize(1,init_time);
  }
  for (unsigned int i=0; i<T.size(); ++i) S[N+i][0] = T[i];
  for (int p=N-1; p>0; --p) S[p][0] = op(S[2*p][0],S[2*p+1][0]);
}

elem PersistentSegmentTree::_persistent_get(int t, int i) const {
  auto it = upper_bound(Time[i].begin(),Time[i].end(),t);
  assert(it!=Time[i].begin());
  --it;
  int j = distance(Time[i].begin(),it);
  return S[i][j];
}

void PersistentSegmentTree::persistent_set(int t, int i, elem v) {
  unsigned int p = N+i;
  assert(Time[p].back()<=t);
  if (Time[p].back()<=t) {
    S[p].push_back(v);
    Time[p].push_back(t);
  }
  else S[p].back() = v;
  p >>= 1;
  while (p>0) {
    assert(Time[p].back()<=t);
    if (Time[p].back()<t) {
      S[p].push_back(op(S[2*p].back(),S[2*p+1].back()));
      Time[p].push_back(t);
    }
    else S[p].back() = op(S[2*p].back(),S[2*p+1].back());
    p >>= 1;
  }
}

elem PersistentSegmentTree::_range(int p, int start, int span, int i, int j) const {
  // returns the minimum in t in the indexes [i,j) intersected
  // with [start,start+span)
  if (start+span<=i || j<=start) return NEUTRAL;
  if (i<=start && start+span<=j) return S[p].back();
  elem left = _range(2*p,start,span/2,i,j);
  elem right = _range(2*p+1,start+span/2,span/2,i,j);
  return op(left,right);
}

elem PersistentSegmentTree::_persistent_range(int t, int p, int start, int span, int i, int j) const {
  // returns the minimum in t in the indexes [i,j) intersected
  // with [start,start+span)
  if (start+span<=i || j<=start) return NEUTRAL;
  if (i<=start && start+span<=j) return _persistent_get(t,p);
  elem left = _persistent_range(t,2*p,start,span/2,i,j);
  elem right = _persistent_range(t,2*p+1,start+span/2,span/2,i,j);
  return op(left,right);
}
/* ===== END PersistentSegmentTree ===== */


int main() {
  vector<elem> T {2,5,7,6,3};
  PersistentSegmentTree PST(T);
  PST.persistent_set(1,2,4);
  PST.persistent_set(2,3,0);
  PST.persistent_set(3,3,3);
  PST.persistent_set(3,3,5);
  cout << PST.persistent_range(0,1,3) << endl;
  cout << PST.persistent_range(1,1,3) << endl;
  cout << PST.persistent_range(2,1,3) << endl;
  cout << PST.persistent_range(3,1,3) << endl;
  return 0;
}
