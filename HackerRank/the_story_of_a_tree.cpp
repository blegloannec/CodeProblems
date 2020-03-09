#include <cstdio>
#include <vector>
using namespace std;

int gcd(int a, int b) {
  return b==0 ? a : gcd(b, a%b);
}

int N;
vector< vector<int> > T;
vector<int> Parent, Trace, Left, Right;

void dfs_trace(int u=0, int u0=-1) {
  Parent[u] = u0;
  Left[u] = Trace.size();   // included
  Trace.push_back(u);
  for (int v : T[u])
    if (v!=u0) dfs_trace(v, u);
  Right[u] = Trace.size();  // excluded
}

int main() {
  int Q;
  scanf("%d", &Q);
  for (int q=0; q<Q; ++q) {
    scanf("%d", &N);
    T.resize(N);
    for (int i=0; i<N-1; ++i) {
      int u,v;
      scanf("%d %d", &u, &v); --u; --v;
      T[u].push_back(v);
      T[v].push_back(u);
    }
    Parent.resize(N);
    Left.resize(N);
    Right.resize(N);
    dfs_trace();
    vector<int> Count(N+1,0);
    int G,K;
    scanf("%d %d", &G, &K);
    for (int i=0; i<G; ++i) {
      int u,v;
      scanf("%d %d", &u, &v); --u; --v;
      // guess: parent(v) = u
      if (Parent[v]==u) {
	// the root can be any vertex except the subtree of v
	if (Left[v]>0) {
	  ++Count[0];
	  --Count[Left[v]];
	}
	++Count[Right[v]];
      }
      else {
	// the root can be any vertex from the subtree of u
	++Count[Left[u]];
	--Count[Right[u]];
      }
    }
    int res = 0;
    for (int u=0; u<N; ++u) {
      if (u>0) Count[u] += Count[u-1];
      if (Count[u]>=K) ++res;
    }
    int g = gcd(res, N);
    printf("%d/%d\n", res/g, N/g);
    // cleaning
    T.clear();
    Trace.clear();
  }
  return 0;
}
