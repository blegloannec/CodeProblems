#include <cstdio>
#include <vector>
using namespace std;

/*
  Modified Lazy Segment Tree
  Recycled + enhanced from CodeChef/flipcoin.cpp
*/
struct elem {
  int q0, q1, q2, q3;
  
  elem(int q0=0, int q1=0, int q2=0, int q3=0) : q0(q0), q1(q1), q2(q2), q3(q3) {}
  
  elem operator+(const elem &B) const {
    return elem(q0+B.q0, q1+B.q1, q2+B.q2, q3+B.q3);
  }

  void xflip() {
    swap(q0,q1);
    swap(q2,q3);
  }

  void yflip() {
    swap(q0,q3);
    swap(q1,q2);
  }
};

struct Flip2DSegmentTree {
  const elem NEUTRAL; // neutre
  unsigned int N;
  vector<elem> S;
  vector<bool> L0,L1; // L0/1[p] ssi x/y flip non propage dans l'intervalle de p

  Flip2DSegmentTree(const vector<elem> &T) {
    N = 1;
    while (N<T.size()) N <<= 1;
    S.resize(2*N,NEUTRAL);
    L0.resize(N,false);
    L1.resize(N,false);
    // les feuilles sont les elements >=N
    for (unsigned int i=0; i<T.size(); ++i) S[N+i] = T[i];
    // les noeuds internes sont les elements de 1 a N-1
    for (int p=N-1; p>0; --p) S[p] = S[2*p] + S[2*p+1];
  }

  void propagate(int p) {
    //assert(p<(int)N && (L0[p]||L1[p]));
    if (L0[p]) {
      S[2*p].xflip();
      S[2*p+1].xflip();
      L0[p] = false;
      if (2*p<(int)N) {
	L0[2*p]   = !L0[2*p];
	L0[2*p+1] = !L0[2*p+1];
      }
    }
    if (L1[p]) {
      S[2*p].yflip();
      S[2*p+1].yflip();
      if (2*p<(int)N) {
	L1[2*p]   = !L1[2*p];
	L1[2*p+1] = !L1[2*p+1];
      }
      L1[p] = false;
    }
  }

  void _lazy_xflip_range(int p, int start, int span, int i, int j) {
    if (start+span<=i || j<=start) return;
    else if (i<=start && start+span<=j) {
      S[p].xflip();
      if (p<(int)N) L0[p] = !L0[p];
    }
    else {
      if (p<(int)N && (L0[p]||L1[p])) propagate(p);
      _lazy_xflip_range(2*p,start,span/2,i,j);
      _lazy_xflip_range(2*p+1,start+span/2,span/2,i,j);
      S[p] = S[2*p] + S[2*p+1];
    }
  }

  void _lazy_yflip_range(int p, int start, int span, int i, int j) {
    if (start+span<=i || j<=start) return;
    else if (i<=start && start+span<=j) {
      S[p].yflip();
      if (p<(int)N) L1[p] = !L1[p];
    }
    else {
      if (p<(int)N && (L0[p]||L1[p])) propagate(p);
      _lazy_yflip_range(2*p,start,span/2,i,j);
      _lazy_yflip_range(2*p+1,start+span/2,span/2,i,j);
      S[p] = S[2*p] + S[2*p+1];
    }
  }
  
  void xflip_range(int i, int j) {
    _lazy_xflip_range(1,0,N,i,j+1);
  }

  void yflip_range(int i, int j) {
    _lazy_yflip_range(1,0,N,i,j+1);
  }
  
  // returns the sum in t in the indexes [i,j) intersected
  // with [start,start+span)
  elem _range(int p, int start, int span, int i, int j) {
    if (start+span<=i || j<=start) return NEUTRAL;
    if (i<=start && start+span<=j) return S[p];
    if (p<(int)N && (L0[p]||L1[p])) propagate(p);
    elem left = _range(2*p,start,span/2,i,j);
    elem right = _range(2*p+1,start+span/2,span/2,i,j);
    return left+right;
  }
  
  // returns sum{t[i], t[i+1], ..., t[j]}
  elem range(int i, int j) {
    return _range(1,0,N,i,j+1);
  }
};

int main() {
  int N,Q;
  scanf("%d",&N);
  vector<elem> T(N);
  for (int i=0; i<N; ++i) {
    long long x,y;
    scanf("%lld %lld",&x,&y);
    if (x>0) {
      if (y>0) T[i].q0 = 1;
      else T[i].q3 = 1;
    }
    else {
      if (y>0) T[i].q1 = 1;
      else T[i].q2 = 1;
    }
  }
  Flip2DSegmentTree FST(T);
  scanf("%d",&Q);
  for (int q=0; q<Q; ++q) {
    char c;
    int l,r;
    scanf(" %c %d %d",&c,&l,&r); --l; --r;
    if (c=='X') FST.yflip_range(l,r);
    else if (c=='Y') FST.xflip_range(l,r);
    else {
      elem res = FST.range(l,r);
      printf("%d %d %d %d\n",res.q0,res.q1,res.q2,res.q3);
    }
  }
  return 0;
}
