#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  int N;
  scanf("%d", &N);
  vector<int> A(N), I(N), L(N), R(N);
  for (int i=0; i<N; ++i) {
    scanf("%d", &A[i]);
    I[i] = i;
    if (i>0) {
      R[i-1] = i;
      L[i] = i-1;
    }
  }
  /*
    sentinel for convenience
    /!\ we use the same for both ends (close the loop)
  */
  A.push_back(1<<30);
  L.push_back(N-1);
  R.push_back(0);
  L[0] = N;
  R[N-1] = N;
  /*
    main algo in O(N log N) (due to the sort)
    eliminate the values in non-decreasing order
    using left/right links to keep track of the current neighbors
  */
  sort(I.begin(), I.end(), [&A](int i, int j){return A[i]<A[j];});
  long long res = 0;
  for (int k=0; k<N-1; ++k) {
    int i = I[k];
    res += min(A[L[i]], A[R[i]]);
    R[L[i]] = R[i];
    L[R[i]] = L[i];
  }
  printf("%lld\n", res);
  return 0;
}
