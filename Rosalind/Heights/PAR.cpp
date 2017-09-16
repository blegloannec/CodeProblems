#include <iostream>
#include <vector>
using namespace std;

// in-place partition
void partition(vector<int> &A, int pivot=0) {
  swap(A[0],A[pivot]);
  int p = 1;
  for (unsigned int i=1; i<A.size(); ++i)
    if (A[i]<=A[0]) swap(A[i],A[p++]);
  swap(A[0],A[p-1]);
}

int main() {
  int n;
  cin >> n;
  vector<int> A(n);
  for (int i=0; i<n; ++i) cin >> A[i];
  partition(A);
  for (int i=0; i<n; ++i) {
    cout << A[i];
    if (i==n-1) cout << endl;
    else cout << ' ';
  }
  return 0;
}
