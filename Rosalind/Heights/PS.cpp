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
  swap(H[(int)H.size()-1],H[0]);
  H.pop_back();
  percolate_down(H,0);
  return root;
}

// O(n + k log n)
void partial_heap_sort(vector<int> &A, int k, vector<int> &B) {
  vector<int> A0 = A;
  for (unsigned int i=0; i<A0.size(); ++i)
    A0[i] = -A0[i]; // because MAX heap
  heapify(A0);
  B.resize(k);
  for (int i=0; i<k; ++i) B[i] = -heap_pop(A0);
}

int main() {
  int n,k;
  cin >> n;
  vector<int> A(n),B;
  for (int i=0; i<n; ++i) cin >> A[i];
  cin >> k;
  partial_heap_sort(A,k,B);
  for (int i=0; i<k; ++i)
    cout << B[i] << (i==k-1 ? '\n' : ' ');
  return 0;
}
