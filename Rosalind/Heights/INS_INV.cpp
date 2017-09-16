#include <iostream>
#include <vector>
using namespace std;

/*
  For INS: The number of swaps is the number of inversions of the initial array
  which can be computed in O(n log n) by a slightly enriched merge sort.

  This code also passes problem INV as is.
*/

int merge_sort_inv(vector<int> &A, int i, int j, vector<int> &B) {
  if (i==j) {
    B.push_back(A[i]);
    return 0;
  }
  int m = (i+j)/2;
  vector<int> B1,B2;
  int inv = merge_sort_inv(A,i,m,B1);
  inv += merge_sort_inv(A,m+1,j,B2);
  unsigned int i1 = 0, i2 = 0;
  while (i1<B1.size() || i2<B2.size()) {
    if (i1<B1.size() && (i2==B2.size() || B1[i1]<=B2[i2]))
      B.push_back(B1[i1++]);
    else {
      B.push_back(B2[i2++]);
      // inversions avec tout le reste de B1
      inv += (int)B1.size()-i1;
    }
  }
  return inv;
}

int main() {
  int n;
  cin >> n;
  vector<int> A(n),B;
  for (int i=0; i<n; ++i) cin >> A[i];
  cout << merge_sort_inv(A,0,n-1,B) << endl;
  return 0;
}
