/*
  k-th ancestor requests on a tree in O(N log N) through
  2^i-th-parent links tables for each node
  (also a classic technique for the LCA Lowest Common Ancestor problem)
*/
#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

const int XMAX = 100001;
int N, Root;
vector<int> Depth;
vector< vector<int> > Parents, Children;

void build_parent_links(int u) {
  assert(Parents[u].size()==1);
  int k = 1;
  while ((1<<k)<=Depth[u]) {
    Parents[u].push_back(Parents[Parents[u].back()][k-1]);
    ++k;
  }
}

int kth_parent(int x, int k) {
  int i = 0;
  while (x>0 && k && i<(int)Parents[x].size()) {
    if (k&1) x = Parents[x][i];
    k >>= 1;
    i += 1;
  }
  return k==0 ? x : 0;
}

void dfs_precomp(int u, int d=0) {
  Depth[u] = d;
  build_parent_links(u);
  for (int v : Children[u]) dfs_precomp(v,d+1);
}

void new_node(int x, int x0) {
  assert(Depth[x]<0);
  assert(Depth[x0]>=0);
  Depth[x] = Depth[x0]+1;
  Parents[x].push_back(x0);
  build_parent_links(x);
}

void delete_leaf(int x) {
  assert(Depth[x]>=0);
  Depth[x] = -1;
  Parents[x].clear();
}

int main() {
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    cin >> N;
    Parents.resize(XMAX);
    Children.resize(XMAX);
    for (int i=0; i<N; ++i) {
      int x,x0;
      cin >> x >> x0;
      Parents[x].push_back(x0);
      Children[x0].push_back(x);
      if (x0==0) Root = x;
    }
    Depth.resize(XMAX,-1);
    dfs_precomp(Root);
    int Q;
    cin >> Q;
    for (int q=0; q<Q; ++q) {
      int c;
      cin >> c;
      if (c==0) {
	int x0,x;
	cin >> x0 >> x;
	new_node(x,x0);
      }
      else if (c==1) {
	int x;
	cin >> x;
	delete_leaf(x);
      }
      else {
	int x,k;
	cin >> x >> k;
	cout << kth_parent(x,k) << endl;
      }
    }
    // cleaning
    Parents.clear();
    Children.clear();
    Depth.clear();
  }
  return 0;
}
