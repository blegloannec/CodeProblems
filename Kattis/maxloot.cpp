/*
  The assumption N + 2*log2 V <= 75 is equivalent to 2^N * V^2 <= 2^75
  i.e. V <= 2^((75-N)/2). It guarantees that the larger n is, the
  smaller the values are, which limits the combinatorial explosion.
  Using a DP-like process to compute the min cost for all the possible
  sums of values over a set of size m is bounded by m * min(2^m, #sums)
  where #sums is itself bounded by the sum of values.
  Here computing that on a subset of size n/2 has a guaranteed complexity
  of ~2^18.5 (worst case for n ~ 75/2).
*/
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

typedef vector< pair<int,int> > pairs;

int N,C;
vector<int> V,W;

pairs gen_sums(int l, int r) {
  unordered_map<int,int> H;
  H[0] = 0;
  for (int i=l; i<r; ++i) {
    pairs H0(H.begin(),H.end());
    for (const auto &sc : H0) {
      int s = sc.first+V[i], c = sc.second+W[i];
      if (c<=C) {
	if (H.find(s)==H.end()) H[s] = c;
	else H[s] = min(H[s], c);
      }
    }
  }
  pairs CS0,CS;
  for (const auto &sc : H)
    CS0.push_back(make_pair(sc.second,sc.first));
  sort(CS0.begin(), CS0.end());
  CS.push_back(CS0[0]);
  for (int i=1; i<(int)CS0.size(); ++i) {
    if (CS.back().first==CS0[i].first) CS.back() = CS0[i];
    else if (CS0[i].second>CS.back().second) CS.push_back(CS0[i]);
  }
  return CS;
}

// meet-in-the-middle knapsack
int knapsack() {
  int L = N/2, res = 0;
  auto CSL = gen_sums(0,L);
  auto CSR = gen_sums(L,N);
  int i = 0, j = CSR.size()-1;
  while (i<(int)CSL.size() && j>=0) {
    while (j>=0 && CSL[i].first+CSR[j].first>C) --j;
    if (j>=0) res = max(res, CSL[i].second+CSR[j].second);
    ++i;
  }
  return res;
}

int main() {
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    cin >> N >> C;
    V.resize(N);
    for (int i=0; i<N; ++i) cin >> V[i];
    W.resize(N);
    for (int i=0; i<N; ++i) cin >> W[i];
    cout << knapsack() << '\n';
  }
  return 0;
}
