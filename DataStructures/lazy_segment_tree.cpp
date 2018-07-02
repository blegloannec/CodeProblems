#include <iostream>
#include <vector>
using namespace std;

typedef int elem;

/* ===== BEGIN LazySegmentTree ===== */
struct LazySegmentTree {
  const elem NEUTRAL = 0; // neutre
  unsigned int N;
  vector<elem> S,L;
  vector<bool> L0;

  // operation utilisee, e.g. min, +, *, etc
  static elem op(elem a, elem b) {
    return a+b;
  }

  // operation iteree n fois
  // a pour min, n*a pour +, a^n pour *
  static elem iter_op (elem a, int n) {
    return n*a;
  }

  // operation de mise a jour (via set() et range_set())
  // a pour un remplacement, a0+a pour addition
  static elem up_op (elem a0, elem a) {
    return a0+a;
  }

  LazySegmentTree() {}
  LazySegmentTree(const vector<elem> &T) {
    init(T);
  }
  
  void init(const vector<elem> &T);
  
  void _update_lazy_field(int p, elem v);
  void _propagate(int p, int span);
  void _lazy_set_range(int p, int start, int span, int i, int j, elem v);
  
  void set_range(int i, int j, elem v) {
    _lazy_set_range(1,0,N,i,j+1,v);
  }

  // returns the op in t in the indexes [i,j) intersected
  // with [start,start+span)
  elem _range(int p, int start, int span, int i, int j);
  
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

void LazySegmentTree::init(const vector<elem> &T) {
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

void LazySegmentTree::_update_lazy_field(int p, elem v) {
  // assert(p<(int)N)
  if (L0[p]) // il y a deja une mise a jour en attente en p
    L[p] = up_op(L[p],v);
  else {
    L0[p] = true;
    L[p] = v;
  }
}

void LazySegmentTree::_propagate(int p, int span) {
  //assert(p<(int)N && L0[p]);
  // propagation de la lazy value de p,
  // mise a jour des valeurs des 2 fils
  elem D = iter_op(L[p],span/2);
  S[2*p] = up_op(S[2*p],D);
  S[2*p+1] = up_op(S[2*p+1],D);
  if (2*p<(int)N) {
    // mise a jour des lazy values des 2 fils
    _update_lazy_field(2*p,L[p]);
    _update_lazy_field(2*p+1,L[p]);
  }
  L0[p] = false;
}

void LazySegmentTree::_lazy_set_range(int p, int start, int span, int i, int j, elem v) {
  if (start+span<=i || j<=start) return;
  else if (i<=start && start+span<=j) {
    // mise a jour des valeurs de p
    S[p] = up_op(S[p],iter_op(v,span));
    if (p<(int)N) _update_lazy_field(p,v);
  }
  else {
    if (p<(int)N && L0[p]) _propagate(p,span);
    _lazy_set_range(2*p,start,span/2,i,j,v);
    _lazy_set_range(2*p+1,start+span/2,span/2,i,j,v);
    S[p] = op(S[2*p],S[2*p+1]);
  }
}

// returns the op in t in the indexes [i,j) intersected
// with [start,start+span)
elem LazySegmentTree::_range(int p, int start, int span, int i, int j) {
  if (start+span<=i || j<=start) return NEUTRAL;
  if (i<=start && start+span<=j) return S[p];
  if (p<(int)N && L0[p]) _propagate(p,span);
  elem left = _range(2*p,start,span/2,i,j);
  elem right = _range(2*p+1,start+span/2,span/2,i,j);
  return op(left,right);
}
/* ===== BEGIN LazySegmentTree ===== */


int main() {
  vector<elem> T = {5,6,4,9,2,1,3,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5};
  LazySegmentTree ST(T);
  for (int i=0; i<(int)T.size(); ++i)
    cout << ST.get(i) << ' ';
  cout << endl;
  ST.set_range(1,16,10);
  ST.set_range(1,9,10);
  ST.set_range(10,16,10);
  ST.set_range(1,16,10);
  for (int i=0; i<(int)T.size(); ++i)
    cout << ST.get(i) << ' ';
  cout << endl;
  return 0;
}
