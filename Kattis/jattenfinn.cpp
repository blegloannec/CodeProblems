/*
  O(N) approach through accelerated simulation.
  If removing pillar i removes all ]l,r[ pillars, then all pillars ]i,r[
  won't go further than r (they cannot do more damage than i) and we can
  directly jump to the next i = r.
  Acceleration in the left direction requires to remember the left end for
  each visited i (and is not required to pass).
*/
#include <cstdio>
#include <vector>
using namespace std;

int N;
vector<int> B,L;

int fast_left(int l, int &w) {
  if (l<0 || B[l]>=w) return l;
  w += 500*(l-L[l]);
  L[l] = fast_left(L[l], w);
  return L[l];
}

int main() {
  scanf("%d", &N);
  B.resize(N);
  for (int i=0; i<N; ++i) scanf("%d", &B[i]);
  L.resize(N);
  for (int i=0; i<N; ++i) L[i] = i-1;
  int i = 0, imax, pmax = 0;
  while (i<N) {
    int w = 1500, l = i-1, r = i+1;
    bool unstable = true;
    while (unstable) {
      int l0 = l;
      l = fast_left(l, w);
      unstable = l<l0;
      while (r<N && B[r]<w) {
	w += 500;
	unstable = true;
	++r;
      }
    }
    int p = r-l-1;
    if (p>pmax) {
      imax = i;
      pmax = p;
    }
    L[i] = l;
    i = r;
  }
  printf("%d %d\n", pmax, imax);
  return 0;
}
