#include <iostream>
#include <vector>
using namespace std;

typedef pair<int,int> edge;
#define _v_ first
#define _d_ second

int N,K;
vector<bool> Keep;
vector< vector<edge> > Tree, SpanTree;
int SpanSum = 0;

/*
  cut useless branches of the tree
  keeping only the edges linking vertices to keep
*/
int dfs_spansubtree(const edge &e0, int u0=-1) {
  int u = e0._v_;
  int sub_keep = Keep[u] ? 1 : 0;
  for (const edge &e : Tree[u])
    if (e._v_!=u0) sub_keep += dfs_spansubtree(e, u);
  if (0<sub_keep && sub_keep<K) {  // keep the edge e
    SpanTree[u0].push_back(e0);
    SpanTree[u].push_back(make_pair(u0, e0._d_));
    SpanSum += 2*e0._d_;
  }
  return sub_keep;
}

/*
  DP for the longest path in a weighted tree
*/
int LongestPath = 0;
int weighted_tree_longest_path(int u, int u0=-1) {
  int l1 = 0, l2 = 0;
  for (const edge &e : SpanTree[u])
    if (e._v_!=u0) {
      int l = e._d_ + weighted_tree_longest_path(e._v_, u);
      if (l>=l1) {l2 = l1; l1 = l;}
      else if (l>l2) l2 = l;
    }
  LongestPath = max(LongestPath, l1+l2);
  return l1;
}

int main() {
  cin >> N >> K;
  Keep.resize(N,false);
  int u0;
  for (int i=0; i<K; ++i) {
    cin >> u0; --u0;
    Keep[u0] = true;
  }
  Tree.resize(N);
  for (int i=0; i<N-1; ++i) {
    int u,v,d;
    cin >> u >> v >> d; --u; --v;
    Tree[u].push_back(make_pair(v,d));
    Tree[v].push_back(make_pair(u,d));
  }
  SpanTree.resize(N);
  dfs_spansubtree(make_pair(0,0));
  weighted_tree_longest_path(u0);
  /*
    the solution is the double total weight of the reduced tree
     - the longest path
    (indeed, starting the tour at one end of the longest path and ending it
     at the other end, we only pay it once, and all the other edges twice)
  */
  cout << SpanSum - LongestPath << endl;
  return 0;
}
