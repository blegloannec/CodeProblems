#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int main() {
  int n,m;
  cin >> n >> m;
  vector<int> A(n);
  for (int i=0; i<n; ++i) cin >> A[i];
  vector< unordered_map<int,int> > C(m+1);
  C[0][0] = 1;
  for (int i=1; i<=n; ++i)
    for (int j=min(m,i)-1; j>=0; --j)
      for (auto it=C[j].begin(); it!=C[j].end(); ++it)
	C[j+1][it->first+A[i-1]] += it->second;
  int res = 0;
  for (auto it=C[m].begin(); it!=C[m].end(); ++it)
    if (it->second==1) res += it->first;
  cout << res << endl;
  return 0;
}
