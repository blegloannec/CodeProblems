/*
  We have n(n-1)/2 = O(n^2) distances between plugs.
  We want to be able to use all the m cables.
  As n ~ 10^5, we cannot precompute all the distances, we generate
  increasing distances on the fly: when dist(i,j) is used
  (as the currently smallest available distance, for the smallest
  remaining cable) we consider (if not yet available) dist(i,j+1)
  and dist(i-1,j).
*/
#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>
#include <unordered_set>
using namespace std;
using hh = long long;

int N,M;
vector<int> X,L;

struct dist {
  int i,j,d;
  dist(int i, int j) : i(i), j(j) { d = X[j]-X[i]; } // assuming i<j
  hh h() const { return (((hh)j)<<32)|((hh)i); }
  bool operator<(const dist &D) const { return d>D.d; }
};

bool cover() {
  int l = 0;
  priority_queue<dist> Avail;
  unordered_set<hh> Used;
  for (int i=0; i<N-1; ++i) {
    dist D(i,i+1);
    Avail.push(D);
    Used.insert(D.h());
  }
  while (l<M && !Avail.empty() && Avail.top().d<=L[l]) {
    dist D = Avail.top();
    Avail.pop();
    if (D.j+1<N) {
      dist Dr = dist(D.i,D.j+1);
      if (Used.find(Dr.h())==Used.end()) {
	Avail.push(Dr);
	Used.insert(Dr.h());
      }
    }
    if (D.i>0) {
      dist Dl = dist(D.i-1,D.j);
      if (Used.find(Dl.h())==Used.end()) {
	Avail.push(Dl);
	Used.insert(Dl.h());
      }
    }
    ++l;
  }
  return l==M;
}

int main() {
  scanf("%d %d", &N, &M);
  X.resize(N);
  for (int i=0; i<N; ++i) scanf("%d", &X[i]);
  L.resize(M);
  for (int i=0; i<M; ++i) scanf("%d", &L[i]);
  sort(L.begin(), L.end());
  if (cover()) printf("yes\n");
  else printf("no\n");
  return 0;
}
