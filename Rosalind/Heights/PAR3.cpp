#include <iostream>
#include <vector>
using namespace std;

void partition(vector<int> &A, int pivot=0) {
  swap(A[0],A[pivot]);
  int p1 = 0, p2 = 1;
  for (unsigned int i=1; i<A.size(); ++i)
    if (A[i]<=A[p1]) {
      if (A[i]<A[p1]) swap(A[i],A[p1++]);
      swap(A[i],A[p2++]);
    }
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
