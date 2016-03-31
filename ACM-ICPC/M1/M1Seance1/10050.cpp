#include <iostream>
using namespace std;

int h[101];
int N, P;

int main() {
  int T;
  cin >> T;
  while (T-->0) {
    cin >> N >> P;
    for (int i=0; i<P; ++i) 
      cin >> h[i];
    int res = 0;
    for (int i=1; i<=N; ++i) {
      if ((i%7 == 6)||(i%7 == 0)) continue;
      for (int j=0; j<P; ++j) 
        if (i % h[j] == 0) {
          ++res;
          break;
        }
    }
    cout << res << '\n';
  }
  return 0;
}
