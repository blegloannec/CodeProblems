//  Offline approach in O((N+Q) log N)
#include <cstdio>
#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;


/* === Fenwick Trees === */
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
  ++i;
  while (i<(int)FT.size()) {
    FT[i] += v;
    i += i&-i;
  }
}

ent Fenwick::prefix_sum(int i) const { // prefix sum
  ++i;
  ent s = 0;
  while (i>0) {
    s += FT[i];
    i -= i&-i;
  }
  return s;
}
/* ===== */


int N, Q, S, Root, NbCol;
vector< vector<int> > Tree;
vector<int> Color;

vector<int> Trace, SubLeft, SubRight;
void dfs(int u, int u0=-1) {
  SubLeft[u] = Trace.size();
  Trace.push_back(Color[u]);
  for (auto iv=Tree[u].begin(); iv!=Tree[u].end(); ++iv)
    if (*iv!=u0) dfs(*iv,u);
  SubRight[u] = Trace.size()-1;
}

struct query {
  int i0, i1, q;
  
  query(int s, int q) : q(q) {
    i0 = SubLeft[s];
    i1 = SubRight[s];
  }
  
  bool operator<(const query &B) const {
    return i1<B.i1;
  }
};

vector<query> Queries;
vector<int> Results;

void process_queries() {
  sort(Queries.begin(), Queries.end());
  Results.resize(Q);
  Fenwick FT(Trace.size());
  vector<int> LastIdx(NbCol,-1);
  int q = 0;
  for (int i=0; i<N && q<Q; ++i) {
    if (LastIdx[Trace[i]]>=0) FT.add(LastIdx[Trace[i]],-1);
    FT.add(i,1);
    LastIdx[Trace[i]] = i;
    while (q<Q && Queries[q].i1==i) {
      Results[Queries[q].q] = FT.prefix_sum(i) - FT.prefix_sum(Queries[q].i0-1);
      ++q;
    }
  }
}

int main() {
  scanf("%d %d %d", &N, &Q, &Root); --Root;
  Tree.resize(N);
  for (int i=0; i<N-1; ++i) {
    int u,v;
    scanf("%d %d", &u, &v); --u; --v;
    Tree[u].push_back(v);
    Tree[v].push_back(u);
  }
  Color.resize(N);
  for (int i=0; i<N; ++i) scanf("%d", &Color[i]);
  // renumbering/compressing colors
  unordered_map<int,int> ColIdx;
  for (int i=0; i<N; ++i) {
    if (ColIdx.find(Color[i])==ColIdx.end())
      ColIdx[Color[i]] = ColIdx.size();
    Color[i] = ColIdx[Color[i]];
  }
  NbCol = ColIdx.size();
  // trace
  SubLeft.resize(N);
  SubRight.resize(N);
  dfs(Root);
  // queries
  for (int q=0; q<Q; ++q) {
    int s;
    scanf("%d", &s); --s;
    Queries.push_back(query(s,q));
  }
  process_queries();
  for (int q=0; q<Q; ++q) printf("%d\n", Results[q]);
  return 0;
}
