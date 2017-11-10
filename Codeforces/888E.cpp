#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n,m;
vector<int> A,X,Y;

void gen(int l, int r, vector<int> &X) {
  X.push_back(0);
  for (int i=l; i<=r; ++i) {
    int s = X.size();
    for (int x=0; x<s; ++x)
      X.push_back((A[i]+X[x])%m);
  }
}

int main() {
  cin >> n >> m;
  A.resize(n);
  for (int i=0; i<n; ++i) cin >> A[i];
  int mid = n/2;
  gen(0,mid,X);
  gen(mid+1,n-1,Y);
  sort(Y.begin(),Y.end());
  int res = 0;
  for (auto ix=X.begin(); ix!=X.end(); ++ix)
    res = max(res,*ix + *(upper_bound(Y.begin(),Y.end(),m-1-*ix)-1));
  cout << res << endl;
  return 0;
}
