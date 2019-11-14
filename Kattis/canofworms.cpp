/*
  We sort the cans by coordinates.
  We compute the interval of explosion of each can by binary search.
  We store the intervals in a segment tree and use a pass from
  left to right to query & update the intervals of each can. This computes
  the longuest chain of explosions from each can moving strictly to the left.
  We do the same from right to left.
  This is however not enough as a can to the left of the current can
  could have a radius that pushes the explosions further to the right!
  Indeed, consider the directed graph where A -> B iff can B is within
  the interval of A. In this graph (that we cannot build as it would have too
  many edges), strongly connected components lead to the same global explosion
  and what we want to compute is the number of vertices reachable from a given
  vertex. Let us call "monotonous chain" any path of increasing/decreasing
  coordinates. Clearly any path can be decomposed into a sequence of
  monotonous chains.
  In one iteration of the two-pass process described above, we take into
  account all the paths made of 1 monotonous chain.
  In a second iteration, all the paths made of 2 monotonous chains.
  In a 3rd iteration, all the 4-chain paths.
  In a kth iteration, all the 2^(k-1)-chain paths.
  Hence we do not need more than O(log n) iterations to reach a fixed-point.
  Each pass is O(n log n). Total complexity is O(n log^2 n).
*/
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;


/* ===== BEGIN SegmentTree ===== */
typedef pair<int,int> elem;
#define _min_ first
#define _max_ second

struct SegmentTree {
  const elem NEUTRAL = make_pair(1<<30, -1<<30); // inf
  unsigned int N = 0;
  vector<elem> S;

  // operation utilisee
  static elem op(const elem &a, const elem &b) {
    return make_pair(min(a._min_,b._min_), max(a._max_,b._max_));
  }

  SegmentTree() {}
  SegmentTree(unsigned int n) {init(n);}
  SegmentTree(const vector<elem> &T) {init(T);}

  void init(unsigned int n);
  void init(const vector<elem> &T);

  elem get(int i) const {
    return S[N+i];
  }

  bool set(int i, const elem &v);

  elem _range(int p, int start, int span, int i, int j) const;
  // returns op{t[i], t[i+1], ..., t[j]}
  elem range(int i, int j) const {
    return _range(1,0,N,i,j+1);
  }
};

void SegmentTree::init(unsigned int n) {
  N = 1;
  while (N<n) N <<= 1;
  S.resize(2*N,NEUTRAL);
}

void SegmentTree::init(const vector<elem> &T) {
  init(T.size());
  for (unsigned int i=0; i<T.size(); ++i) S[N+i] = T[i];
  for (int p=N-1; p>0; --p) S[p] = op(S[2*p],S[2*p+1]);
}

bool SegmentTree::set(int i, const elem &v) {
  unsigned int p = N+i;
  if (S[p]==v) return false;
  S[p] = v;
  p >>= 1;
  while (p>0) {
    S[p] = op(S[2*p],S[2*p+1]);
    p >>= 1;
  }
  return true;
}

elem SegmentTree::_range(int p, int start, int span, int i, int j) const {
  // returns the minimum in t in the indexes [i,j) intersected
  // with [start,start+span)
  if (start+span<=i || j<=start) return NEUTRAL;
  if (i<=start && start+span<=j) return S[p];
  elem left = _range(2*p,start,span/2,i,j);
  elem right = _range(2*p+1,start+span/2,span/2,i,j);
  return op(left,right);
}
/* ===== END SegmentTree ===== */


struct can {
  int x,r,i;
  can(int x, int r, int i) : x(x), r(r), i(i) {}
  bool operator<(const can &C) const { return x<C.x; }
};

int N;
vector<can> Cans;

int dicho_left(int i) {
  int l = 0, r = i;
  while (l<r) {
    int m = (l+r)/2;
    if (Cans[i].x-Cans[m].x <= Cans[i].r) r = m;
    else l = m+1;
  }
  return l;
}

int dicho_right(int i) {
  int l = i, r = N-1;
  while (l<r) {
    int m = (l+r+1)/2;
    if (Cans[m].x-Cans[i].x <= Cans[i].r) l = m;
    else r = m-1;
  }
  return l;
}

int main() {
  // input
  scanf("%d", &N);
  for (int i=0; i<N; ++i) {
    int x,r;
    scanf("%d %d", &x, &r);
    Cans.push_back(can(x,r,i));
  }
  // init.
  sort(Cans.begin(), Cans.end());
  vector<elem> I;
  for (int i=0; i<N; ++i)
    I.push_back(make_pair(dicho_left(i), dicho_right(i)));
  SegmentTree ST(I);
  // iterations
  bool modif = true;
  while (modif) {
    modif = false;
    for (int i=0; i<N; ++i) {
      auto LRi = ST.get(i);
      modif |= ST.set(i, ST.range(LRi._min_,LRi._max_));
    }
    for (int i=N-1; i>=0; --i) {
      auto LRi = ST.get(i);
      modif |= ST.set(i, ST.range(LRi._min_,LRi._max_));
    }
  }
  // gathering results
  vector<int> Res(N,1);
  for (int i=0; i<N; ++i) {
    auto LRi = ST.get(i);
    Res[Cans[i].i] = LRi._max_ - LRi._min_ + 1;
  }
  // output
  for (int i=0; i<N; ++i) {
    printf("%d", Res[i]);
    if (i==N-1) printf("\n");
    else printf(" ");
  }
  return 0;
}
