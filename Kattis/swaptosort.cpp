/*
  Obviously swapping u and v requires that they are connected by some path.
  And it is enough, e.g. u -- a -- b -- c -- v
                         a -- u -- b -- c -- v
                         a -- b -- u -- c -- v
                         a -- b -- c -- u -- v
                         a -- b -- c -- v -- u
                         a -- b -- v -- c -- u
                         a -- v -- b -- c -- u
                         v -- a -- b -- c -- u
  swaps u and v without changing the rest.
*/
#include <cstdio>
#include <vector>
using namespace std;

int N;
vector<int> T;

int find(int x) {
  if (T[x]<0) return x;
  T[x] = find(T[x]);
  return T[x];
}

void merge(int x, int y) {
  int x0 = find(x), y0 = find(y);
  if (x0!=y0) T[y0] = x0;
}

int main() {
  int K;
  scanf("%d %d", &N, &K);
  T.resize(N,-1);
  for (int k=0; k<K; ++k) {
    int a,b;
    scanf("%d %d", &a, &b); --a; --b;
    merge(a, b);
  }
  bool possible = true;
  for (int u=0; u<N/2 && possible; ++u)
    possible = find(u)==find(N-1-u);
  printf(possible ? "Yes\n" : "No\n");
  return 0;
}
