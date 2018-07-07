/*
  Illustration of a very simple yet worthwhile "trick" when a segment tree S
  is used as a frequency array (buckets that count the number of occurrences
  of each value) of a multiset T.
  Without loss of generality, we assume the values in T are between 0 and N-1.
  When looking for the k-th smallest value of T, one can do a dichotomic search
  for the smallest index x such that k <= S.range(0,x). That "black box"
  approach costs O(log^2 N).
  A better idea is to do the dichotomic search "inside" the segment tree as
  illustrated by the get_kth() method below, which only costs O(log N).
  This is a very basic technique, as long as you think about it...
*/

#include <iostream>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <algorithm>
#include <cassert>
using namespace std;

typedef int elem;

/* ===== Frequency SegmentTree ===== */
struct SegmentTree {
  const elem NEUTRAL = 0; // neutre pour l'operation
  unsigned int N = 0;
  vector<elem> S;

  // operation utilisee, ici min
  static elem op(elem a, elem b) {
    return a+b;
  }

  SegmentTree() {}
  SegmentTree(unsigned int n) {init(n);}
  SegmentTree(const vector<elem> &T) {init(T);}

  void init(unsigned int n);
  void init(const vector<elem> &T);

  elem get(int i) const {
    return S[N+i];
  }

  void set(int i, elem v);

  elem _range(int p, int start, int span, int i, int j) const;
  // returns op{t[i], t[i+1], ..., t[j]}
  elem range(int i, int j) const {
    return _range(1,0,N,i,j+1);
  }
  
  int get_kth(int k) const;  //  <--
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

void SegmentTree::set(int i, elem v) {
  unsigned int p = N+i;
  S[p] = v;
  p >>= 1;
  while (p>0) {
    S[p] = op(S[2*p],S[2*p+1]);
    p >>= 1;
  }
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

// dichotomic search for k-th element inside the frequency segment tree
int SegmentTree::get_kth(int k) const {
  assert(1<=k);
  unsigned int p = 1;
  while (p<N) {
    if (k<=S[2*p]) p = 2*p;
    else {
      k -= S[2*p];
      p = 2*p+1;
    }
  }
  return (int)p-N;
}
/* ===== Frequency SegmentTree ===== */


int main() {
  srand(time(NULL));
  const int n = 2000000, m = 500000, q = 500000;
  vector<int> T(n),F(m,0);
  for (int i=0; i<n; ++i) {
    T[i] = rand()%m;
    ++F[T[i]];
  }
  sort(T.begin(),T.end());
  SegmentTree ST(F);
  for (int i=0; i<q; ++i) {
    int k = rand()%n;
    assert(ST.get_kth(k+1)==T[k]);
  }
  return 0;
}
