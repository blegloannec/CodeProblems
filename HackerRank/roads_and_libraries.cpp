#include <iostream>
#include <vector>
using namespace std;

long long N, Clib, Croad, Comp;
vector<int> T;

int find(int x) {
  if (T[x]<0) return x;
  T[x] = find(T[x]);
  return T[x];
}

void merge(int x, int y) {
  int x0 = find(x), y0 = find(y);
  if (x0!=y0) {
    T[y0] = x0;
    --Comp;
  }
}

int main() {
  int Q;
  cin >> Q;
  for (int q=0; q<Q; ++q) {
    int M;
    cin >> N >> M >> Clib >> Croad;
    T.resize(N,-1);
    Comp = N;
    for (int i=0; i<M; ++i) {
      int u,v;
      cin >> u >> v; --u; --v;
      merge(u,v);
    }
    cout << (Clib<=Croad ? N*Clib : Comp*Clib + (N-Comp)*Croad) << endl;
    // cleaning
    T.clear();
  }
  return 0;
}
