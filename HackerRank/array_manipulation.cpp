#include <iostream>
#include <vector>
using namespace std;

/*
  Let T be the array that we want to modify over ranges.
  Let A[0] = T[0] and A[i+1] = T[i+1] - T[i]  the differential
  array that we will manipulate instead and that verifies
  T[i] = A[0] + A[1] + ... + A[i].
  Adding k to [a,b[ in T is equivalent to A[a] += k and A[b] -= k.
  Modification is in O(1) and access in O(n) which is ok as there 
  is only the equivalent of 1 access here in the end.
  NB: Fenwick Trees (range/differential version) or Lazy Segment Trees
      do the same with O(log n) for both access and modification
      (hence they would be much more complicated and less efficient here).
  NB: This approach is O(n+m) with n ~ 10^7 and m ~ 10^5.
      As n >> m, it can be optimized in O(m log m) by splitting
      the array at the 2m interval bounds of the requests, thus reducing
      the O(n) space to O(m). This requires however to sort the bounds
      so that the complexity is O(m log m).
*/

typedef long long ent;

int main() {
  int n,m;
  cin >> n >> m;
  vector<ent> A(n,0);
  for (int q=0; q<m; ++q) {
    int a,b;
    ent k;
    cin >> a >> b >> k; --a; --b;
    A[a] += k;
    if (b+1<n) A[b+1] -= k;
  }
  ent S = 0, res = 0;
  for (int i=0; i<n; ++i) {
    S += A[i];
    res = max(res,S);
  }
  cout << res << endl;
  return 0;
}
