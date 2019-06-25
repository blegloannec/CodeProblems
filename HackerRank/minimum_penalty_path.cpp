/*
  Shortest path for the bitwise OR operation on edges
  O((N+M) log C) approach deducing solution bits from left to right
  and using DFS to check A-B connectedness each time
*/
#include <iostream>
#include <vector>
using namespace std;

const int C = 10;  // solution bits

int N,A,B;
vector< vector< pair<int,int> > > G;
#define _v_ first
#define _c_ second

bool dfs_connected(int mask) {
  vector<bool> seen(N,false);
  seen[A] = true;
  vector<int> S(1,A);
  while (!S.empty()) {
    int u = S.back();
    S.pop_back();
    for (auto &e : G[u])
      if ((mask|e._c_)==mask && !seen[e._v_]) {
	if (e._v_==B) return true;
	S.push_back(e._v_);
	seen[e._v_] = true;
      }
  }
  return false;
}

int main() {
  int M;
  cin >> N >> M;
  G.resize(N);
  for (int i=0; i<M; ++i) {
    int u,v,c;
    cin >> u >> v >> c; --u; --v;
    G[u].push_back(make_pair(v,c));
    G[v].push_back(make_pair(u,c));
  }
  cin >> A >> B; --A; --B;
  // computing solution bits
  int mask = (1<<C)-1;
  if (dfs_connected(mask)) {
    for (int i=C-1; i>=0; --i)
      if (dfs_connected(mask^(1<<i)))
	mask ^= 1<<i;
  }
  else mask = -1;  // unreachable
  cout << mask << endl;
  return 0;
}
