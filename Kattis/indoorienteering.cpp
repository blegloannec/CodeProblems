#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;
using ll = long long;

int N, full, N1,N2;
ll L;
vector< vector<ll> > D;
unordered_map< int, vector<ll> > H;

bool path(int u=0, int mask=1, int l=0, ll d=0LL) {
  if (l==N1 || l==N2) {
    int k = mask | (u<<N);
    H[k].push_back(d);
    int kinv = (k^full) | 1 | (1<<u);
    auto it = H.find(kinv);
    if (it!=H.end() &&
	find(it->second.begin(), it->second.end(), L-d)!=it->second.end())
      return true;
  }
  if (l<N2)
    for (int v=0; v<N; ++v)
      if (((mask>>v)&1)==0)
	if (path(v, mask|(1<<v), l+1, d+D[u][v]))
	  return true;
  return false;
}

int main() {
  cin >> N >> L;
  full = (1<<N)-1;
  N1 = N/2;
  N2 = N-N1;
  D.resize(N, vector<ll>(N));
  for (int i=0; i<N; ++i)
    for (int j=0; j<N; ++j)
      cin >> D[i][j];
  if (!path()) cout << "im";
  cout << "possible" << endl;
  return 0;
}
