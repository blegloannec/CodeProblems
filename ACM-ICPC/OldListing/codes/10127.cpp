#include <iostream>
using namespace std;

int main() {
  int n;
  while (cin >> n) {
    int res = 0;
    for (int i=1; 1; ++i) {
      res = (10*res + 1) % n;
      if (res == 0) {
        cout << i << '\n';
        break;
      }
    }
  }
  return 0;
}
