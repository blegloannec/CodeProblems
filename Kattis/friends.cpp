/*
  Counting / enumerating maximal cliques
  Bron-Kerbosch algorithm
  https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
*/
#include <iostream>
#include <vector>
#include <bitset>
#include <algorithm>
using namespace std;

typedef bitset<128> setmask;

const int CMAX = 1000;
int N;
vector<setmask> G;  // graph
vector<int> O;      // ordering

/*
  At any time:
   - R is the current clique
   - P the set of pending vertices that are valid candidates to extend R
     (i.e. are neighbors to all vertices in R)
   - X is the set of excluded vertices that are valid candidates too
*/
int Bron_Kerbosch(setmask &R, setmask &P, setmask &X) {
  if (P.none())
    // if X is not empty, then R is not maximal as any vertex
    // in X could be added to form a larger clique
    return X.none() ? 1 : 0;
  else {
    int res = 0;
    int u = -1;  // pivot (initially undefined)
    for (int iv=0; iv<N && res<=CMAX; ++iv) {
      int v = O[iv];
      if (P[v] && (u<0 || !G[u][v])) {  // if v in P - G[u]
	if (u<0) u = v;  // arbitrarily use the 1st vertex in P as pivot
	setmask Pv = P&G[v], Xv = X&G[v];
	R[v] = true;     // we select v
	res += Bron_Kerbosch(R, Pv, Xv);
	R[v] = false;    // we unselect v
	P[v] = false;    // we remove it
	X[v] = true;     // and exclude it for later calls
      }
    }
    return res;
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int M;
  while (cin >> N >> M) {
    G.resize(N);
    vector<int> Deg(N, 0);
    for (int i=0; i<M; ++i) {
      int u,v;
      cin >> u >> v; --u; --v;
      G[u][v] = G[v][u] = true;
      ++Deg[u]; ++Deg[v];
    }
    /*
      For simplicity, we use decreasing degree vertex ordering here
      (the link recommends a degeneracy ordering), which is faster than
      no particular ordering (~20% faster on randomly generated tests),
      but does not make any difference on the Kattis runtime.
    */
    O.resize(N);
    for (int i=0; i<N; ++i) O[i] = i;
    sort(O.begin(), O.end(), [&Deg](int u, int v){ return Deg[u]>Deg[v]; });
    
    setmask R,P,X;
    for (int i=0; i<N; ++i) P[i] = true;
    int res = Bron_Kerbosch(R, P, X);
    if (res>CMAX) cout << "Too many maximal sets of friends." << endl;
    else cout << res << endl;
    G.clear();
  }
  return 0;
}
