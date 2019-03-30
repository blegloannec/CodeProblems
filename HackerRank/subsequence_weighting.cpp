#include <iostream>
#include <vector>
#include <set>
using namespace std;
using ll = long long;

/*
  DP in O(n log n) for the maximum weight increasing subsequence
  by generalization of the longest increasing subsequence (~ all weights = 1)
*/
ll heaviest_increasing_subsequence(vector<ll> &A, vector<ll> &W) {
  ll res = 0;
  set< pair<ll,ll> > right_ends;
  right_ends.insert(make_pair(0,0));
  for (unsigned int i=0; i<A.size(); ++i) {
    /*
      At the beginning of iteration i, right_ends is a set of pairs
      (last value A[j] of a subseq ending at j<i, weight of the subseq)
      that is increasing in both components (values and weights)
      and "optimal" in the following sense: the maximum weight of a subseq
      ending at i can always be achieved by prolongating a subseq of
      right_ends.
      First, we compute the best subseq ending at i.
    */
    auto it = right_ends.lower_bound(make_pair(A[i],0)); --it;
    ll wi = it->second + W[i];
    res = max(res, wi);
    /*
      Then we update right_ends by removing all (A[j],wj) (j<i) such that
      A[i] <= A[j] and wi >= wj: They are not "optimal" anymore compared
      to (A[j],wj).
      As any element is inserted/erased at most once in/from right_ends,
      this *overall* costs O(n log n).
    */
    ++it;
    while (it!=right_ends.end() && wi>=it->second) {
      auto it0 = it++;
      right_ends.erase(it0);
    }
    if (it==right_ends.end() || A[i]<it->first) right_ends.insert(make_pair(A[i],wi));
  }
  return res;
}

int main() {
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    int N;
    cin >> N;
    vector<ll> A(N), W(N);
    for (int i=0; i<N; ++i) cin >> A[i];
    for (int i=0; i<N; ++i) cin >> W[i];
    cout << heaviest_increasing_subsequence(A,W) << endl;
  }
  return 0;
}
