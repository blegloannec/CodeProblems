#include <iostream>
#include <vector>
using namespace std;

int n;
vector<int> A;

// Boyer-Moore algorithm, O(n) time, O(1) space
int maj() {
  int c, cpt = 0;
  for (int i=0; i<n; ++i) {
    if (cpt==0) c = A[i];
    cpt += (A[i]==c ? 1 : -1);
  }
  // c is our candidate, let's verify
  cpt = 0;
  for (int i=0; i<n; ++i)
    if (A[i]==c) ++cpt;
  return (2*cpt>n ? c : -1);
}

int main() {
  int k;
  cin >> k >> n;
  A.resize(n);
  for (int t=1; t<=k; ++t) {
    for (int i=0; i<n; ++i) cin >> A[i];
    cout << maj();
    if (t==k) cout << endl;
    else cout << ' ';
  }
  return 0;
}
