/*
  Let us call *red triplets* the triplets we are looking for.
  A triplet (a,b,c) has a unique *center* d, defined as the node from which
  a, b and c are reached following disjoint paths (possibly empty
  if d is in {a,b,c}). d is also for instance the first node in the
  path a ~~ b that you reach when going from c to a or b, or simply
  the intersection of the 3 paths.
  A triplet (a,b,c) of center d is red iff at least 2 of the paths d~~a, d~~b
  and d~~c contain a red edge.
  In the following , we use a linear DP on the tree to count the triplets,
  each vertex u contributes to the final result by adding the red triplets
  centered at u.  

  NB: The editorial suggests a simpler and more elegant solution (same
      complexity though), relying on the sizes of the connected components
      of the tree without its red edges.
*/
#include <iostream>
#include <vector>
using namespace std;
using ll = long long;

typedef pair<int,bool> edge;
#define _v_ first
#define _red_ second

const ll P = 1000000007;
int N;
vector< vector<edge> > T;
vector<int> SubRed, SubBlack;

void addmod(ll &a, ll b) {
  a = (a + (b%P)) % P;
}

/*
  We use 0 as an arbitrary root.
  First pass DFS to count colors withing subtrees:
  SubBlack[u] = nb of nodes v in the subtree rooted at u such that
                path u~~v is fully black
  SubRed[u]   = the complementary
*/
void dfs_sub(int u=0, int u0=-1) {
  for (auto iv=T[u].begin(); iv!=T[u].end(); ++iv) {
    int v = iv->_v_;
    if (v!=u0) {
      dfs_sub(v, u);
      SubRed[u] += SubRed[v];
      if (iv->_red_) SubRed[u] += SubBlack[v];
      else SubBlack[u] += SubBlack[v];
    }
  }
}

ll dfs_count_triplets(int u=0, int u0=-1, int SupRed=0, int SupBlack=0) {
  ll res = 0;
  int TotalRed = SupRed + SubRed[u];
  int TotalBlack = SupBlack + SubBlack[u];
  ll SumChildRed = 0, SumChildBlack = 0;
  ll SumChildRed2 = 0, SumChildRedBlack = 0;
  for (auto iv=T[u].begin(); iv!=T[u].end(); ++iv) {
    int v = iv->_v_;
    // counting red triplets centered at u (not hard but slightly tedious)
    ll ChildRed, ChildBlack;
    if (v==u0) {
      ChildRed = SupRed;
      ChildBlack = SupBlack;
    }
    else if (iv->_red_) {
      ChildRed = SubRed[v] + SubBlack[v];
      ChildBlack = 0;
    }
    else {
      ChildRed = SubRed[v];
      ChildBlack = SubBlack[v];
    }
    addmod(res, SumChildRed*ChildRed);
    addmod(res, SumChildRed2*ChildBlack);
    addmod(res, SumChildRed2*ChildRed);
    addmod(res, SumChildRedBlack*ChildRed);
    addmod(SumChildRed2, SumChildRed*ChildRed);
    addmod(SumChildRedBlack, SumChildBlack*ChildRed);
    addmod(SumChildRedBlack, SumChildRed*ChildBlack);
    addmod(SumChildRed, ChildRed);
    addmod(SumChildBlack, ChildBlack);
    // moving to children
    if (v!=u0) {
      int vSupRed = TotalRed - SubRed[v];
      int vSupBlack = TotalBlack - SubBlack[v];
      if (iv->_red_) {
	vSupRed += vSupBlack;
	vSupBlack = 0;
      }
      addmod(res, dfs_count_triplets(v, u, vSupRed, vSupBlack));
    }
  }
  return res;
}

int main() {
  cin >> N;
  T.resize(N);
  SubRed.resize(N,0);
  SubBlack.resize(N,1);
  for (int i=0; i<N-1; ++i) {
    int u,v;
    char c;
    cin >> u >> v >> c; --u; --v;
    bool red = c=='r';
    T[u].push_back(make_pair(v,red));
    T[v].push_back(make_pair(u,red));
  }
  dfs_sub();
  cout << dfs_count_triplets() << endl;
  return 0;
}
