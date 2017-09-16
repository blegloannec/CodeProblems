#include <iostream>
#include <vector>
using namespace std;

int dicho_search(vector<int> &A, int x) {
  int l = 0, r = A.size()-1;
  while (l<r) {
    int m = (l+r)/2;
    if (A[m]<x) l = m+1;
    else r = m;
  }
  return A[l]==x ? l+1 : -1;
}

int main() {
  int n,m;
  cin >> n >> m;
  vector<int> A(n);
  for (int i=0; i<n; ++i) cin >> A[i];
  for (int i=0; i<m; ++i) {
    int x;
    cin >> x;
    cout << dicho_search(A,x);
    if (i==m-1) cout << endl;
    else cout << ' ';
  }
  return 0;
}
