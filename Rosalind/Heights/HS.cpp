#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

// NB: MAX heap here

void percolate_down(vector<int> &H, int u) {
  int n = H.size(), l = 2*u+1, r = 2*u+2;
  while ((l<n && H[u]<H[l]) || (r<n && H[u]<H[r])) {
    int v = (r<n && H[r]>=H[l]) ? r : l;
    swap(H[u],H[v]);
    u = v; l = 2*u+1; r = 2*u+2;
  }
}

void heapify(vector<int> &H) {
  for (int i=((int)H.size()-2)/2; i>=0; --i)
    percolate_down(H,i);
}

int heap_pop(vector<int> &H) {
  assert(!H.empty());
  int root = H[0];
  H[0] = H.back();
  H.pop_back();
  percolate_down(H,0);
  return root;
}

void heap_sort(vector<int> &A, vector<int> &B) {
  heapify(A);
  int n = A.size();
  B.resize(n);
  for (int i=n-1; i>=0; --i) B[i] = heap_pop(A);
}

int main() {
  int n;
  cin >> n;
  vector<int> A(n),B;
  for (int i=0; i<n; ++i) cin >> A[i];
  heap_sort(A,B);
  for (int i=0; i<n; ++i)
    cout << B[i] << (i==n-1 ? '\n' : ' ');
  return 0;
}
