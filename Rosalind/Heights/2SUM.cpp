#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int n;
vector<int> A;
unordered_map<int,int> H;

bool two_sum(int &i1, int &i2) {
  H.clear();
  for (int i=0; i<n; ++i) {
    if (H.find(-A[i])!=H.end()) {
      i1 = H[-A[i]];
      i2 = i;
      return true;
    }
    H[A[i]] = i;
  }
  return false;
}

int main() {
  int k;
  cin >> k >> n;
  A.resize(n);
  for (int t=0; t<k; ++t) {
    for (int i=0; i<n; ++i) cin >> A[i];
    int a,b;
    if (two_sum(a,b)) cout << a+1 << ' ' << b+1 << endl;
    else cout << -1 << endl;
  }
  return 0;
}
