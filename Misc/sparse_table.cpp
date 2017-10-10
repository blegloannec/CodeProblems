#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

/* 
   see for instance:
   https://www.topcoder.com/community/data-science/data-science-tutorials/range-minimum-query-and-lowest-common-ancestor/#Sparse_Table_(ST)_algorithm
*/

typedef int elem;

// MAX sparse table, O(n log n) pre-computation and space, O(1) per request
struct SparseTable {
  int size, depth;
  vector<elem> A;
  vector< vector<elem> > T;
  
  SparseTable(vector<elem> &A0) {
    A = A0;  // copy
    size = A.size();
    depth = 0;
    while ((1<<depth)<=size) ++depth;
    T.resize(depth);
    T[0].resize(size);
    for (int i=0; i<size; ++i) T[0][i] = i;
    for (int k=1; k<depth; ++k) {
      int sizek = size+1-(1<<k), dk = 1<<(k-1);
      T[k].resize(sizek,0);
      for (int i=0; i<sizek; ++i) // MAX
        T[k][i] = A[T[k-1][i]] >= A[T[k-1][i+dk]] ? T[k-1][i] : T[k-1][i+dk];
    }
  }

  int range_index(int l, int r) {
    assert(0<=l && l<=r && r<size);
    int w = r-l+1, k = 0;
    while (w>1) {w >>= 1; ++k;}
    int dk = 1<<k;
    return (A[T[k][l]] >= A[T[k][r-dk+1]] ? T[k][l] : T[k][r-dk+1]);  // MAX
  }

  elem range(int l, int r) {
    return A[range_index(l,r)];
  }
};

int main() {
  vector<int> A {0,2,8,3,7,20,15,2};
  SparseTable S(A);
  cout << S.range(1,4) << endl;
  cout << S.range(5,7) << endl;
  return 0;
}
