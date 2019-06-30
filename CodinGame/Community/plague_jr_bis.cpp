#include <iostream>
#include <vector>
using namespace std;

int n;
vector< vector<int> > T;

int center_dist() {
  vector<int> leaves, degree(n);
  for (int u=0; u<n; ++u) {
    degree[u] = T[u].size();
    if (degree[u]<=1) {
      leaves.push_back(u);
      degree[u] = -1; // to mark treated vertices
    }
  }
  int d = 0;
  while (leaves.size()>=2) {
    vector<int> new_leaves;
    for (int u : leaves)
      for (int v : T[u])
	if (degree[v]>=1 && --degree[v]<=1) {
	  new_leaves.push_back(v);
	  degree[v] = -1;
	}
    swap(leaves, new_leaves);
    ++d;
  }
  return d;
}

int main() {
  cin >> n; ++n;
  T.resize(n);
  for (int i=0; i<n-1; ++i) {
    int u,v;
    cin >> u >> v;
    T[u].push_back(v);
    T[v].push_back(u);
  }
  cout << center_dist() << endl;
  return 0;
}
