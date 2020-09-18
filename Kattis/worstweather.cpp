#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

typedef int elem;

/* ===== BEGIN SegmentTree ===== */
struct SegmentTree {
  const elem NEUTRAL = 0;
  unsigned int N = 0;
  vector<elem> S;

  static elem op(elem a, elem b) {
    return max(a,b);
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
/* ===== END SegmentTree ===== */


int main() {
  bool first = true;
  while (true) {
    int N;
    scanf("%d", &N);
    if (N==0) break;
    if (first) first = false;
    else printf("\n");
    vector<int> Y(N), R(N);
    for (int i=0; i<N; ++i)
      scanf("%d %d", &Y[i], &R[i]);
    SegmentTree ST(R);
    int Q;
    scanf("%d", &Q);
    for (int q=0; q<Q; ++q) {
      int y,x;
      scanf("%d %d", &y, &x);
      auto ity = lower_bound(Y.begin(), Y.end(), y);
      bool yknown = (ity!=Y.end() && *ity==y);
      int iy = distance(Y.begin(), ity);
      auto itx = lower_bound(Y.begin(), Y.end(), x);
      bool xknown = (itx!=Y.end() && *itx==x);
      int ix = distance(Y.begin(), itx);
      if (!yknown && !xknown) printf("maybe\n");
      else if (!yknown && xknown) {
	if (iy<ix && ST.range(iy,ix-1)>=R[ix]) printf("false\n");
	else printf("maybe\n");
      }
      else if (yknown && !xknown) {
	if (iy+1<ix && ST.range(iy+1,ix-1)>=R[iy]) printf("false\n");
	else printf("maybe\n");
      }
      else {
	if (R[iy]<R[ix] || (iy+1<ix && ST.range(iy+1,ix-1)>=R[ix]))
	  printf("false\n");
	else if (ix-iy==x-y) printf("true\n");
	else printf("maybe\n");
      }
    }
  }
  return 0;
}
