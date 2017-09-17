#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
using namespace std;

/*
  Divide and conquer for k-th smallest element, using randomized pivot.
  (also known as "quickselect" by analogy with quicksort)
  Optimal O(n) in average, but O(n^2) in the worst case.
*/

int median(int k, vector<int> &A, int l, int r) {
  int pivot = l + rand()%(r-l+1);
  // 3-partition
  swap(A[l],A[pivot]);
  int p1 = l, p2 = l+1;
  for (int i=l+1; i<=r; ++i)
    if (A[i]<=A[p1]) {
      if (A[i]<A[p1]) swap(A[i],A[p1++]);
      swap(A[i],A[p2++]);
    }
  // branching
  if (k<=p1) return median(k,A,l,p1-1);
  else if (k<=p2) return A[p1];
  else return median(k,A,p2,r);
}

int main() {
  srand(time(NULL));
  int n,k;
  cin >> n;
  vector<int> A(n);
  for (int i=0; i<n; ++i) cin >> A[i];
  cin >> k;
  cout << median(k,A,0,n-1) << endl;
  return 0;
}
