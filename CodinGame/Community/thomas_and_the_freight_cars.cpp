#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> longest_increasing_subsequence(const vector<int> &X) {
  // at the beginning of iteration i
  // best[k] contains the smallest value X[j], j<i
  // ending an increasing subsequence of size k
  vector<int> best(1, -(1<<30));
  vector<int> length(X.size());
  //vector<int> pred(X.size(),-1);
  //vector<int> head(1,-1);
  for (int i=0; i<(int)X.size(); ++i) {
    // use > for increasing
    // use >= for non-decreasing
    if (X[i] > best[best.size()-1]) {
      length[i] = best.size();
      best.push_back(X[i]);
      //pred[i] = head[head.size()-1];
      //head.push_back(i);
    }
    else {
      // use lower_bound for increasing:
      // dicho search best[k-1] < X[i] <= best[k]
      // use upper_bound for non-decreasing:
      // dicho search best[k-1] <= X[i] < best[k]
      int k = distance(best.begin(),lower_bound(best.begin(),best.end(),X[i]));
      length[i] = k;
      best[k] = X[i];
      //head[k] = i;
      //pred[i] = head[k-1];
    }
  }
  //return best.size()-1;
  return length;
  /* // extract solution (in reverse)
  int q = head[head.size()-1];
  vector<int> sol;
  while (q>=0) {
    sol.push_back(X[q]);
    q = pred[q];
  } */
}

int main() {
  int N;
  cin >> N;
  vector<int> A(N);
  for (int i=N-1; i>=0; --i) cin >> A[i];
  vector<int> length1 = longest_increasing_subsequence(A);
  for (int i=0; i<N; ++i) A[i] = -A[i];
  vector<int> length2 = longest_increasing_subsequence(A);
  int res = 0;
  for (int i=0; i<N; ++i)
    res = max(res, length1[i]+length2[i]-1);
  cout << res << endl;
  return 0;
}
