#include <iostream>
#include <vector>
using namespace std;

void merge_sort(vector<int> &A, int i, int j, vector<int> &B) {
  if (i==j) {
    B.push_back(A[i]);
    return;
  }
  int m = (i+j)/2;
  vector<int> B1,B2;
  merge_sort(A,i,m,B1);
  merge_sort(A,m+1,j,B2);
  unsigned int i1 = 0, i2 = 0;
  while (i1<B1.size() || i2<B2.size()) {
    if (i1<B1.size() && (i2==B2.size() || B1[i1]<=B2[i2]))
      B.push_back(B1[i1++]);
    else B.push_back(B2[i2++]);
  }
}

int main() {
  int n;
  cin >> n;
  vector<int> A(n),B;
  for (int i=0; i<n; ++i) cin >> A[i];
  merge_sort(A,0,n-1,B);
  for (int i=0; i<n; ++i) {
    cout << B[i];
    if (i==n-1) cout << endl;
    else cout << ' ';
  }
  return 0;
}
