#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int longest_increasing_subsequence(vector<int> &X, vector<int> &sol) {
  // at the beginning of iteration i
  // best[k] contains the smallest value X[j], j<i
  // ending an increasing subsequence of size k
  // we use -1 as as a "-inf" value as elements are non-negative
  vector<int> best(1,-1);
  vector<int> pred(X.size(),-1);
  vector<int> head(1,-1);
  for (int i=0; i<(int)X.size(); ++i) {
    // use > for increasing
    // use >= for non-decreasing
    if (X[i] > best[best.size()-1]) {
      best.push_back(X[i]);
      pred[i] = head[head.size()-1];
      head.push_back(i);
    }
    else {
      // use lower_bound for increasing:
      // dicho search best[k-1] < X[i] <= best[k]
      // use upper_bound for non-decreasing:
      // dicho search best[k-1] <= X[i] < best[k]
      int k = distance(best.begin(),lower_bound(best.begin(),best.end(),X[i]));
      best[k] = X[i];
      head[k] = i;
      pred[i] = head[k-1];
    }
  }
  // extract solution (in reverse)
  int q = head[head.size()-1];
  while (q>=0) {
    sol.push_back(X[q]);
    q = pred[q];
  }
  return best.size()-1;
}

int main() {
  int N;
  cin >> N;
  vector<int> A(N);
  int M = -1;
  for (int i=0; i<N; ++i) {
    cin >> A[i];
    M = max(M,A[i]);
  }
  vector<int> sol;
  longest_increasing_subsequence(A,sol);
  for (int i=sol.size()-1; i>=0; --i) {
    cout << sol[i];
    if (i==0) cout << endl;
    else cout << ' ';
  }
  for (int i=0; i<N; ++i) A[i] = M-A[i];
  sol.clear();
  longest_increasing_subsequence(A,sol);
  for (int i=sol.size()-1; i>=0; --i) {
    cout << M-sol[i];
    if (i==0) cout << endl;
    else cout << ' ';
  }
  return 0;
}
