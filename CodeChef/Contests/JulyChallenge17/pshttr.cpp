#include <cstdio>
#include <vector>
#include <algorithm>
#include <cassert>
using namespace std;

struct triple {
  int u,v,c,i;
  triple(int u, int v, int c, int i=0) : u(u), v(v), c(c), i(i) {}
  bool operator<(const triple &B) const {
    return c<B.c;
  }
};

struct FenwickXor {
  vector<int> FT;

  void add(int i, int v);
  int prefix_sum(int i) const;

  // variante range
  void range_add(int a, int b, int v);

  int operator[](int i) const;

  FenwickXor(int n) {
    FT.resize(n+1,0);
  }
};

void FenwickXor::add(int i, int v=1) {
  assert(i>0);
  while (i<(int)FT.size()) {
    FT[i] ^= v;
    i += i&-i;
  }
}

int FenwickXor::prefix_sum(int i) const { // prefix sum
  int s = 0;
  while (i>0) {
    s ^= FT[i];
    i -= i&-i;
  }
  return s;
}

void FenwickXor::range_add(int a, int b, int v=1) {
  add(a,v);
  add(b+1,v);
}

int FenwickXor::operator[](int i) const {
  return prefix_sum(i);
}

int N,cpt;
vector< vector<int> > G;
vector<triple> E,Q;
vector<int> L,R;

void dfs(int u=0, int u0=-1) {
  L[u] = cpt++;
  for (vector<int>::iterator iv=G[u].begin(); iv!=G[u].end(); ++iv)
    if (*iv!=u0) dfs(*iv,u);
  R[u] = cpt-1;
}

int main() {
  int T,M,U,V,C,K;
  scanf("%d",&T);
  for (int t=0; t<T; ++t) {
    scanf("%d",&N);
    G.resize(N);
    for (int i=0; i<N-1; ++i) {
      scanf("%d %d %d",&U,&V,&C);
      --U; --V;
      G[U].push_back(V);
      G[V].push_back(U);
      E.push_back(triple(U,V,C));
    }
    sort(E.begin(),E.end());
    scanf("%d",&M);
    for (int i=0; i<M; ++i) {
      scanf("%d %d %d",&U,&V,&K);
      --U; --V;
      Q.push_back(triple(U,V,K,i));
    }
    sort(Q.begin(),Q.end());
    L.resize(N);
    R.resize(N);
    cpt = 0;
    dfs();
    FenwickXor F(N);
    vector<int> res(M);
    int q = 0, e = 0;
    while (q<M) {
      K = Q[q].c;
      while (e<N-1 && E[e].c<=K) {
	V = L[E[e].u]<L[E[e].v] ? E[e].v : E[e].u;
	F.range_add(L[V]+1,R[V]+1,E[e].c);
	++e;
      }
      while (q<M && Q[q].c==K) {
	res[Q[q].i] = F[L[Q[q].u]+1]^F[L[Q[q].v]+1];
	++q;
      }
    }
    for (int i=0; i<M; ++i) printf("%d\n",res[i]);
    //cleaning
    G.clear();
    E.clear();
    Q.clear();
  }
  return 0;
}
