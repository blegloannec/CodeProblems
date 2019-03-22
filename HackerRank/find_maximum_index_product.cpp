#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;
using ll = long long;

void previous_greater(vector<int> &A, vector<int> &Left) {
  stack<int> S;
  for (int i=0; i<(int)A.size(); ++i) {
    while (!S.empty() && A[S.top()]<=A[i]) S.pop();
    if (!S.empty()) Left[i] = S.top();
    S.push(i);
  }
}

int main() {
  int N;
  cin >> N;
  vector<int> A(N);
  for (int i=0; i<N; ++i) cin >> A[i];
  vector<int> Left(N,-1), Right(N,-1);
  previous_greater(A,Left);
  reverse(A.begin(),A.end());
  previous_greater(A,Right);
  reverse(Right.begin(),Right.end());
  for (int i=0; i<N; ++i) if (Right[i]>=0) Right[i] = N-1-Right[i];
  ll res = 0;
  for (int i=0; i<N; ++i) res = max(res, ((ll)Left[i]+1)*((ll)Right[i]+1));
  cout << res << endl;
  return 0;
}
