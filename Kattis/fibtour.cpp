// longest path in a DAG, except the tediousness is about buiding the DAG
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
using ll = long long;

int N;
const int FibS = 90;
vector<ll> H, Fib;
vector< vector<int> > G;  // we'll make it a DAG
vector<int> L, FibIdx;

int length(int u) {
  if (L[u]<0) {
    L[u] = (int)(FibIdx[u]>=0);
    for (int v : G[u]) L[u] = max(L[u], 1+length(v));
  }
  return L[u];
}

int main() {
  Fib.resize(FibS,1);
  for (int i=2; i<FibS; ++i) Fib[i] = Fib[i-1] + Fib[i-2];
  int M;
  cin >> N >> M;
  H.resize(N); FibIdx.resize(N,-1);
  for (int i=0; i<N; ++i) {
    cin >> H[i];
    int k = H[i]==1 ? 1 : distance(Fib.begin(), lower_bound(Fib.begin(), Fib.end(), H[i]));
    if (k<FibS && Fib[k]==H[i]) FibIdx[i] = k;
  }
  vector<int> Dupe(N);
  int new_id = N;
  for (int u=0; u<N; ++u)
    if (H[u]==1) Dupe[u] = new_id++;
  N = new_id;
  G.resize(N);
  for (int i=0; i<M; ++i) {
    int a,b;
    cin >> a >> b; --a; --b;
    if (H[a]==1 && H[b]==1) {
      G[a].push_back(Dupe[b]);
      G[b].push_back(Dupe[a]);
    }
    else if (FibIdx[a]>=0 && FibIdx[b]>=0) {
      if (FibIdx[a]>FibIdx[b]) swap(a,b);
      if (FibIdx[a]+1==FibIdx[b]) {
	G[a].push_back(b);
	if (H[a]==1) G[Dupe[a]].push_back(b);
      }
    }
  }
  L.resize(N,-1);
  int max_length = 0;
  for (int u=0; u<N; ++u) max_length = max(max_length, length(u));
  cout << max_length << endl;
  return 0;
}
