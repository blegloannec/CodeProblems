#include <iostream>
#include <vector>
using namespace std;

int N, Sum = 0;
vector<int> Data;
vector< vector<int> > T;

int subsum_dfs(int u=0, int u0=-1) {
  for (auto iv=T[u].begin(); iv!=T[u].end(); ++iv)
    if (*iv!=u0) Data[u]+= subsum_dfs(*iv,u);
  return Data[u];
}

int main() {
  cin >> N;
  Data.resize(N);
  for (int i=0; i<N; ++i) {
    cin >> Data[i];
    Sum += Data[i];
  }
  T.resize(N);
  for (int i=0; i<N-1; ++i) {
    int u,v;
    cin >> u >> v; --u; --v;
    T[u].push_back(v);
    T[v].push_back(u);
  }
  subsum_dfs();
  int res = Sum;
  for (int u=0; u<N; ++u)
    res = min(res, abs(Data[u]-(Sum-Data[u])));
  cout << res << endl;
  return 0;
}
