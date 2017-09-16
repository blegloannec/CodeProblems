#include <iostream>
#include <vector>
using namespace std;

int main() {
  int n,m;
  cin >> n >> m;
  vector<int> D(n,0);
  for (int i=0; i<m; ++i) {
    int u,v;
    cin >> u >> v;
    ++D[u-1]; ++D[v-1];
  }
  for (int i=0; i<n; ++i) {
    cout << D[i];
    if (i==n-1) cout << endl;
    else cout << ' ';
  }
  return 0;
}
