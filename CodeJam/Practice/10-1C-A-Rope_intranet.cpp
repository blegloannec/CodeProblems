#include <iostream>
using namespace std;

int T,N;
int A[1000],B[1000];

/*
  We implement here the O(n^2) naive algo.
  However, the problem is equivalent to counting
  the number of inversions of a permutation (sort
  A and B and replace the elements by their indices).
  This can be solved in O(n log n) by a modified merge
  sort: recursively count inversions + sort sub-arrays;
  during the merge of arrays A (first half) and B (second half),
  each time an element of B is the smallest, then there is an
  inversion with every remaining element of A.
*/

int main() {
  int cpt;
  cin >> T;
  for (int t=1; t<=T; ++t) {
    cpt = 0;
    cin >> N;
    for (int n=0; n<N; ++n) {
      cin >> A[n] >> B[n];
      // naive O(n) intersection check
      for (int p=0; p<n; ++p)
	if ((A[p]-A[n])*(B[p]-B[n])<0) ++cpt;
    }
    cout << "Case #" << t << ": " << cpt << endl;
  }
  return 0;
}
