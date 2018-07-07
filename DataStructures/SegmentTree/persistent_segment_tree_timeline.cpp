#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>
using namespace std;

/*
  Array-based implementation of Persistent Segment Tree for a *linear* timeline.
  Standard usage:
    using set_curr() and set_new()
    version times are 0, 1, 2, 3, ...
    Time[root] = {0, 1, 2, ...} so that time = index at the root
  Custom usage: !! UNCOMMENT @Custom code for that !!
    using _set() directly with arbitrarily increasing version times
    times are increasing but not consecutive integers
*/

/* ===== BEGIN PersistentSegmentTree ===== */
typedef int elem;

struct PersistentSegmentTree {
  const elem NEUTRAL = 1<<30; // neutre pour l'operation, ici l'infini
  const int root = 1;
  const int init_time = 0;
  unsigned int N;
  int curr_time = 0;
  vector< vector<int> > Time, LTime, RTime;
  vector< vector<elem> > S;
  /*
    Time[u] contains the times at which node u was modified
    (S[u][k] contains the value of node u at time Time[u][k])
    LTime[u] and RTime[u] contain the time indices of left (2*u)
    and right (2*u+1) children of u at each time from Time[u]
    (e.g. the left child of the k-th version of u, i.e. at time Time[u][k],
     is the l-th version of 2*u for l = LTime[u][k], i.e. at time
     Time[2*u][l] <= Time[u][k] < Time[2*u][l+1] if it exists)
  */

  // operation utilisee, ici min
  static elem op(elem a, elem b) {
    return min(a,b);
  }

  PersistentSegmentTree() {}
  PersistentSegmentTree(unsigned int n) {init(n);}
  PersistentSegmentTree(const vector<elem> &T) {init(T);}

  void init(unsigned int n);
  void init(const vector<elem> &T);

  elem get(int i) const {
    return S[N+i].back();
  }
  // get S[i] at time t in O(log #Time[i]), instead of O(log N) for range(t,i,i)
  elem _get(int t, int i) const;
  elem get(int t, int i) const {
    return _get(t,N+i);
  }

  // modifies at time t >= curr_time
  void _set(int t, int i, elem v);
  // modifies the current version
  void set_curr(int i, elem v) {_set(curr_time,i,v);}
  // modifies as a new version at curr_time+1
  void set_new(int i, elem v) {_set(++curr_time,i,v);}

  elem _range(int t, int p, int start, int span, int i, int j) const;  
  // returns op{t[i], ..., t[j]} at time t
  elem range(int t, int i, int j) const;
  // returns op{t[i], ..., t[j]} at current time
  elem range_curr(int i, int j) const {
    return range(curr_time,i,j);
  }
};

void PersistentSegmentTree::init(unsigned int n) {
  N = 1;
  while (N<n) N <<= 1;
  S.resize(2*N);
  Time.resize(2*N);
  LTime.resize(N);
  RTime.resize(N);
  for (unsigned int i=0; i<2*N; ++i) {
    S[i].resize(1,NEUTRAL);
    Time[i].resize(1,init_time);
    if (i<N) {
      LTime[i].resize(1,init_time);
      RTime[i].resize(1,init_time);
    }
  }
}

void PersistentSegmentTree::init(const vector<elem> &T) {
  init(T.size());
  for (unsigned int i=0; i<T.size(); ++i) S[N+i][0] = T[i];
  for (int p=N-1; p>0; --p) S[p][0] = op(S[2*p][0],S[2*p+1][0]);
}

elem PersistentSegmentTree::_get(int t, int i) const {
  auto it = upper_bound(Time[i].begin(),Time[i].end(),t);
  assert(it!=Time[i].begin());
  --it;
  int j = distance(Time[i].begin(),it);
  return S[i][j];
}

void PersistentSegmentTree::_set(int t, int i, elem v) {
  //curr_time = t;  // @Custom: t becomes the current version
  unsigned int p = N+i;
  assert(Time[p].back()<=t);
  if (Time[p].back()<t) {
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
      LTime[p].push_back(Time[2*p].size()-1);
      RTime[p].push_back(Time[2*p+1].size()-1);
    }
    else {
      S[p].back() = op(S[2*p].back(),S[2*p+1].back());
      LTime[p].back() = Time[2*p].size()-1;
      RTime[p].back() = Time[2*p+1].size()-1;
    }
    p >>= 1;
  }
}

elem PersistentSegmentTree::_range(int t, int p, int start, int span, int i, int j) const {
  // !! here t is not the time but the index of the time in Time[p] !!
  if (start+span<=i || j<=start) return NEUTRAL;
  if (i<=start && start+span<=j) return S[p][t];
  elem left = _range(LTime[p][t],2*p,start,span/2,i,j);
  elem right = _range(RTime[p][t],2*p+1,start+span/2,span/2,i,j);
  return op(left,right);
}

elem PersistentSegmentTree::range(int t, int i, int j) const {
  // @Standard: Time[root] = {0, 1, 2, 3, ...}, time is index
  t = min(t,Time[root].back());
  /* // @Custom: Time[root] values are increasing but not consecutive, dicho search for the index
  auto it = upper_bound(Time[root].begin(),Time[root].end(),t);
  assert(it!=Time[root].begin());
  --it;
  t = distance(Time[root].begin(),it);
  */
  return _range(t,root,0,N,i,j+1);
}
/* ===== END PersistentSegmentTree ===== */


int main() {
  vector<elem> T {2,5,7,6,3};
  PersistentSegmentTree PST(T);
  PST.set_new(2,4);
  PST.set_new(3,0);
  PST.set_new(3,3);
  PST.set_curr(3,5);
  cout << PST.range(0,1,3) << endl;
  cout << PST.range(1,1,3) << endl;
  cout << PST.range(2,1,3) << endl;
  cout << PST.range(3,1,3) << endl;
  return 0;
}
