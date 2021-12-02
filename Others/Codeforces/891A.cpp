#include <iostream>
using namespace std;

int n;
int A[2000];

int gcd(int a, int b) {
  return b==0 ? a : gcd(b,a%b);
}

int main() {
  cin >> n;
  for (int i=0; i<n; ++i) cin >> A[i];
  int smin = n+1, cpt1 = 0;
  for (int l=0; l<n; ++l) {
    int g = A[l];
    if (g==1) {
      smin = 1;
      ++cpt1;
    }
    for (int r=l+1; r<n; ++r) {
      g = gcd(g,A[r]);
      if (g==1 && smin>r-l+1) smin = r-l+1;
    }
  }
  int res = -1;
  if (cpt1>0) res = n-cpt1;
  else if (smin<=n) res = smin-1 + n-1;
  cout << res << endl;
  return 0;
}
