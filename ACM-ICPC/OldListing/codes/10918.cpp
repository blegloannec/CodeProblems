#include <iostream>
using namespace std;

#define MAX 31

int t[MAX];
int tA[MAX];

int main() {
  int n;
  t[0] = 1; // ATTENTION : IDIOT !
  tA[0] = 0;
  t[1] = 0;
  tA[1] = 1;
  t[2] = 3;
  tA[2] = 0;
  for (int i=3; i<MAX; ++i) {
    t[i] = 2*tA[i-1] + t[i-2];
    tA[i] = t[i-1] + tA[i-2];
  }
  while (cin >> n) {
    if (n<0) return 0;
    cout << t[n] << '\n';
  }
  return 0;
}
