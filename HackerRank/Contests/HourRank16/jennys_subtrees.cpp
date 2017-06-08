#include <cstdio>
#include <vector>
#include <algorithm>
#include <unordered_set>
using namespace std;

typedef long long ll;
vector<ll> hfactor;
typedef vector< vector<int> > graph;
typedef vector<bool> mask;

/*
  A center of a tree is a vertex that minimize the maximal distance
  to any other vertex. There is either 1 center or 2 centers that are
  neighbors (in that case, one could say the center is an edge).
  Algorithm: one step consists in listing the leaves and removing all of them,
  repeat that step by step until the tree has 1 or 2 vertices.
*/

/*
// standard versions
vector<int> center(graph &T) {
  int n = T.size();
  vector< vector<int> > leaves(2);
  vector<int> degree(n);
  for (int u=0; u<n; ++u) {
    degree[u] = T[u].size();
    // degree can be 0 for the one vertex tree
    if (degree[u]<=1) {
      leaves[0].push_back(u);
      degree[u] = -1; // to mark treated vertices
    }
  }
  int c = 0;
  while (leaves[c].size()>2) {
    int d = (c+1)%2;
    for (vector<int>::iterator iu=leaves[c].begin(); iu!=leaves[c].end(); ++iu)
      for (vector<int>::iterator iv=T[*iu].begin(); iv!=T[*iu].end(); ++iv)
	if (degree[*iv]>=1 && --degree[*iv]<=1) {
	  leaves[d].push_back(*iv);
	  degree[*iv] = -1;
	}
    leaves[c].clear();
    c = d;
  }
  return leaves[c];
}

ll rooted_tree_hash(graph &T, int u, int u0=-1) {
  vector<ll> H;
  for (vector<int>::iterator iv=T[u].begin(); iv!=T[u].end(); ++iv)
    if (*iv!=u0) H.push_back(rooted_tree_hash(T,*iv,u));
  sort(H.begin(),H.end());
  ll h = 123456789123456L;
  for (unsigned int i=0; i<H.size(); ++i)
    h ^= hfactor[i]*H[i];
  return h;
}

ll tree_hash(graph &T) {
  vector<int> ctr = center(T);
  ll res = 1;
  for (vector<int>::iterator it=ctr.begin(); it!=ctr.end(); ++it)
    res *= rooted_tree_hash(T,*it);
  return res;
}
*/

void dfs_degree(graph &T, vector<int> &degree, mask &subleaf, vector<int> &leaves, int r, int u, int d=0, int u0=-1) {
  if (d==r) {
    degree[u] = 1;
    subleaf[u] = true;
  }
  else {
    degree[u] = T[u].size();
    for (vector<int>::iterator iv=T[u].begin(); iv!=T[u].end(); ++iv)
      if (*iv!=u0) dfs_degree(T,degree,subleaf,leaves,r,*iv,d+1,u);
  }
  if (degree[u]<=1) {
    leaves.push_back(u);
    degree[u] = -1;
  }
}

// radius versions
vector<int> center(graph &T, int r, int u, mask &subleaf) {
  vector< vector<int> > leaves(2);
  vector<int> degree(T.size(),0);
  dfs_degree(T,degree,subleaf,leaves[0],r,u);
  int c = 0;
  while (leaves[c].size()>2) {
    int d = (c+1)%2;
    for (vector<int>::iterator iu=leaves[c].begin(); iu!=leaves[c].end(); ++iu)
      for (vector<int>::iterator iv=T[*iu].begin(); iv!=T[*iu].end(); ++iv)
	if (degree[*iv]>=1 && --degree[*iv]<=1) {
	  leaves[d].push_back(*iv);
	  degree[*iv] = -1;
	}
    leaves[c].clear();
    c = d;
  }
  return leaves[c];
}

ll rooted_tree_hash(graph &T, mask &subleaf, int u, int u0=-1) {
  ll h = 123456789123LL;
  if (subleaf[u]) return h; // leaf
  vector<ll> H;
  for (vector<int>::iterator iv=T[u].begin(); iv!=T[u].end(); ++iv)
    if (*iv!=u0)
      H.push_back(rooted_tree_hash(T,subleaf,*iv,u));
  sort(H.begin(),H.end());
  for (unsigned int i=0; i<H.size(); ++i) h ^= hfactor[i]*H[i];
  return h;
}

ll tree_hash(graph &T, int r, int u) {
  mask subleaf(T.size(),false);
  vector<int> ctr = center(T,r,u,subleaf);
  ll res = rooted_tree_hash(T,subleaf,ctr[0]); 
  if (ctr.size()>1) res *= rooted_tree_hash(T,subleaf,ctr[1]);
  return res;
}

int main() {
  srand(1496407411);
  int n,r,a,b;
  scanf("%d %d",&n,&r);
  for (int i=0; i<n; ++i) hfactor.push_back((ll)rand() | ((ll)rand()<<32));
  graph G(n);
  for (int i=0; i<n-1; ++i) {
    scanf("%d %d",&a,&b);
    --a; --b;
    G[a].push_back(b);
    G[b].push_back(a);
  }
  unordered_set<ll> H;
  for (int u=0; u<n; ++u) H.insert(tree_hash(G,r,u));
  printf("%d\n",(int)H.size());
  return 0;
}
