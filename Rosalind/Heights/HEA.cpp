#include <iostream>
#include <vector>
using namespace std;

/*
  O(n) heapification, downward percolation of every element starting from
  the internal nodes at the deepest levels (the last leaf is n-1 so the last
  internal node is (n-2)/2)
  NB: MAX heap here
*/
void heapify(vector<int> &H) {
  int n = H.size();
  for (int i=(n-2)/2; i>=0; --i) {
    int u = i, l = 2*u+1, r = 2*u+2;
    while ((l<n && H[u]<H[l]) || (r<n && H[u]<H[r])) {
      int v = (r<n && H[r]>=H[l]) ? r : l;
      swap(H[u],H[v]);
      u = v; l = 2*u+1; r = 2*u+2;
    }
  }
}

int main() {
  int n;
  cin >> n;
  vector<int> A(n);
  for (int i=0; i<n; ++i) cin >> A[i];
  heapify(A);
  for (int i=0; i<n; ++i)
    cout << A[i] << (i==n-1 ? '\n' : ' ');
  return 0;
}
