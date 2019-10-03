#include <cstdio>
#include <vector>
using namespace std;
using flt = float;

int N;
vector<flt> C, Memo;
vector< vector<int> > DAG;

flt dp(int u=0) {
  if (Memo[u]<0)   {
    flt res = C[u];
    for (int v : DAG[u]) {
      flt sv = dp(v);
      res = max(res, max(sv, C[u]+sv/2));
    }
    Memo[u] = res;
  }
  return Memo[u];
}

int main() {
  int M;
  scanf("%d %d", &N, &M);
  C.resize(N);
  for (int i=0; i<N; ++i) scanf("%f", &C[i]);
  DAG.resize(N);
  for (int i=0; i<M; ++i) {
    int s,t;
    scanf("%d %d", &s, &t);
    DAG[s].push_back(t);
  }
  Memo.resize(N,-1);
  printf("%.6f\n", dp());
  return 0;
}
