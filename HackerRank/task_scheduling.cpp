/*
  NOT an actual scheduling problem...
  Given a set of n indexed tasks (not sorted in any way),
  one has to compute the maximum lateness of the "1 | pmtn | Lmax"
  scheduling problem of the first k tasks, for all k from 1 to n.
  Without release times on 1 machine, pmtn does not make any difference
  and the basic earliest-deadline-first heuristic is optimal.
  Given the deadline-sorted planning for the first k tasks, one has to
  insert the task k+1 at its position (sorted by deadline, which shifts the
  tasks planified after by the duration of this task) and to update Lmax.
  The following code implements this in O(n log n) relying on
  sorting  (to compute the final planning & insertion positions)
    &  (max,+) lazy segment tree  (to shift tasks & compute Lmax)
    &  + fenwick tree  (to compute insertion times on-the-fly)
*/
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;


/* ===== BEGIN LazySegmentTree ===== */
typedef int elem;

struct LazySegmentTree {
  const elem NEUTRAL = INT_MIN; // neutre
  const elem NEUTRAL_UP = 0; // neutre pour up_op
  unsigned int N = 0;
  vector<elem> S,L;
  vector<bool> L0;

  // operation utilisee, e.g. min, +, *, etc
  static elem op(elem a, elem b) {
    return max(a,b);
  }

  // operation iteree n fois
  // a pour min, n*a pour +, a^n pour *
  static elem iter_op (elem a, int n) {
    return a;
  }

  // operation de mise a jour (via set() et set_range())
  // a pour un remplacement, a0+a pour addition
  static elem up_op (elem a0, elem a) {
    return a0+a;
  }

  LazySegmentTree() {}
  LazySegmentTree(unsigned int n) {init(n);}
  LazySegmentTree(const vector<elem> &T) {init(T);}

  void init(unsigned int n);
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

void LazySegmentTree::init(unsigned int n) {
  N = 1;
  while (N<n) N <<= 1;
  S.resize(2*N,NEUTRAL);
  L.resize(N,NEUTRAL_UP); // lazy fields
  L0.resize(N,false);
}

void LazySegmentTree::init(const vector<elem> &T) {
  init(T.size());
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
/* ===== END LazySegmentTree ===== */


/* ===== Fenwick Trees ===== */
typedef int ent;

struct Fenwick {
  vector<ent> FT;

  void add(int i, ent v);
  ent prefix_sum(int i) const;

  Fenwick(int n) {
    FT.resize(n+1,0);
  }
};

void Fenwick::add(int i, ent v=1) {
  //assert(i>0);
  while (i<(int)FT.size()) {
    FT[i] += v;
    i += i&-i;
  }
}

ent Fenwick::prefix_sum(int i) const { // prefix sum
  ent s = 0;
  while (i>0) {
    s += FT[i];
    i -= i&-i;
  }
  return s;
}
/* ===== END Fenwick ===== */


struct Task {
  int i,D,M;
  Task(int i, int D, int M) : i(i), D(D), M(M) {}
  bool operator<(const Task &B) const {
    return (D<B.D) || (D==B.D && i<B.i);
  }
};

int main() {
  int T;
  cin >> T;
  vector<Task> Tasks;
  for (int i=0; i<T; ++i) {
    int D,M;
    cin >> D >> M;
    Tasks.push_back(Task(i,D,M));
  }
  sort(Tasks.begin(),Tasks.end());
  vector<int> Idx(T);
  for (int i=0; i<T; ++i) Idx[Tasks[i].i] = i;
  LazySegmentTree ST(T);
  Fenwick F(T);
  for (int i=0; i<T; ++i) {
    int j = Idx[i];
    int t = F.prefix_sum(j);
    F.add(j+1,Tasks[j].M);
    if (j<T-1) ST.set_range(j+1,T-1,Tasks[j].M); // adds M to the range [j+1..]
    ST.set(j,-ST.get(j));               // reset to 0
    ST.set(j,t+Tasks[j].M-Tasks[j].D);  // sets to the right overshot
    cout << max(0,ST.range(0,T-1)) << endl;
  }
  return 0;
}
