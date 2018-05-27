/*
  We use interval-compatible renumbering of the tree + tree traversal trace +
  segment tree for range min query to get LCA in O(log N).
  Using interval-compatible renumbering of the tree + Fenwick tree we maintain
  the number F(u) of broken links from the (arbitrary) root to any vertex u.
  This is easily maintainable and allows us to know whether any vertex u is
  currently connected to any of its descendants v: we always have F(v) >= F(u)
  and F(v) = F(u) iff they are connected.
  Each request costs O(log N).
*/

#include <iostream>
#include <vector>
#include <unordered_set>
#include <cassert>
using namespace std;

typedef int elem;

struct SegmentTree {
  const elem NEUTRAL = 1<<30; // neutre pour l'operation, ici l'infini
  unsigned int N;
  vector<elem> S;

  // operation utilisee, ici min
  static elem op(elem a, elem b) {
    return min(a,b);
  }

  SegmentTree(const vector<elem> &T) {
    N = 1;
    while (N<T.size()) N <<= 1;
    S.resize(2*N,NEUTRAL);
    for (unsigned int i=0; i<T.size(); ++i) S[N+i] = T[i];
    for (int p=N-1; p>0; --p) S[p] = op(S[2*p],S[2*p+1]);
  }

  elem get(int i) const {
    return S[N+i];
  }

  void set(int i, elem v) {
    unsigned int p = N+i;
    S[p] = v;
    p >>= 1;
    while (p>0) {
      S[p] = op(S[2*p],S[2*p+1]);
      p >>= 1;
    }
  }

  elem _range(int p, int start, int span, int i, int j) const {
    // returns the minimum in t in the indexes [i,j) intersected
    // with [start,start+span)
    if (start+span<=i || j<=start) return NEUTRAL;
    if (i<=start && start+span<=j) return S[p];
    elem left = _range(2*p,start,span/2,i,j);
    elem right = _range(2*p+1,start+span/2,span/2,i,j);
    return op(left,right);
  }
  
  // returns op{t[i], t[i+1], ..., t[j]}
  elem range(int i, int j) const {
    return _range(1,0,N,i,j+1);
  }
};

typedef int ent;

struct Fenwick {
  vector<ent> FT;

  void add(int i, ent v);
  ent prefix_sum(int i) const;

  // variante range
  void range_add(int a, int b, ent v);

  ent operator[](int i) const;

  Fenwick(int n) {
    FT.resize(n+1,0);
  }
};

void Fenwick::add(int i, ent v=1) {
  assert(i>0);
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

void Fenwick::range_add(int a, int b, ent v=1) {
  add(a,v);
  add(b+1,-v);
}

// variante range
ent Fenwick::operator[](int i) const {
  return prefix_sum(i);
}


int N;
vector< unordered_set<int> > G;
int C = 0;
vector<int> Num,Trace,L,R,TR,TL,Ind,Depth;

void dfs(int u=1, int u0=-1) {
  Num[u] = ++C;
  Ind[Num[u]] = u;
  L[Num[u]] = Num[u];
  TL[Num[u]] = Trace.size();
  if (u0>=0) Depth[Num[u]] = Depth[Num[u0]]+1;
  for (auto iv=G[u].begin(); iv!=G[u].end(); ++iv)
    if (*iv!=u0) {
      Trace.push_back(Num[u]);
      dfs(*iv,u);
    }
  Trace.push_back(Num[u]);
  R[Num[u]] = C;
  TR[Num[u]] = Trace.size();
}

// u and v are nums!
int LCA(SegmentTree &SegTrace, int u, int v) {
  if (u>v) swap(u,v);
  if (TL[u]<=TL[v] && TR[v]<=TR[u]) return u;
  return SegTrace.range(TR[u],TL[v]);
}

int main() {
  cin >> N;
  G.resize(N+1);
  for (int i=0; i<N-1; ++i) {
    int x,y;
    cin >> x >> y;
    G[x].insert(y);
    G[y].insert(x);
  }
  Num.resize(N+1);
  Ind.resize(N+1);
  L.resize(N+1); R.resize(N+1);
  TL.resize(N+1); TR.resize(N+1);
  Depth.resize(N+1,0);
  dfs();
  SegmentTree SegTrace(Trace);
  Fenwick F(N+1);
  int Q;
  cin >> Q;
  for (int q=0; q<Q; ++q) {
    char c; int x,y;
    cin >> c >> x >> y;
    if (c=='d') {
      if (G[x].find(y)!=G[x].end()) {
	int u = Num[x], v = Num[y];
	if (u>v) swap(u,v);
	if (F[u]==F[v]) F.range_add(L[v],R[v],1);
      }
    }
    else if (c=='c') {
      if (G[x].find(y)!=G[x].end()) {
	int u = Num[x], v = Num[y];
	if (u>v) swap(u,v);
	if (F[u]!=F[v]) F.range_add(L[v],R[v],-1);
      }
    }
    else if (c=='q') {
      int u = Num[x], v = Num[y];
      int w = LCA(SegTrace,u,v);
      if (F[u]==F[w] && F[v]==F[w]) cout << Depth[u]+Depth[v]-2*Depth[w] << endl;
      else cout << "Impossible" << endl;
    }
  }
  return 0;
}
