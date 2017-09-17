#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int n;
vector<int> A;
unordered_map< int, pair<int,int> > H;

// O(n^2) approach, ~5s with -O3 (and almost 1 min without optimization)
bool three_sum(int &i1, int &i2, int &i3) {
  H.clear();
  for (int i=0; i<n; ++i) {
    if (H.find(-A[i])!=H.end()) {
      i1 = H[-A[i]].first;
      i2 = H[-A[i]].second;
      i3 = i;
      return true;
    }
    for (int j=0; j<i; ++j)
      H[A[j]+A[i]] = make_pair(j,i);
  }
  return false;
}

int main() {
  int k;
  cin >> k >> n;
  A.resize(n);
  for (int t=0; t<k; ++t) {
    for (int i=0; i<n; ++i) cin >> A[i];
    int a,b,c;
    if (three_sum(a,b,c)) cout << a+1 << ' ' << b+1 << ' ' << c+1 << endl;
    else cout << -1 << endl;
  }
  return 0;
}
