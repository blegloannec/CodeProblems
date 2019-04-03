/*
  O(N) stack-based previous smaller element approach
  First of all, the given boolean function easily reduces to XOR
  (that observation is useless to solve the problem though).
  Given an interval [l,r], the value associated to this interval
  is the same as the one associated to the interval [l',r']
  where l<=l'<=r'<=r and A[l'] & A[r'] are the two smallest values of
  [l,r]. Then, either A[l']<=A[r'] and A[l'] is the previous smaller
  value of A[r'], or the contrary.
*/
#include <cstdio>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

int max_xor_smallest_pair(vector<int> &A) {
  int res = 0;
  stack<int> S;
  for (int i=0; i<(int)A.size(); ++i) {
    while (!S.empty() && S.top()>A[i]) {
      /* Small "trick" to do the reverse in one single pass:
	 A[i] is the next smaller value of S.top()           */
      res = max(res, A[i]^S.top());
      S.pop();
    }
    if (!S.empty()) res = max(res, A[i]^S.top());
    S.push(A[i]);
  }
  return res;
}

int main() {
  int N;
  scanf("%d", &N);
  vector<int> A(N);
  for (int i=0; i<N; ++i) scanf("%d", &A[i]);
  printf("%d\n", max_xor_smallest_pair(A));
  return 0;
}
