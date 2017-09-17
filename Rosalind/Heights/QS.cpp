#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
using namespace std;

void quicksort(vector<int> &A, int l, int r) {
  if (r-l<=0) return;
  int pivot = l + rand()%(r-l+1);
  // 3-partition
  swap(A[l],A[pivot]);
  int p1 = l, p2 = l+1;
  for (int i=l+1; i<=r; ++i)
    if (A[i]<=A[p1]) {
      if (A[i]<A[p1]) swap(A[i],A[p1++]);
      swap(A[i],A[p2++]);
    }
  quicksort(A,l,p1-1);
  quicksort(A,p2,r);
}

int main() {
  srand(time(NULL));
  int n;
  cin >> n;
  vector<int> A(n);
  for (int i=0; i<n; ++i) cin >> A[i];
  quicksort(A,0,n-1);
  for (int i=0; i<n; ++i) {
    cout << A[i];
    if (i==n-1) cout << endl;
    else cout << ' ';
  }
  return 0;
}
