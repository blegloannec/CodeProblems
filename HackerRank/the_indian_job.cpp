#include <iostream>
#include <vector>
using namespace std;

int N,G,S;
vector<int> A;

/*
  The problem reduces to finding a 2-partition of A where both
  subsets have a sum <= G.
  let S = sum(A)
  DP in O(N * S/2) to compute all possible sums <= S/2
  with S <= N*max(A) ~ 10^4 here
*/
int dp() {
  int UpSum = S/2+1;
  vector<bool> SubsetSum(UpSum,false);
  SubsetSum[0] = true;
  for (int a : A)
    for (int s=UpSum-1-a; s>=0; --s)
      SubsetSum[s+a] = SubsetSum[s+a] || SubsetSum[s];
  // return the max subset sum <= S/2
  int s = UpSum-1;
  while (!SubsetSum[s]) --s;
  return s;
}

int main() {
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    cin >> N >> G;
    A.resize(N);
    S = 0;
    for (int i=0; i<N; ++i) {
      cin >> A[i];
      S += A[i];
    }
    if (S>2*G) cout << "NO\n";
    else {
      int s = dp(); // s <= S/2 so s <= S-s
      if (S-s<=G) cout << "YES\n";
      else cout << "NO\n";
    }
  }
  return 0;
}
