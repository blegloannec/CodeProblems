#include <iostream>
using namespace std;

typedef long long ent;

int main() {
  int n,f;
  ent res,a,b,c;
  cin >> n;
  for (int i=0; i<n; ++i) {
    cin >> f;
    res = 0L;
    for (int j=0; j<f; ++j) {
      cin >> a >> b >> c;
      res += a*c;
    }
    cout << res << '\n';
  }
  return 0;
}
