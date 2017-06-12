#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

typedef vector<int> ens;

int N,K;
vector<ens> E;

bool test(int a, int b) {
  unsigned int ia = 0, ib = 0;
  for (int k=1; k<=K; ++k) {
    bool seen = false;
    if (ia<E[a].size() && E[a][ia]==k) {
      ++ia;
      seen = true;
    }
    if (ib<E[b].size() && E[b][ib]==k) {
      ++ib;
      seen = true;
    }
    if (!seen) return false;
  }
  return true;
}

int main() {
  int T;
  scanf("%d",&T);
  for (int t=0; t<T; ++t) {
    scanf("%d %d",&N,&K);
    E.resize(N);
    for (int i=0; i<N; ++i) {
      int l;
      scanf("%d",&l);
      E[i].resize(l);
      for (int j=0; j<l; ++j) scanf("%d",&E[i][j]);
      sort(E[i].begin(),E[i].end());
    }
    int cpt = 0;
    for (int i=0; i<N; ++i)
      for (int j=i+1; j<N; ++j)
	if (test(i,j)) ++cpt;
    printf("%d\n",cpt);
  }
  return 0;
}
