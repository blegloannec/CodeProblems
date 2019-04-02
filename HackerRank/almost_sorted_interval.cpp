/*
  O(N log N)  Stack-based Next Greater Element  +  Fenwick
  NB: Not using the fact that P is a permutation (works for arbitrary P).
*/
#include <cstdio>
#include <vector>
using namespace std;


// == Fenwick Trees == //
typedef int ent;

struct Fenwick {
  vector<ent> FT;

  void add(int i, ent v);
  ent prefix_sum(int i) const;

  Fenwick(int n) {
    FT.resize(n+1,0);
  }
};

void Fenwick::add(int i, ent v=1) {
  ++i;
  while (i<(int)FT.size()) {
    FT[i] += v;
    i += i&-i;
  }
}

ent Fenwick::prefix_sum(int i) const { // prefix sum
  ++i;
  ent s = 0;
  while (i>0) {
    s += FT[i];
    i -= i&-i;
  }
  return s;
}
// ===== //


int main() {
  int N;
  scanf("%d", &N);
  vector<int> P(N);
  for (int i=0; i<N; ++i) scanf("%d", &P[i]);
  // pre-computation: next smaller element
  vector<int> S;
  vector<int> NextSmaller(N,-1);
  for (int i=N-1; i>=0; --i) {
    while (!S.empty() && P[S.back()]>=P[i]) S.pop_back();
    if (!S.empty()) NextSmaller[i] = S.back();
    S.push_back(i);
  }
  // main computation: previous greater element + fenwick
  long long res = 0;
  S.clear();
  vector< vector<int> > LeftEnds(N);
  Fenwick FT(N);
  for (int i=0; i<N; ++i) {
    // adding i as a left end
    FT.add(i);
    if (NextSmaller[i]>=0) LeftEnds[NextSmaller[i]].push_back(i);
    // removing current left ends that are greater than P[i]
    for (auto it=LeftEnds[i].begin(); it!=LeftEnds[i].end(); ++it) FT.add(*it,-1);
    // considering i as a right end
    while (!S.empty() && P[S.back()]<=P[i]) S.pop_back();
    res += FT.prefix_sum(i);
    if (!S.empty()) res -= FT.prefix_sum(S.back());
    S.push_back(i);
  }
  printf("%lld\n", res);
  return 0;
}
