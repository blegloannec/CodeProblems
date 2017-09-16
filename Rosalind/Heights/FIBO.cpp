#include <iostream>
using namespace std;

int main() {
  int n;
  cin >> n;
  long long u0 = 0, u1 = 1;
  for (int i=2; i<=n; ++i) {
    long long s = u1;
    u1 += u0;
    u0 = s;
  }
  cout << u1 << endl;
  return 0;
}
