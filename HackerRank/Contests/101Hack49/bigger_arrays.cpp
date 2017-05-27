#include <iostream>
#include <vector>
//#include <cassert>
using namespace std;

typedef long long elem;

const elem P = 1000000007;

elem expmod(elem a, int n) {
  if (n==0) return 1;
  if (n%2==0) return expmod((a*a)%P,n/2);
  return (a*expmod((a*a)%P,(n-1)/2))%P;
}

struct LazySegmentTree {
  const elem NEUTRAL = 1; // neutre
  unsigned int N;
  vector<elem> S,L;
  vector<bool> L0;

  // operation utilisee
  static inline elem op(elem a, elem b) {
    return (a*b)%P;
  }

  // operation iteree n fois
  static inline elem iter_op (elem a, int n) {
    return expmod(a,n);
  }
  
  LazySegmentTree(const vector<elem> &T) {
    N = 1;
    while (N<T.size()) N <<= 1;
    S.resize(2*N,NEUTRAL);
    L.resize(N,NEUTRAL); // lazy fields
    L0.resize(N,false);
    // les feuilles sont les elements >=N
    for (unsigned int i=0; i<T.size(); ++i) S[N+i] = T[i];
    // les noeuds internes sont les elements de 1 a N-1
    for (int p=N-1; p>0; --p) S[p] = op(S[2*p],S[2*p+1]);
  }

  void propagate(int p, int span) {
    //assert(p<(int)N && L0[p]);
    S[2*p] = iter_op(L[p],span/2);
    S[2*p+1] = iter_op(L[p],span/2);
    if (2*p<(int)N) {
      L0[2*p] = true;
      L[2*p] = L[p];
      L0[2*p+1] = true;
      L[2*p+1] = L[p];
    }
    L0[p] = false;
    //L[p] = NEUTRAL; // useless
  }

  elem _lazy_set_range(int p, int start, int span, int i, int j, elem v) {
    if (start+span<=i || j<=start) return S[p];
    if (i<=start && start+span<=j) {
      S[p] = iter_op(v,span);
      if (p<(int)N) {
	L0[p] = true;
	L[p] = v;
      }
      return S[p];
    }
    if (p<(int)N && L0[p]) propagate(p,span);
    elem left = _lazy_set_range(2*p,start,span/2,i,j,v);
    elem right = _lazy_set_range(2*p+1,start+span/2,span/2,i,j,v);
    S[p] = op(left,right);
    return S[p];
  }
  
  void set_range(int i, int j, elem v) {
    _lazy_set_range(1,0,N,i,j+1,v);
  }

  elem _range(int p, int start, int span, int i, int j) {
    // returns the minimum in t in the indexes [i,j) intersected
    // with [start,start+span)
    if (p<(int)N && L0[p]) propagate(p,span);
    if (start+span<=i || j<=start) return NEUTRAL;
    if (i<=start && start+span<=j) return S[p];
    elem left = _range(2*p,start,span/2,i,j);
    elem right = _range(2*p+1,start+span/2,span/2,i,j);
    return op(left,right);
  }
  
  // returns op{t[i], t[i+1], ..., t[j]}
  elem range(int i, int j) {
    return _range(1,0,N,i,j+1);
  }

  elem get(int i) {
    return range(i,i);
  }

  void set(int i, elem v) {
    set_range(i,i,v);
  }
};

int main() {
  int n,q;
  cin >> n >> q;
  vector<elem> T0(n),T1(n);
  for (int i=0; i<n; ++i) {
    cin >> T0[i];
    T1[i] = T0[i]-1;
  }
  LazySegmentTree ST0(T0),ST1(T1);
  for (int i=0; i<q; ++i) {
    int c,l,r;
    cin >> c;
    if (c==1) {
      elem x;
      cin >> l >> r >> x; --l; --r;
      ST0.set_range(l,r,x);
      ST1.set_range(l,r,x-1);
    }
    else {
      cin >> l >> r; --l; --r;
      cout << ((ST0.range(l,r)-ST1.range(l,r))%P + P)%P << endl;
    }
  }
  return 0;
}
