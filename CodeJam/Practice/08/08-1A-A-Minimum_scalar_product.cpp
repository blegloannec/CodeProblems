#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int T,n;
vector<int> x,y;

int main() {
  int v;
  long long res;
  cin >> T;
  for (int t=1; t<=T; ++t) {
    x.clear(); y.clear();
    cin >> n;
    for (int i=0; i<n; ++i) {cin >> v; x.push_back(v);}
    for (int i=0; i<n; ++i) {cin >> v; y.push_back(v);}
    sort(x.begin(), x.end());
    sort(y.begin(), y.end());
    res = 0;
    for (int i=0; i<n; ++i) res += (long long)x[i]*(long long)y[n-1-i];
    // Attention au dépassement, cast obligatoire ici !
    cout << "Case #" << t << ": " << res << endl;
  }
  return 0;
}
