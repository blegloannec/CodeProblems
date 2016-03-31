#include <iostream>
#include <algorithm>
using namespace std;

typedef long long ent;

ent pgcd(ent a, ent b) {
  if (b==0) return a;
  else return pgcd(b, a%b);
}

int main() {
  int t, c;
  ent a, s, N, m;

  cin >> t;
  while (t-->0) {
    cin >> c;
    N = -1;
    m = -1;
    while (c-->0) {
      s = 0;
      for (int i=0; i<10; ++i) {
	cin >> a;
	if (i==9) s -= a;
	else s += a;
      }
      m = max(m,a);
      if (N<0) N=s;
      else N = pgcd(s,N);
    }
    if ((N>1)&&(m<N)) cout << N << '\n';
    else cout << "impossible\n";
  }

  return 0;
}
