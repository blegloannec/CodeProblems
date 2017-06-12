#include <iostream>
#include <vector>
#include <set>
using namespace std;

int main() {
  set<int> S;
  for (int i=1; i<=500; ++i) S.insert(i);
  vector<int> good;
  for (int i=0; i<100; ++i) {
    int a = *S.begin();
    good.push_back(a);
    S.erase(S.begin());
    for (int j=0; j<i; ++j) S.erase(a+good[j]);
  }
  int T,n;
  cin >> T;
  for (int t=0; t<T; ++t) {
    cin >> n;
    for (int i=0; i<n-1; ++i)
      cout << good[i] << ' ';
    cout << good[n-1] << endl;
  } 
  return 0;
}
