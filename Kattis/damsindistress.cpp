#include <cstdio>
#include <vector>
using namespace std;

int N;
vector<int> Parent, C, U, DP;

int rain(int u) {
  if (DP[u]<0)
    DP[u] = C[u]-U[u] + max(0, rain(Parent[u])-C[u]);
  return DP[u];
}

int main() {
  int W;
  scanf("%d %d", &N, &W);
  Parent.resize(N+1);
  C.resize(N+1);
  U.resize(N+1);
  for (int i=1; i<=N; ++i)
    scanf("%d %d %d", &Parent[i], &C[i], &U[i]);
  DP.resize(N+1, -1);
  DP[0] = W;
  for (int u=1; u<=N; ++u) W = min(W, rain(u));
  printf("%d\n", W);
  return 0;
}
