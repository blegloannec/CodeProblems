#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>
#include <cstdio>
#include <ctime>
using namespace std;

typedef long long ll;
vector<ll> hfactor;
typedef vector< vector<int> > graph;

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
  vector<int> leaves, degree(n);
  for (int u=0; u<n; ++u) {
    degree[u] = T[u].size();
    // degree can be 0 for the one vertex tree
    if (degree[u]<=1) {
      leaves.push_back(u);
      degree[u] = -1; // to mark treated vertices
    }
  }
  while (leaves[c].size()>=2) {
    vector<int> new_leaves;
    for (vector<int>::iterator iu=leaves.begin(); iu!=leaves.end(); ++iu)
      for (vector<int>::iterator iv=T[*iu].begin(); iv!=T[*iu].end(); ++iv)
	if (degree[*iv]>=1 && --degree[*iv]<=1) {
	  new_leaves.push_back(*iv);
	  degree[*iv] = -1;
	}
    if (new_leaves.empty()) break;
    swap(leaves, new_leaves);
  }
  return leaves;
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

bool isin(int mask, int i) {
  return ((mask>>i)&1)!=0;
}

// masked versions (the mask defines a subgraph)
vector<int> center(graph &T, int mask) {
  int n = T.size();
  vector<int> leaves, degree(n,0);
  for (int u=0; u<n; ++u)
    if (isin(mask,u)) {
      for (vector<int>::iterator iv=T[u].begin(); iv!=T[u].end(); ++iv)
	if (isin(mask,*iv)) ++degree[u];
      if (degree[u]<=1) {
	leaves.push_back(u);
	degree[u] = -1;
      }
    }
  while (leaves.size()>=2) {
    vector<int> new_leaves;
    for (vector<int>::iterator iu=leaves.begin(); iu!=leaves.end(); ++iu)
      for (vector<int>::iterator iv=T[*iu].begin(); iv!=T[*iu].end(); ++iv)
	if (isin(mask,*iv) && degree[*iv]>=1 && --degree[*iv]<=1) {
	  new_leaves.push_back(*iv);
	  degree[*iv] = -1;
	}
    if (new_leaves.empty()) break;
    swap(leaves, new_leaves);
  }
  return leaves;
}

ll rooted_tree_hash(graph &T, int mask, int u, int u0=-1) {
  vector<ll> H;
  for (vector<int>::iterator iv=T[u].begin(); iv!=T[u].end(); ++iv)
    if (isin(mask,*iv) && *iv!=u0) H.push_back(rooted_tree_hash(T,mask,*iv,u));
  sort(H.begin(),H.end());
  ll h = 123456789123456L;
  for (unsigned int i=0; i<H.size(); ++i)
    h ^= hfactor[i]*H[i];
  return h;
}

ll tree_hash(graph &T, int mask) {
  vector<int> ctr = center(T,mask);
  ll res = 1;
  for (vector<int>::iterator it=ctr.begin(); it!=ctr.end(); ++it)
    res *= rooted_tree_hash(T,mask,*it);
  return res;
}

bool connected_subtree(graph &G, int mask) {
  int cpt = 0;
  for (int u=0; u<(int)G.size(); ++u)
    if (isin(mask,u)) {
      ++cpt;
      for (vector<int>::iterator iv=G[u].begin(); iv!=G[u].end(); ++iv)
	if (u<*iv && isin(mask,*iv)) --cpt;
    }
  return cpt==1;
}

int main() {
  srand(time(NULL));
  int n,a,b;
  cin >> n;
  for (int i=0; i<n; ++i)
    hfactor.push_back(rand());
  graph G(n);
  for (int i=0; i<n-1; ++i) {
    cin >> a >> b; --a; --b;
    G[a].push_back(b);
    G[b].push_back(a);
  }
  unordered_set<ll> H;
  for (int mask=1; mask<(1<<n); ++mask)
    if (connected_subtree(G,mask))
      H.insert(tree_hash(G,mask));
  cout << H.size() << endl;
  return 0;
}
